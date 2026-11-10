# -*- coding: utf-8 -*-
"""クライアント送付用：パターン② × デザインA の TOP だけを、単独で開けるフォルダに書き出す（2026-11-10）。
・元のサイト（/pattern2/ など）には手を加えない。ここで作るのは送付用のコピー。
・リンクはすべて無効（href・target・rel を外し、aria-disabled を付ける。見た目はそのまま）。
・デモ用の部品（パターン切替バー・確認用/公開イメージの切替・デモの注記）は外し、公開イメージで表示する。
・使っているCSS・JS・フォント・写真だけを assets/ に集める（他のページの変更の影響を受けない）。
使い方：python3 client_build.py <サイトのフォルダ> <書き出し先フォルダ>
"""
import os, re, sys, shutil, posixpath

SRC_PAGE = "pattern2/index.html"


def build(site, out):
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    html = open(os.path.join(site, SRC_PAGE), encoding="utf-8").read()

    # デモ用の部品を外す
    html = re.sub(r'<div class="p2-bar">.*?</div></div>\s*', "", html, flags=re.S)
    html = re.sub(r'<div class="mode-bar".*?</div>\s*', "", html, flags=re.S)
    html = re.sub(r"<!--\s*デザインデモ.*?-->\s*", "", html, flags=re.S)
    html = re.sub(r"<span>DESIGN DEMO[^<]*</span>", "", html)
    html = html.replace('class="mode-review"', 'class="mode-public"', 1)
    html = re.sub(r"<title>[^<]*</title>", "<title>株式会社久留米興業｜TOPページ デザイン案</title>", html, count=1)

    # リンクを無効に（a要素は残し、飛び先だけを外す）
    def kill(m):
        tag = m.group(0)
        if 'class="skip-link"' in tag:
            return tag  # ページ内の「本文へ移動」は残す
        tag = re.sub(r'\s(?:href|target|rel)="[^"]*"', "", tag)
        return tag[:-1] + ' aria-disabled="true">'
    html = re.sub(r"<a\b[^>]*>", kill, html)
    html = html.replace('<span class="sr-only">（外部サイトが開きます）</span>', "")
    html = html.replace('<span class="sr-only">（お問い合わせフォームが別画面で開きます）</span>', "")
    html = html.replace("</head>", '<style>/* 送付用：リンクは無効 */a[aria-disabled="true"]{cursor:default}</style>\n</head>', 1)

    # 参照している素材を集め、パスを assets/ 直下に付け替える
    base = posixpath.dirname(SRC_PAGE)
    files = set()

    def collect(url, frm):
        if re.match(r"^(?:[a-z]+:|#|//)", url) or not url:
            return None
        p = posixpath.normpath(posixpath.join(frm, url.split("#")[0].split("?")[0]))
        if os.path.isfile(os.path.join(site, p)):
            files.add(p)
            return p
        return None

    def rel(m):
        p = collect(m.group(2), base)
        return m.group(1) + (posixpath.relpath(p, "") if p else m.group(2)) + m.group(3)
    html = re.sub(r'(\b(?:href|src)=")([^"]*)(")', rel, html)
    html = re.sub(r"(url\(['\"]?)([^'\")]+)(['\"]?\))", rel, html)

    # CSSの中の素材（フォント・背景画像）
    for p in sorted(f for f in files if f.endswith(".css")):
        css = open(os.path.join(site, p), encoding="utf-8").read()
        for u in re.findall(r"url\(['\"]?([^'\")]+)['\"]?\)", css):
            collect(u, posixpath.dirname(p))

    for p in sorted(files):
        dst = os.path.join(out, p)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy(os.path.join(site, p), dst)

    # 送付用は常に公開イメージで表示（確認用の注記を出さない）
    sj = os.path.join(out, "assets/site.js")
    if os.path.exists(sj):
        s = open(sj, encoding="utf-8").read()
        s = s.replace("setMode(saved==='public'?'public':'review');", "setMode('public'); /* 送付用：常に公開イメージ */")
        open(sj, "w", encoding="utf-8").write(s)

    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)
    return sorted(files)


if __name__ == "__main__":
    fs = build(sys.argv[1], sys.argv[2])
    print(len(fs), "files")

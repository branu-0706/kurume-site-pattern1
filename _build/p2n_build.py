# -*- coding: utf-8 -*-
"""パターン②の派生デザイン（B・C）を作る。
ベース（/pattern2/ 以下の6ページ）を /pattern2/design-b/・/pattern2/design-c/ に写し、
・相対パスを写し先から見た形に直す（パターン②内のリンクは写し先の同じページへ）
・data-design を p2-b / p2-c に、CSS に p2-b.css / p2-c.css を足す
HTMLの中身は同じ（＝内容・順番は同じで、見た目だけが違う）。"""
import os, re, posixpath

DESIGNS = [("design-b", "B", "EDITORIAL", "p2-b"), ("design-c", "C", "CINEMA", "p2-c")]
PAGES = ["index.html", "about/index.html", "recruit/index.html", "people/index.html", "future/index.html", "company/index.html"]
ATTR = re.compile(r'(\b(?:href|src)=")([^"]*)(")')
CSSURL = re.compile(r"(url\(['\"]?)([^'\")]+)(['\"]?\))")  # style属性の背景画像も写し先から見たパスに


def _map(url, src_dir, dst_dir, key):
    if not url or re.match(r'^(?:[a-z]+:|#|//)', url):
        return url
    path, sep, frag = url.partition("#")
    if not path:
        return url
    absu = posixpath.normpath(posixpath.join(src_dir, path))
    if absu.startswith("pattern2/") and not absu.startswith("pattern2/design-"):
        absu = "pattern2/" + key + "/" + absu[len("pattern2/"):]
    elif absu == "pattern2":
        absu = "pattern2/" + key
    rel = posixpath.relpath(absu, dst_dir)
    if path.endswith("/") and not rel.endswith("/"):
        rel += "/"
    return rel + (sep + frag if sep else "")


NAMES = [("", "A", "NAVY CURVE"), ("design-b", "B", "EDITORIAL"), ("design-c", "C", "CINEMA")]
BAR_RE = re.compile(r'<div class="p2-bar">.*?</div></div>', re.S)


def bar(cur_key, page, dst_dir):
    """デモ用の切替バー（パターン②のA・B・C、比較ページ）。CMS移植時は削除する。"""
    links = []
    for key, letter, name in NAMES:
        target = "pattern2/" + (key + "/" if key else "") + page
        cur = ' aria-current="page"' if key == cur_key else ""
        links.append(f'<a href="{posixpath.relpath(target, dst_dir)}"{cur}>{letter}｜{name}</a>')
    hub = posixpath.relpath("compare/index.html", dst_dir)
    return f'<div class="p2-bar"><div class="wrap"><b>パターン②（ビジョン → 採用）</b>{"".join(links)}<a href="{hub}">比較ページ</a></div></div>'


def build(out):
    for key, letter, name, dkey in DESIGNS:
        for page in PAGES:
            src_rel = "pattern2/" + page
            dst_rel = "pattern2/" + key + "/" + page
            html = open(os.path.join(out, src_rel), encoding="utf-8").read()
            sd, dd = posixpath.dirname(src_rel), posixpath.dirname(dst_rel)
            html = ATTR.sub(lambda m: m.group(1) + _map(m.group(2), sd, dd, key) + m.group(3), html)
            html = CSSURL.sub(lambda m: m.group(1) + _map(m.group(2), sd, dd, key) + m.group(3), html)
            html = html.replace('data-design="p2-a"', f'data-design="{dkey}"', 1)
            css = posixpath.relpath("assets/n/" + dkey + ".css", dd)
            html = html.replace('/assets/n/p2.css">', f'/assets/n/p2.css">\n<link rel="stylesheet" href="{css}">', 1)
            html = html.replace("<title>", f"<title>パターン② {letter}｜", 1)
            html = BAR_RE.sub(lambda m: bar(key, page, dd), html, count=1)
            fp = os.path.join(out, dst_rel)
            os.makedirs(os.path.dirname(fp), exist_ok=True)
            open(fp, "w", encoding="utf-8").write(html)

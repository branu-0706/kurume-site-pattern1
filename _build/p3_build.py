# -*- coding: utf-8 -*-
"""第3パターン（写真の色を活かす）：TOP 3デザイン。
出力：pattern3/design-a|b|c/index.html。CSS：assets/p3/base.css ＋ a.css|b.css|c.css。
・写真はすべてカラーのまま（フィルタ・暗幕なし）。文字は写真の外の無地の面に置く。
・CMSのsectionで作れる構成（721 / 16 / 54 / 42 / 22 / 80）。ボタン・リンクはファーストビューに置かない。"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
if not os.path.isdir(OUT):
    OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
P = "../../assets/photos/"

DESIGNS = [
    ("design-a", "A", "CROSS SECTION", "ベース：白い地に紺の面、道路の断面図と大きな角丸の写真"),
    ("design-b", "B", "ASPHALT", "派生：アスファルトの黒を地に、路面の白線と重機の黄"),
    ("design-c", "C", "STRATA", "派生：地層の縞を全面に。生成りの紙と地層の色"),
]
F4 = [("ガス管取替後の復旧舗装工事", "ガス管の取替後に行う道路の舗装復旧工事。", "paving-roller", "ローラーで舗装を締め固める現場"),
      ("水道工事", "水道管の布設・布設替など、給水インフラに関わる工事。", "water-pipe", "水道管の工事現場"),
      ("一般土木工事", "道路の改良・維持など、公共空間の基盤に関わる工事。", "civil-road", "道路の土木工事"),
      ("下水道工事", "下水道の整備など、生活環境を支える工事。", "work-kyuden", "工事を終えた道路")]
H1 = '<span class="ln">道路の復旧舗装から、</span><br><span class="ln">水道・土木工事まで。</span>'
LEAD = "世田谷を拠点に、1974年から。道路と街のインフラに関わる工事を担っています。"
NAV = "".join(f"<span>{t}</span>" for t in ["TOP", "事業内容", "採用情報", "労働環境", "働くメンバー", "会社情報"])


def bar(cur):
    links = "".join(f'<a href="../{k}/"{" aria-current=\"page\"" if k == cur else ""}>{l}｜{n}</a>' for k, l, n, _ in DESIGNS)
    return f'''<div class="p3-bar"><div class="wrap"><b>第3パターン（写真の色を活かす）</b>{links}<a href="../../">パターン①（手描き）と比べる</a><a href="../../compare/">比較ページ</a></div></div>'''


def head(key, title):
    return f'''<!doctype html>
<html lang="ja" data-structure="p3" data-design="{key}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>{title}｜株式会社久留米興業</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@500;600;700&family=Noto+Sans+JP:wght@400;500;700;900&display=swap">
<link rel="stylesheet" href="../../assets/theme.css">
<link rel="stylesheet" href="../../assets/fonts/dela-gothic.css">
<link rel="stylesheet" href="../../assets/p3/base.css">
<link rel="stylesheet" href="../../assets/p3/{key[-1]}.css">
<script src="../../assets/theme/presets.js"></script>
<script src="../../assets/theme/theme.js" defer></script>
</head>
<body>
{bar(key)}
<header class="hd"><div class="wrap"><img src="../../assets/kurume-logo.png" alt="久留米興業 ロゴ" width="70" height="44"><p class="wm">KURUME KOGYO<span>株式会社久留米興業</span></p><nav aria-label="メインナビゲーション（見本）">{NAV}</nav><span class="ct">お問い合わせ</span></div></header>
<main>
'''


FOOT_MAIN = '''
<!-- CONTACT｜CMS 80 H2 Text ＋ ボタン -->
<section class="p3-contact"><div class="wrap"><div><p class="kicker">CONTACT</p><h2 class="h2">工事のご相談・お問い合わせ</h2><p>道路舗装・水道・土木工事のご相談は、お電話またはお問い合わせフォームから。</p></div><div class="p3-cta"><a class="p3-btn" href="https://www.kurume-k.jp/contact" target="_blank" rel="noopener noreferrer">お問い合わせフォーム</a><p class="tel">TEL <a href="tel:0333093786">03-3309-3786</a></p></div></div></section>
'''


def biz_cards():
    return "".join(f'<figure class="biz-item"><img src="{P}{im}.jpg" alt="{alt}" loading="lazy" width="1600" height="1066"><figcaption><small>{i+1:02d}</small><h3>{t}</h3><p>{d}</p></figcaption></figure>' for i, (t, d, im, alt) in enumerate(F4))


def mv_a():
    return f'''
<!-- 01 MAIN VISUAL｜CMS 721（写真1枚・カラーのまま。文字は写真の下の白い面） -->
<section class="mv" aria-labelledby="h1" data-cms-id="721">
  <figure class="mv-photo"><img src="{P}field-work-street.jpg" alt="重機とともに歩道の路盤をつくる施工中の現場" width="1600" height="1066" fetchpriority="high"></figure>
  <div class="mv-copy wrap"><div><p class="kicker">INFRASTRUCTURE / KURUME KOGYO</p><h1 id="h1">{H1}</h1></div><div><p class="p3-lead">{LEAD}</p><ul class="mv-fields" aria-label="対応する工事">{"".join(f"<li>{t}</li>" for t,*_ in F4)}</ul></div></div>
</section>
'''


def sig_a():
    return f'''
<!-- A の見せ場｜CMS 54 Half（全幅の写真＋白い面の文字） -->
<section class="full" aria-labelledby="onsite-title"><img src="{P}machine.jpg" alt="社名の入った重機" loading="lazy" width="1600" height="1066"><div class="full-copy"><p class="kicker">ON SITE</p><h2 class="h2" id="onsite-title">社名を背負って、<br>街の道路に出ていく。</h2><p>北烏山の資材置き場から、重機と資材を積んで各現場へ。</p></div></section>
'''


def mv_b():
    return f'''
<!-- 01 MAIN VISUAL｜CMS 734（見出し）＋ 721（写真3枚をグリッドで。合成しない） -->
<section class="mv" aria-labelledby="h1" data-cms-id="734,721">
  <div class="wrap mv-head"><p class="kicker">INFRASTRUCTURE / KURUME KOGYO</p><h1 id="h1">{H1}</h1><p class="p3-lead">{LEAD}</p></div>
  <div class="wrap mv-grid">
    <figure class="g1"><img src="{P}field-work-street.jpg" alt="重機とともに歩道の路盤をつくる施工中の現場" width="1600" height="1066" fetchpriority="high"><figcaption>歩道の路盤工事</figcaption></figure>
    <figure class="g2"><img src="{P}yard-low-krm.jpg" alt="重機が並ぶ北烏山の資材置き場" width="1600" height="1066"><figcaption>北烏山の資材置き場</figcaption></figure>
    <figure class="g3"><img src="{P}loader-wheel.jpg" alt="資材置き場の重機のタイヤ" width="1600" height="1066"><figcaption>資材置き場</figcaption></figure>
  </div>
  <ul class="wrap mv-fields" aria-label="対応する工事">{"".join(f"<li><span>{i+1:02d}</span>{t}</li>" for i,(t,*_) in enumerate(F4))}</ul>
</section>
'''


def sig_b():
    return f'''
<!-- B の見せ場｜CMS 42 Card Three（写真のみ・大小） -->
<section class="sec soft" aria-labelledby="scenes-title"><div class="wrap"><div class="head"><p class="kicker">SCENES</p><h2 class="h2" id="scenes-title">現場の、<br>ある一日。</h2><p>資材置き場で重機を準備し、現場へ。古い舗装を剥がし、新しい道に仕上げるまで。</p></div>
  <div class="scenes"><figure class="s1"><img src="{P}machine.jpg" alt="社名の入った重機" loading="lazy" width="1600" height="1066"><figcaption>朝、重機を積んで現場へ</figcaption></figure><figure class="s2"><img src="{P}operator-lever.jpg" alt="作業着の袖で重機のレバーを握る手元" loading="lazy" width="1600" height="1066"><figcaption>重機を操作して作業開始</figcaption></figure><figure class="s3"><img src="{P}yard-machines.jpg" alt="資材置き場に並ぶ重機と運搬車" loading="lazy" width="1600" height="1066"><figcaption>資材置き場で重機と車両を準備</figcaption></figure><figure class="s4"><img src="{P}asphalt-rubble.jpg" alt="剥がした古いアスファルトの塊" loading="lazy" width="1600" height="1066"><figcaption>古い舗装を剥がして、新しい道へ</figcaption></figure></div>
</div></section>
'''


def mv_c():
    return f'''
<!-- 01 MAIN VISUAL｜CMS 721（写真1枚）＋ 734（重機の黄色の面に見出し） -->
<section class="mv" aria-labelledby="h1" data-cms-id="721,734">
  <div class="mv-panel"><p class="kicker">INFRASTRUCTURE / KURUME KOGYO</p><h1 id="h1">{H1}</h1><p class="p3-lead">{LEAD}</p></div>
  <figure class="mv-photo"><img src="{P}field-work-street.jpg" alt="重機とともに歩道の路盤をつくる施工中の現場" width="1600" height="1066" fetchpriority="high"></figure>
  <ul class="mv-fields" aria-label="対応する工事">{"".join(f"<li><span>{i+1:02d}</span>{t}</li>" for i,(t,*_) in enumerate(F4))}</ul>
</section>
'''


def sig_c():
    return f'''
<!-- C の見せ場｜CMS 42 Card Three（写真＋その写真の色の面） -->
<section class="sec navy" aria-labelledby="colors-title"><div class="wrap"><div class="head"><p class="kicker">COLORS OF THE SITE</p><h2 class="h2" id="colors-title">現場の色が、<br>この会社の色。</h2><p>重機の黄色、作業着の紺、舗装の黒。毎日の現場にある色を、そのまま会社の色にしています。</p></div>
  <div class="swatches">
    <figure class="sw y"><img src="{P}loader-wheel.jpg" alt="資材置き場の重機のタイヤ" loading="lazy" width="1600" height="1066"><figcaption><b>MACHINE YELLOW</b>重機の黄色</figcaption></figure>
    <figure class="sw n"><img src="{P}operator-lever.jpg" alt="作業着の袖で重機のレバーを握る手元" loading="lazy" width="1600" height="1066"><figcaption><b>WORK NAVY</b>作業着の紺</figcaption></figure>
    <figure class="sw k"><img src="{P}asphalt-rubble.jpg" alt="剥がした古いアスファルトの塊" loading="lazy" width="1600" height="1066"><figcaption><b>ASPHALT BLACK</b>舗装の黒</figcaption></figure>
  </div></div></section>
'''


import re as _re

PAGES = ["business", "recruit", "work-environment", "people", "company"]


def _rewrite(html, base):
    """P1の出力HTMLを pattern3/design-x/ 配下へ移すためのパス書き換え。base は元の相対接頭辞（"" か "../"）。"""
    keep = ("index.html", "#", "http", "tel:", "mailto:") + tuple(p + "/" for p in PAGES)
    def fix(m):
        attr, val = m.group(1), m.group(2)
        if not val.startswith(base):
            return m.group(0)
        rest = val[len(base):]
        if rest.startswith(keep):
            return m.group(0)
        return attr + base + "../../" + rest
    html = _re.sub(r'((?:href|src)=")([^"]*)', fix, html)
    html = _re.sub(r"(url\(')([^']*)", fix, html)
    return html


def _strip(html, key):
    for pat in [r'\n<link rel="stylesheet" href="[^"]*(?:ink|marker|dela-gothic|switcher)\.css">', r'\n<script defer src="[^"]*switcher\.js"></script>']:
        html = _re.sub(pat, "", html)
    html = _re.sub(r'data-design="d1"', f'data-design="p3-{key[-1]}"', html, count=1)
    html = html.replace('data-structure="p1"', 'data-structure="p1" data-pattern="p3"', 1)
    return html


def _add_css(html, root, files):
    """新デザイン（2026-11-09〜）：英字フォント＋ assets/n/ のCSS＋動き（n.js）"""
    links = f'\n<link rel="stylesheet" href="{root}assets/fonts/display-en.css">' + "".join(f'\n<link rel="stylesheet" href="{root}assets/n/{f}">' for f in files)
    html = html.replace('/office.css">', '/office.css">' + links, 1)
    return html.replace("</head>", f'<script defer src="{root}assets/n/n.js"></script>\n</head>', 1)


def _bar(html, key, root):
    return html.replace("<body>", "<body>\n" + bar(key).replace('href="../', f'href="{root}pattern3/').replace(f'href="{root}pattern3/../', f'href="{root}'), 1)


def build(out=OUT):
    import p3n_top
    for key, letter, name, desc in DESIGNS:
        d = os.path.join(out, "pattern3", key)
        os.makedirs(d, exist_ok=True)
        css = ["p3.css"] + ([f"p3-{key[-1]}.css"] if key != "design-a" else [])
        # TOP：パターン①のTOPの枠（ヘッダー・フッター）に、新しい本文（①②のミックス）を入れる
        src = open(os.path.join(out, "index.html"), encoding="utf-8").read()
        html = _strip(_rewrite(src, ""), key)
        html, n = _re.subn(r'<main id="main">.*?</main>', lambda m: '<main id="main">' + p3n_top.body() + '</main>', html, count=1, flags=_re.S)
        assert n == 1
        html = html.replace('<title>', f'<title>第3パターン {letter}｜', 1)
        html = _add_css(html, "../../", css)
        html = _bar(html, key, "../../")
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
        # 下層：P1 の下層ページを、新デザインのCSSで
        for p in PAGES:
            src = open(os.path.join(out, p, "index.html"), encoding="utf-8").read()
            html = _strip(_rewrite(src, "../"), key)
            html = _add_css(html, "../../../", css)
            html = _bar(html, key, "../../../")
            os.makedirs(os.path.join(d, p), exist_ok=True)
            open(os.path.join(d, p, "index.html"), "w", encoding="utf-8").write(html)


if __name__ == "__main__":
    build()
    print("pattern3 built")

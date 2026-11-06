# 比較用TOP（デザイン②・③）の共通パーツ。
# 置き場所：/compare/pattern{1,2}/design-{a,b}/index.html（リポジトリ直下から3階層）。
# CSSはデザインごとに独立（assets/compare/p1-d2.css など）。JSはパターン①と同じ site.js（ヘッダー・メニュー・表示切替・控えめな出現）を流用。
from common import OFFICIAL_CONTACT, ext
from common import PAGES as P1_PAGES
from p2common import P2_PAGES, switcher_tags

ROOT = "../../../"
DESIGN_NAME = {"d2": "DESIGN 02", "d3": "DESIGN 03"}
VARIANT = {("p1", "d2"): "OFFICIAL STANDARD", ("p1", "d3"): "INFRASTRUCTURE CANVAS", ("p2", "d2"): "HUMAN ATLAS", ("p2", "d3"): "KEEP / CHANGE"}


def nav_items(structure):
    """D2/D3はTOPのみ。下層は同じ構成パターンのデザイン①へリンクする。"""
    if structure == "p1":
        items = [(l, "index.html" if k == "top" else ROOT + p) for k, l, p in P1_PAGES]
    else:
        items = [(l, "index.html" if k == "top" else ROOT + "pattern2/" + p) for k, l, p in P2_PAGES]
    return items


def head(structure, design, title, desc):
    return f'''<!doctype html>
<html lang="ja" class="mode-review" data-structure="{structure}" data-design="{design}" data-page="top">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#1A2259">
<meta name="robots" content="noindex">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@500;600;700&family=Noto+Sans+JP:wght@400;500;700;800;900&display=swap">
<link rel="stylesheet" href="{ROOT}assets/theme.css">
<link rel="stylesheet" href="{ROOT}assets/compare/base.css">
<link rel="stylesheet" href="{ROOT}assets/compare/{structure}-{design}.css">
<script defer src="{ROOT}assets/site.js"></script>
{switcher_tags(ROOT)}</head>
<body>
<!-- 比較用TOP（{structure.upper()} × {DESIGN_NAME[design]}）。下層ページは同じ構成パターンのデザイン①へリンクします。 -->
<a class="skip-link" href="#main">本文へ移動</a>
'''


def header(structure, cta_label, cta_href):
    cur = ' aria-current="page"'
    navs = "".join(f'<a href="{h}"{cur if h == "index.html" else ""}>{l}</a>' for l, h in nav_items(structure))
    return f'''<header class="c-header" id="site-header">
  <div class="c-header-inner">
    <a class="c-brand" href="index.html" aria-label="久留米興業 トップへ"><img src="{ROOT}assets/kurume-logo.png" alt="久留米興業 ロゴ" width="64" height="40"><span>KURUME KOGYO<small>株式会社久留米興業</small></span></a>
    <nav class="c-nav" aria-label="メインナビゲーション">{navs}</nav>
    <a class="c-header-cta" href="{cta_href}"{' target="_blank" rel="noopener noreferrer"' if cta_href.startswith('http') else ''}>{cta_label}{' ↗<span class="sr-only">（外部サイトが開きます）</span>' if cta_href.startswith('http') else ''}</a>
    <button class="c-menu" id="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="メニューを開く"><span></span><span></span><span></span></button>
  </div>
  <nav class="c-mobile-nav" id="mobile-nav" aria-label="モバイルナビゲーション" hidden>{navs}<a href="{cta_href}">{cta_label}</a></nav>
</header>
'''


def footer(structure, design):
    links = "".join(f'<a href="{h}">{l}</a>' for l, h in nav_items(structure))
    label = f"DESIGN DEMO / PATTERN 0{structure[1]} · {DESIGN_NAME[design]} {VARIANT[(structure, design)]}"
    return f'''<footer class="c-footer">
  <div class="c-wrap c-footer-top">
    <div class="c-footer-brand"><img src="{ROOT}assets/kurume-logo.png" alt="久留米興業 ロゴ" width="64" height="40"><div><strong>株式会社久留米興業</strong><p>〒157-0061 東京都世田谷区北烏山6丁目26-28<br>TEL 03-3309-3786</p></div></div>
    <nav class="c-footer-links" aria-label="フッターナビゲーション">{links}<a href="{OFFICIAL_CONTACT}" target="_blank" rel="noopener noreferrer">お問い合わせ ↗<span class="sr-only">（外部サイトが開きます）</span></a></nav>
  </div>
  <div class="c-wrap c-footer-bottom"><span>© KURUME KOGYO CO., LTD.</span><span>{label}</span><a href="#main">BACK TO TOP ↑</a></div>
</footer>
<div class="mode-bar" role="group" aria-label="デモの表示切替"><span class="mb-label">DESIGN DEMO</span><button type="button" data-mode="review" aria-pressed="true">確認用</button><button type="button" data-mode="public" aria-pressed="false">公開イメージ</button></div>
</body>
</html>
'''


def page(structure, design, title, desc, body, cta_label, cta_href):
    html = head(structure, design, title, desc) + header(structure, cta_label, cta_href)
    html += '<main id="main">\n' + body + '\n</main>\n' + footer(structure, design)
    return html.replace("@R@", ROOT).replace("@P1@", ROOT).replace("@P2@", ROOT + "pattern2/")

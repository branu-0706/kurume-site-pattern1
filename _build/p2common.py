# パターン②（ビジョン共感 → 採用）の共通パーツ。2026-11-09〜：参考 GTN 採用サイト。手描き（ink.css）は使わず、assets/n/p2.css で作る。
# パターン①の site.css / site.js をそのまま使い、差分は assets/p2.css（[data-structure="p2"] にスコープ）に置く。
# @R@ はサイトのルート（リポジトリ直下）までの相対パス、@P2@ はパターン②TOPまでの相対パスに置換する。
from common import (demo_tags, OFFICIAL_CONTACT, OFFICIAL_NEWS, OFFICIAL_WORKS, OFFICIAL_RECRUIT, SALES_JOB, KRM, DISASTER, MAPS,
                    BLOG_NEGISHI, BLOG_TAKAHATA, BLOG_IMAI, BLOG_LIST, ext)

P2_PAGES = [
    ("top", "TOP", "index.html"),
    ("about", "私たちについて", "about/index.html"),
    ("recruit", "採用情報", "recruit/index.html"),
    ("people", "社員紹介", "people/index.html"),
    ("future", "これからの久留米興業", "future/index.html"),
    ("company", "会社情報", "company/index.html"),
]


def switcher_tags(root):
    """デモ専用の部品（配色の試し変更・比較切替）。CMS移植時は削除する。"""
    return demo_tags(root)


def p2_head(title, desc, root, page):
    return f'''<!doctype html>
<html lang="ja" class="mode-review" data-structure="p2" data-pattern="p2" data-design="p2-a" data-page="{page}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#1A2259">
<meta name="robots" content="noindex">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@500;600;700&family=Noto+Sans+JP:wght@400;500;700;800&display=swap">
<link rel="stylesheet" href="{root}assets/theme.css">
<link rel="stylesheet" href="{root}assets/site.css">
<link rel="stylesheet" href="{root}assets/p2.css">
<link rel="stylesheet" href="{root}assets/office.css">
<link rel="stylesheet" href="{root}assets/fonts/display-en.css">
<link rel="stylesheet" href="{root}assets/n/p2.css">
<script defer src="{root}assets/site.js"></script>
<script defer src="{root}assets/n/n.js"></script>
</head>
<body>
<!-- デザインデモ（パターン② × デザイン①）。CMS移植前の静的プロトタイプであり、本番公開物ではありません。 -->
<a class="skip-link" href="#main">本文へ移動</a>
'''


def p2_header(current, p2root):
    nav = []
    for key, label, path in P2_PAGES:
        cur = ' aria-current="page"' if key == current else ""
        nav.append(f'<a href="{p2root}{path}"{cur}>{label}</a>')
    navs = "".join(nav)
    return f'''<header class="site-header p2-header" id="site-header">
  <div class="header-inner wrap">
    <a class="site-brand" href="{p2root}index.html" aria-label="久留米興業 トップへ">
      <img src="@R@assets/kurume-logo.png" alt="久留米興業 ロゴ" width="72" height="45">
      <span class="brand-wordmark">KURUME KOGYO<span>株式会社久留米興業</span></span>
    </a>
    <nav class="desktop-nav" aria-label="メインナビゲーション">{navs}</nav>
    <a class="header-contact" href="{OFFICIAL_CONTACT}" target="_blank" rel="noopener noreferrer">お問い合わせ <span aria-hidden="true">↗</span><span class="sr-only">（外部サイトが開きます）</span></a>
    <button class="menu-toggle" id="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="メニューを開く"><span></span><span></span><span></span></button>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="モバイルナビゲーション" hidden>{navs}<a href="{OFFICIAL_CONTACT}" target="_blank" rel="noopener noreferrer">お問い合わせ ↗</a></nav>
</header>
'''


def p2_breadcrumb(label, p2root):
    return f'''<nav class="breadcrumb" aria-label="パンくずリスト"><ol class="wrap"><li><a href="{p2root}index.html">TOP</a></li><li aria-current="page">{label}</li></ol></nav>
'''


def p2_footer(p2root):
    links = "".join(f'<a href="{p2root}{p}">{l}</a>' for _, l, p in P2_PAGES)
    return f'''<footer class="site-footer" id="top-footer-info">
  <div class="wrap footer-top">
    <div class="footer-brand"><img src="@R@assets/kurume-logo.png" alt="久留米興業 ロゴ" width="75" height="47"><div><strong>株式会社久留米興業</strong><p>〒157-0061 東京都世田谷区北烏山6丁目26-28<br>TEL 03-3309-3786</p></div></div>
    <nav class="footer-links" aria-label="フッターナビゲーション">{links}<a href="{OFFICIAL_CONTACT}" target="_blank" rel="noopener noreferrer">お問い合わせ ↗</a></nav>
  </div>
  <div class="wrap footer-bottom"><span>© KURUME KOGYO CO., LTD.</span><span>DESIGN DEMO / PATTERN 02 · DESIGN 01</span><a href="#main">BACK TO TOP ↑</a></div>
</footer>
<div class="mode-bar" role="group" aria-label="デモの表示切替"><span class="mb-label">DESIGN DEMO</span><button type="button" data-mode="review" aria-pressed="true">確認用</button><button type="button" data-mode="public" aria-pressed="false">公開イメージ</button></div>
</body>
</html>
'''


def p2_page(current, title, desc, depth, body, crumb=None):
    """depth: リポジトリ直下からの深さ（/pattern2/ は1、/pattern2/about/ は2）"""
    root = "../" * depth
    p2root = "../" * (depth - 1)
    import p2n_build
    page = dict((k, pth) for k, _, pth in P2_PAGES)[current]
    out = p2_head(title, desc, root, current).replace("<body>", "<body>\n" + p2n_build.bar("", page, "pattern2/" + page.rsplit("/", 1)[0] if "/" in page else "pattern2"), 1) + p2_header(current, p2root)
    out += '<main id="main">\n'
    if crumb:
        body = body.replace("<!--CRUMB-->", "")  # パンくずは表示しない（2026-11-09）
    body = body.replace('<div class="page-hero-img"', '<span class="lane" aria-hidden="true"></span><div class="page-hero-img"')
    out += body + "\n</main>\n" + p2_footer(p2root)
    return out.replace("@R@", root).replace("@P2@", p2root)


def gate_text(label):
    return f'data-gate="{label}"'

# 共通パーツ（ヘッダー・フッター・head）。@R@ はサイトのルートまでの相対パスに置換する。
OFFICIAL_CONTACT = "https://www.kurume-k.jp/contact"
OFFICIAL_NEWS = "https://www.kurume-k.jp/news"
OFFICIAL_WORKS = "https://www.kurume-k.jp/achievement"
OFFICIAL_RECRUIT = "https://www.kurume-k.jp/recruit"
SALES_JOB = "https://recruit.careecon.jp/co/kurume-k/jobs/01KHJ5MKWZVXFZE8M584EPP84R"
KRM = "https://www.krm-setagaya.jp/"
DISASTER = "https://www.kurume-k.jp/452874803881/6"
MAPS = "https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E4%B8%96%E7%94%B0%E8%B0%B7%E5%8C%BA%E5%8C%97%E7%83%8F%E5%B1%B16%E4%B8%81%E7%9B%AE26-28"

PAGES = [
    ("top", "TOP", "index.html"),
    ("business", "事業内容", "business/index.html"),
    ("recruit", "採用情報", "recruit/index.html"),
    ("environment", "労働環境", "work-environment/index.html"),
    ("people", "働くメンバー", "people/index.html"),
    ("company", "会社情報", "company/index.html"),
]
HREF = {k: p for k, _, p in PAGES}


def ext(url, text, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{url}" target="_blank" rel="noopener noreferrer">{text}<span class="sr-only">（外部サイトが開きます）</span></a>'


def demo_tags(root):
    """デモ専用の部品（配色の試し変更・構成×デザインの比較切替）。CMS移植時はこの4行を削除する。"""
    return (f'<script src="{root}assets/theme/presets.js"></script>\n'
            f'<script src="{root}assets/theme/theme.js"></script>\n'
            f'<link rel="stylesheet" href="{root}assets/compare/switcher.css">\n'
            f'<script defer src="{root}assets/compare/switcher.js"></script>\n')


def head(title, desc, root, current="top"):
    return f'''<!doctype html>
<html lang="ja" class="mode-review" data-structure="p1" data-design="d1" data-page="{current}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#1A2259">
<meta name="robots" content="noindex">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@500;600;700&family=Barlow+Condensed:wght@600;700&family=Noto+Sans+JP:wght@400;500;700;800&display=swap">
<link rel="stylesheet" href="{root}assets/theme.css">
<link rel="stylesheet" href="{root}assets/site.css">
<link rel="stylesheet" href="{root}assets/office.css">
<link rel="stylesheet" href="{root}assets/hero.css">
<script defer src="{root}assets/site.js"></script>
{demo_tags(root)}</head>
<body>
<!-- デザインデモ（パターン① × デザイン①）。CMS移植前の静的プロトタイプであり、本番公開物ではありません。 -->
<a class="skip-link" href="#main">本文へ移動</a>
'''


def header(current, root):
    nav = []
    for key, label, path in PAGES:
        cur = ' aria-current="page"' if key == current else ""
        nav.append(f'<a href="{root}{path}"{cur}>{label}</a>')
    navs = "".join(nav)
    return f'''<header class="site-header" id="site-header">
  <div class="header-inner wrap">
    <a class="site-brand" href="{root}index.html" aria-label="久留米興業 トップへ">
      <img src="{root}assets/kurume-logo.png" alt="久留米興業 ロゴ" width="72" height="45">
      <span class="brand-wordmark">KURUME KOGYO<span>株式会社久留米興業</span></span>
    </a>
    <nav class="desktop-nav" aria-label="メインナビゲーション">{navs}</nav>
    <a class="header-contact" href="{OFFICIAL_CONTACT}" target="_blank" rel="noopener noreferrer">お問い合わせ <span aria-hidden="true">↗</span><span class="sr-only">（お問い合わせフォームが別画面で開きます）</span></a>
    <button class="menu-toggle" id="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="メニューを開く"><span></span><span></span><span></span></button>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="モバイルナビゲーション" hidden>{navs}<a href="{OFFICIAL_CONTACT}" target="_blank" rel="noopener noreferrer">お問い合わせ ↗</a></nav>
</header>
'''


def breadcrumb(label, root):
    return f'''<nav class="breadcrumb" aria-label="パンくずリスト"><ol class="wrap"><li><a href="{root}index.html">TOP</a></li><li aria-current="page">{label}</li></ol></nav>
'''


def footer(root):
    links = "".join(f'<a href="{root}{p}">{l}</a>' for _, l, p in PAGES)
    return f'''<footer class="site-footer">
  <div class="wrap footer-top">
    <div class="footer-brand"><img src="{root}assets/kurume-logo.png" alt="久留米興業 ロゴ" width="75" height="47"><div><strong>株式会社久留米興業</strong><p>〒157-0061 東京都世田谷区北烏山6丁目26-28<br>TEL 03-3309-3786</p></div></div>
    <nav class="footer-links" aria-label="フッターナビゲーション">{links}<a href="{OFFICIAL_CONTACT}" target="_blank" rel="noopener noreferrer">お問い合わせ ↗</a></nav>
  </div>
  <div class="wrap footer-bottom"><span>© KURUME KOGYO CO., LTD.</span><span>DESIGN DEMO / PATTERN 01 · DESIGN 01</span><a href="#main">BACK TO TOP ↑</a></div>
</footer>
<div class="mode-bar" role="group" aria-label="デモの表示切替"><span class="mb-label">DESIGN DEMO</span><button type="button" data-mode="review" aria-pressed="true">確認用</button><button type="button" data-mode="public" aria-pressed="false">公開イメージ</button></div>
</body>
</html>
'''


def page(current, title, desc, depth, body, crumb=None):
    root = "../" * depth
    out = head(title, desc, root, current) + header(current, root)
    out += '<main id="main">\n'
    if crumb:
        # パンくずはHEROの直後に置く（HEROを最初の視覚要素にするため）
        body = body.replace("<!--CRUMB-->", breadcrumb(crumb, root))
    marks = {"business-hero": "BUSINESS", "recruit-hero": "RECRUIT", "environment-hero": "WORK STYLE", "people-hero": "PEOPLE", "company-hero": "COMPANY"}
    for hid, word in marks.items():
        body = body.replace(f'class="page-hero" id="{hid}"', f'class="page-hero" id="{hid}" data-mark="{word}"')
    body = body.replace('<div class="page-hero-img"', '<span class="lane" aria-hidden="true"></span><div class="page-hero-img"')
    out += body.replace("@R@", root) + "\n</main>\n" + footer(root)
    return out

# 採用ブログ（CAREECON）のインタビュー記事
BLOG_NEGISHI = "https://recruit.careecon.jp/co/kurume-k/blogs/214004"
BLOG_TAKAHATA = "https://recruit.careecon.jp/co/kurume-k/blogs/214003"
BLOG_IMAI = "https://recruit.careecon.jp/co/kurume-k/blogs/214001"
BLOG_LIST = "https://recruit.careecon.jp/co/kurume-k/blogs"

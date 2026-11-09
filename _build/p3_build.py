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
    ("design-a", "A", "PHOTO FULL", "写真を全面に。余白は白、文字は最小限"),
    ("design-b", "B", "GALLERY", "白い誌面に、写真を大小のグリッドで"),
    ("design-c", "C", "SITE COLOR", "現場の色（重機の黄・コーンの橙・作業着の紺）を拾う"),
]
F4 = [("ガス管取替後の復旧舗装工事", "ガス管の取替後に行う道路の舗装復旧工事。", "paving-roller", "ローラーで舗装を締め固める現場"),
      ("水道工事", "水道管の布設・布設替など、給水インフラに関わる工事。", "water-pipe", "水道管の工事現場"),
      ("一般土木工事", "道路の改良・維持など、公共空間の基盤に関わる工事。", "civil-road", "道路の土木工事"),
      ("下水道工事", "下水道の整備など、生活環境を支える工事。", "process-remove", "舗装を撤去する作業")]
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


FOOT = '''
<!-- CONTACT｜CMS 80 H2 Text ＋ ボタン -->
<section class="p3-contact"><div class="wrap"><div><p class="kicker">CONTACT</p><h2 class="h2">工事のご相談・お問い合わせ</h2><p>道路舗装・水道・土木工事のご相談は、お電話またはお問い合わせフォームから。</p></div><div class="p3-cta"><a class="btn" href="../../company/index.html#company-contact">お問い合わせフォーム</a><p class="tel">TEL <a href="tel:0333093786">03-3309-3786</a></p></div></div></section>
</main>
<footer class="ft"><div class="wrap"><img src="../../assets/kurume-logo.png" alt="" width="56" height="35"><p>株式会社久留米興業　東京都世田谷区北烏山6丁目26-28</p></div></footer>
</body></html>
'''


def biz_cards():
    return "".join(f'<figure class="biz-item"><img src="{P}{im}.jpg" alt="{alt}" loading="lazy" width="1600" height="1066"><figcaption><small>{i+1:02d}</small><h3>{t}</h3><p>{d}</p></figcaption></figure>' for i, (t, d, im, alt) in enumerate(F4))


def page_a():
    return f'''
<!-- 01 MAIN VISUAL｜CMS 721（写真1枚・カラーのまま。文字は写真の下の白い面） -->
<section class="mv" aria-labelledby="h1" data-cms-id="721">
  <figure class="mv-photo"><img src="{P}field-work-street.jpg" alt="重機とともに歩道の路盤をつくる施工中の現場" width="1600" height="1066" fetchpriority="high"></figure>
  <div class="mv-copy wrap"><div><p class="kicker">INFRASTRUCTURE / KURUME KOGYO</p><h1 id="h1">{H1}</h1></div><div><p class="lead">{LEAD}</p><ul class="mv-fields" aria-label="対応する工事">{"".join(f"<li>{t}</li>" for t,*_ in F4)}</ul></div></div>
</section>
<!-- 02 BUSINESS｜CMS 16 Card Four -->
<section class="sec"><div class="wrap"><div class="head"><p class="kicker">BUSINESS</p><h2 class="h2">対応する工事</h2></div><div class="biz">{biz_cards()}</div></div></section>
<!-- 03 ON SITE｜CMS 54 Half（全幅の写真＋白い面の文字） -->
<section class="full"><img src="{P}excavator-boom-name.jpg" alt="社名の入った重機と資材置き場" loading="lazy" width="1600" height="1066"><div class="full-copy"><p class="kicker">ON SITE</p><h2 class="h2">社名を背負って、<br>街の道路に出ていく。</h2><p>北烏山の資材置き場から、重機と資材を積んで各現場へ。</p></div></section>
<!-- 04 OFFICE｜CMS 54 Half -->
<section class="sec"><div class="wrap half"><img src="{P}office-wide-window.jpg" alt="窓際まで机が並ぶ本社の事務所" loading="lazy" width="1600" height="1066"><div><p class="kicker">OFFICE</p><h2 class="h2">現場を動かす、<br>北烏山の本社。</h2><p>取引先との調整、見積、書類、工程。現場が予定どおり進むように、本社の社員が支えています。</p></div></div></section>
<!-- 05 RECRUIT｜CMS 54 Half -->
<section class="sec soft"><div class="wrap half is-rev"><img src="{P}compactor-shovel.jpg" alt="締固め機とスコップで路盤を整える二人の現場職" loading="lazy" width="1600" height="1066"><div><p class="kicker">RECRUIT</p><h2 class="h2">未経験から、<br>道路の仕事へ。</h2><p>営業職・現場職ともに、未経験から始めた社員が活躍しています。</p><a class="more" href="../../recruit/index.html">採用情報を見る</a></div></div></section>
'''


def page_b():
    return f'''
<!-- 01 MAIN VISUAL｜CMS 734（見出し）＋ 721（写真3枚をグリッドで。合成しない） -->
<section class="mv" aria-labelledby="h1" data-cms-id="734,721">
  <div class="wrap mv-head"><p class="kicker">INFRASTRUCTURE / KURUME KOGYO</p><h1 id="h1">{H1}</h1><p class="lead">{LEAD}</p></div>
  <div class="wrap mv-grid">
    <figure class="g1"><img src="{P}field-work-street.jpg" alt="重機とともに歩道の路盤をつくる施工中の現場" width="1600" height="1066" fetchpriority="high"><figcaption>歩道の路盤工事</figcaption></figure>
    <figure class="g2"><img src="{P}office-wide-window.jpg" alt="窓際まで机が並ぶ本社の事務所" width="1600" height="1066"><figcaption>北烏山の本社</figcaption></figure>
    <figure class="g3"><img src="{P}loader-wheel.jpg" alt="資材置き場の重機のタイヤ" width="1600" height="1066"><figcaption>資材置き場</figcaption></figure>
  </div>
  <ul class="wrap mv-fields" aria-label="対応する工事">{"".join(f"<li><span>{i+1:02d}</span>{t}</li>" for i,(t,*_) in enumerate(F4))}</ul>
</section>
<!-- 02 BUSINESS｜CMS 16 Card Four（2×2） -->
<section class="sec"><div class="wrap"><div class="head"><p class="kicker">BUSINESS</p><h2 class="h2">対応する工事</h2><p>ガス管取替後の道路復旧から、水道・土木・下水道工事まで。</p></div><div class="biz">{biz_cards()}</div></div></section>
<!-- 03 SCENES｜CMS 42 Card Three（写真のみ・大小） -->
<section class="sec soft"><div class="wrap"><div class="head"><p class="kicker">SCENES</p><h2 class="h2">現場と本社の、<br>ある一日。</h2></div>
  <div class="scenes"><figure class="s1"><img src="{P}excavator-boom-name.jpg" alt="社名の入った重機と資材置き場" loading="lazy" width="1600" height="1066"><figcaption>朝、重機を積んで現場へ</figcaption></figure><figure class="s2"><img src="{P}traffic-guard.jpg" alt="道路で誘導する警備員" loading="lazy" width="1600" height="1066"><figcaption>安全を確保して作業開始</figcaption></figure><figure class="s3"><img src="{P}office-team-wide.jpg" alt="社員が机を並べて働く本社の事務所" loading="lazy" width="1600" height="1066"><figcaption>本社で見積と段取り</figcaption></figure><figure class="s4"><img src="{P}compactor-shovel.jpg" alt="締固め機とスコップで路盤を整える二人の現場職" loading="lazy" width="1600" height="1066"><figcaption>路盤を整え、道を元に戻す</figcaption></figure></div>
</div></section>
<!-- 04 COMPANY｜CMS 22 Table -->
<section class="sec"><div class="wrap half"><div><p class="kicker">COMPANY</p><h2 class="h2">1974年から、<br>この街の道路と。</h2><dl class="facts"><div><dt>設立</dt><dd>1974年3月4日</dd></div><div><dt>所在地</dt><dd>東京都世田谷区北烏山6丁目26-28</dd></div><div><dt>関連会社</dt><dd>KRM株式会社</dd></div></dl><a class="more" href="../../company/index.html">会社情報を見る</a></div><img src="{P}yard-gate.jpg" alt="「(株)久留米興業」の看板を掲げた資材置き場の入口" loading="lazy" width="1600" height="1066"></div></section>
'''


def page_c():
    return f'''
<!-- 01 MAIN VISUAL｜CMS 721（写真1枚）＋ 734（重機の黄色の面に見出し） -->
<section class="mv" aria-labelledby="h1" data-cms-id="721,734">
  <div class="mv-panel"><p class="kicker">INFRASTRUCTURE / KURUME KOGYO</p><h1 id="h1">{H1}</h1><p class="lead">{LEAD}</p></div>
  <figure class="mv-photo"><img src="{P}field-work-street.jpg" alt="重機とともに歩道の路盤をつくる施工中の現場" width="1600" height="1066" fetchpriority="high"></figure>
  <ul class="mv-fields" aria-label="対応する工事">{"".join(f"<li><span>{i+1:02d}</span>{t}</li>" for i,(t,*_) in enumerate(F4))}</ul>
</section>
<!-- 02 BUSINESS｜CMS 16 Card Four（写真の下に色の帯） -->
<section class="sec"><div class="wrap"><div class="head"><p class="kicker">BUSINESS</p><h2 class="h2">対応する工事</h2></div><div class="biz">{biz_cards()}</div></div></section>
<!-- 03 COLORS OF THE SITE｜CMS 42 Card Three（写真＋その写真の色の面） -->
<section class="sec navy"><div class="wrap"><div class="head"><p class="kicker">COLORS OF THE SITE</p><h2 class="h2">現場の色が、<br>この会社の色。</h2><p>重機の黄色、コーンの橙、作業着の紺。毎日の現場にある色を、そのまま会社の色にしています。</p></div>
  <div class="swatches">
    <figure class="sw y"><img src="{P}loader-wheel.jpg" alt="資材置き場の重機のタイヤ" loading="lazy" width="1600" height="1066"><figcaption><b>MACHINE YELLOW</b>重機の黄色</figcaption></figure>
    <figure class="sw o"><img src="{P}traffic-guard.jpg" alt="道路で誘導する警備員" loading="lazy" width="1600" height="1066"><figcaption><b>SAFETY ORANGE</b>安全の橙</figcaption></figure>
    <figure class="sw n"><img src="{P}worker-back-towel.jpg" alt="ヘルメット姿で作業する現場職の後ろ姿" loading="lazy" width="1600" height="1066"><figcaption><b>WORK NAVY</b>作業着の紺</figcaption></figure>
  </div></div></section>
<!-- 04 OFFICE｜CMS 54 Half -->
<section class="sec"><div class="wrap half"><img src="{P}office-wide-window.jpg" alt="窓際まで机が並ぶ本社の事務所" loading="lazy" width="1600" height="1066"><div><p class="kicker">OFFICE</p><h2 class="h2">ライムの椅子が並ぶ、<br>北烏山の本社。</h2><p>取引先との調整、見積、書類、工程。現場が予定どおり進むように、本社の社員が支えています。</p><a class="more" href="../../company/index.html">会社情報を見る</a></div></div></section>
'''


def build(out=OUT):
    for (key, letter, name, desc), body in zip(DESIGNS, [page_a, page_b, page_c]):
        d = os.path.join(out, "pattern3", key)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(head(key, f"第3パターン {letter} {name}") + body() + FOOT)


if __name__ == "__main__":
    build()
    print("pattern3 built")

# パターン① × デザイン③｜FIELD ENERGY（現場の迫力・非対称パネル）
# フル幅の写真HERO、巨大な見出し、交互に並ぶ番号付きの事業、紺の大面積、写真モザイク。
# 動き：セクション境界のライン描画0.55s、写真のclip reveal 0.6s、CTAの矢印が最大6px移動。
from cmp_common import page
from cmp_copy import P1 as C, PH, br, a


def head(no, label, ja, light=False):
    cls = "d3-head is-light" if light else "d3-head"
    return f'<div class="{cls}"><span class="d3-line" aria-hidden="true"></span><p><span class="d3-no">{no:02d}</span>{label}<span class="d3-ja">{ja}</span></p></div>'


def build():
    h, ab, bz, va, wk, ws, pp, rc, nw, cl = (C[k] for k in ["hero", "about", "business", "values", "works", "workstyle", "people", "recruit", "news", "close"])
    rows = []
    for i, (t, d, img, alt, href) in enumerate(bz["items"]):
        media = (f'<div class="d3-biz-photo d3-clip"><img src="{PH}{img}" alt="{alt}" loading="lazy"></div>' if img
                 else '<div class="d3-biz-photo is-text" aria-hidden="true"><span>SEWERAGE</span></div>')
        rows.append(f'<a class="d3-biz-row{" is-rev" if i % 2 else ""} reveal" href="{href}"><span class="d3-biz-no">{i+1:02d}</span><div class="d3-biz-text"><h3>{t}</h3><p>{d}</p><span class="d3-arrow">詳しく見る <b aria-hidden="true">→</b></span></div>{media}</a>')
    works = wk["items"]
    vitems = "".join(f'<li><span>{i+1:02d}</span><div><strong>{t}</strong><p>{d}</p></div></li>' for i, (t, d) in enumerate(va["items"]))
    people = "".join(f'<a class="d3-person reveal" href="{href}" data-delay="{i}"><div class="d3-person-img d3-clip"><img src="{PH}{img}" alt="{alt}" loading="lazy"></div><div class="d3-person-body"><small>{en}</small><h3>{ja}</h3><p>{d}</p><span class="d3-arrow"><b aria-hidden="true">→</b></span></div></a>' for i, (ja, en, d, img, alt, href) in enumerate(pp["items"]))
    recruit = "".join(f'<a class="d3-role" href="{cta[1]}"><img src="{PH}{img}" alt="{alt}" loading="lazy"><div class="d3-role-band"><small>{en}</small><h3>{ja}</h3><p>{d}</p><span class="d3-role-cta">{cta[0]} <b aria-hidden="true">→</b></span></div></a>' for ja, en, d, img, alt, cta in rc["items"])
    news = "".join(f'<li><a href="{url}" target="_blank" rel="noopener noreferrer"><time datetime="{iso}">{date}</time><span>{t}</span><b aria-hidden="true">↗</b><span class="sr-only">（外部サイトが開きます）</span></a></li>' for iso, date, cat, t, url in nw["items"])
    ws_role = ws["roles"][1]

    body = f'''
<!-- 01 HERO #top-hero｜方式C：独自HTML＋CSS（写真が主役の全幅HERO、左上に巨大H1）。CMS ID参考：721/734 -->
<section class="d3-hero" id="top-hero" aria-labelledby="hero-title" data-cms-id="721,734" data-implementation="C">
  <img class="d3-hero-img" src="{PH}{h["img"][0]}" alt="{h["img"][1]}" width="941" height="627">
  <div class="d3-hero-shade" aria-hidden="true"></div>
  <div class="c-wrap d3-hero-inner">
    <p class="d3-hero-label">{h["label"]} <span>SINCE 1974</span></p>
    <h1 id="hero-title"><span>{h["h1"][0]}</span><span>{h["h1"][1]}</span></h1>
    <p class="d3-hero-lead">{h["lead"]}</p>
    <div class="d3-actions">{a(h["cta"][0][0], h["cta"][0][1], "d3-btn is-white")}{a(h["cta"][1][0], h["cta"][1][1], "d3-btn is-line")}</div>
  </div>
  <p class="d3-hero-deco" aria-hidden="true">INFRASTRUCTURE / PEOPLE</p>
</section>

<!-- 02 ABOUT #top-about｜方式B：CMS 54 Half ＋ CSS（1974と社屋写真・白いプレートの段差配置） -->
<section class="d3-section d3-about" id="top-about" aria-labelledby="about-title" data-cms-id="54" data-implementation="B">
  <div class="c-wrap">
    {head(2, ab["label"], ab["ja"])}
    <div class="d3-about-grid">
      <p class="d3-year" aria-hidden="true">1974</p>
      <div class="d3-about-photo d3-clip reveal"><img src="{PH}{ab["img"][0]}" alt="{ab["img"][1]}" loading="lazy"></div>
      <div class="d3-plate reveal"><h2 id="about-title">{br(ab["h2"])}</h2>{"".join(f"<p>{p}</p>" for p in ab["body"])}{a(ab["cta"][0], ab["cta"][1], "d3-text-link")}</div>
    </div>
  </div>
</section>

<!-- 03 BUSINESS #top-business｜方式B：CMS 16 Card Four ＋ scoped CSS（大番号と写真帯が交互に並ぶ） -->
<section class="d3-section d3-business" id="top-business" aria-labelledby="biz-title" data-cms-id="16" data-implementation="B">
  <div class="c-wrap">
    {head(3, bz["label"], bz["ja"])}
    <div class="d3-title-row"><h2 id="biz-title">{br(bz["h2"])}</h2><p>{bz["lead"]}</p></div>
    <div class="d3-biz">{"".join(rows)}</div>
    <div class="d3-end">{a(bz["cta"][0], bz["cta"][1], "d3-btn is-navy")}</div>
  </div>
</section>

<!-- 04 VALUES #top-values｜方式B：CMS 80 H2 Text ＋ 54 Half（紺の大面積、左端にブルーの進行ライン） -->
<section class="d3-values" id="top-values" aria-labelledby="values-title" data-cms-id="80,54" data-implementation="B">
  <div class="c-wrap d3-values-grid">
    <div class="d3-values-copy reveal">
      {head(4, va["label"], va["ja"], light=True)}
      <h2 id="values-title">{br(va["h2"])}</h2>
      <p>{va["lead"]}</p>
      <ul class="d3-values-list">{vitems}</ul>
      {a(va["cta"][0], va["cta"][1], "d3-text-link is-light")}
    </div>
    <div class="d3-values-photo d3-clip reveal"><img src="{PH}{va["img"][0]}" alt="{va["img"][1]}" loading="lazy"></div>
  </div>
</section>

<!-- 05 WORKS #top-works｜方式A/B：CMS 718 Portfolio（大1＋小2のモザイク） -->
<section class="d3-section" id="top-works" aria-labelledby="works-title" data-cms-id="718" data-implementation="A/B">
  <div class="c-wrap">
    {head(5, wk["label"], wk["ja"])}
    <div class="d3-title-row"><h2 id="works-title">{br(wk["h2"])}</h2><p>{wk["lead"]}</p></div>
    <div class="d3-mosaic reveal">
      <figure class="is-main"><img src="{PH}{works[0][0]}" alt="{works[0][1]}" loading="lazy"></figure>
      <figure><img src="{PH}{works[1][0]}" alt="{works[1][1]}" loading="lazy"></figure>
      <figure><img src="{PH}{works[2][0]}" alt="{works[2][1]}" loading="lazy"></figure>
    </div>
    <div class="d3-end">{a(wk["cta"][0], wk["cta"][1], "d3-btn is-navy")}<a class="d3-text-link" href="@P1@business/index.html">工事内容を知る <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<!-- 06 WORK STYLE #top-workstyle｜方式B：CMS 54 Half（左に現場写真、右に紺パネル） -->
<section class="d3-workstyle" id="top-workstyle" aria-labelledby="ws-title" data-cms-id="54" data-implementation="B">
  <div class="d3-ws-photo d3-clip"><img src="{PH}{ws_role[2]}" alt="{ws_role[3]}" loading="lazy"></div>
  <div class="d3-ws-panel reveal">
    {head(6, ws["label"], ws["ja"], light=True)}
    <h2 id="ws-title">{br(ws["h2"])}</h2>
    {"".join(f"<p>{p}</p>" for p in ws["body"])}
    <dl class="d3-ws-roles">{"".join(f"<div><dt>{t}</dt><dd>{d}</dd></div>" for t, d, _, _ in ws["roles"])}</dl>
    {a(ws["cta"][0], ws["cta"][1], "d3-btn is-white")}
  </div>
</section>

<!-- 07 PEOPLE #top-people｜方式B：CMS 42 Card Three（段差カード＋大きな背景文字） -->
<section class="d3-section d3-people-sec" id="top-people" aria-labelledby="people-title" data-cms-id="42" data-implementation="B">
  <p class="d3-bgword" aria-hidden="true">PEOPLE</p>
  <div class="c-wrap">
    {head(7, pp["label"], pp["ja"])}
    <div class="d3-title-row"><h2 id="people-title">{br(pp["h2"])}</h2><p>{pp["lead"]}</p></div>
    <div class="d3-people">{people}</div>
    <div class="d3-end">{a(pp["cta"][0], pp["cta"][1], "d3-btn is-navy")}</div>
  </div>
</section>

<!-- 08 RECRUIT #top-recruit｜方式B：CMS 787 Two Text ＋ 90（左右に分けた写真パネル） -->
<section class="d3-recruit" id="top-recruit" aria-labelledby="recruit-title" data-cms-id="787,90" data-implementation="B">
  <div class="c-wrap d3-recruit-head">{head(8, rc["label"], rc["ja"], light=True)}<h2 id="recruit-title">{br(rc["h2"])}</h2><p>{rc["lead"]}</p></div>
  <div class="d3-roles">{recruit}</div>
  <div class="c-wrap d3-end is-light">{a(rc["cta"][0], rc["cta"][1], "d3-btn is-white")}</div>
</section>

<!-- 09 NEWS #top-news｜方式A：CMS 101 Blog Standard（紺の見出しバー＋実在記事） -->
<section class="d3-section" id="top-news" aria-labelledby="news-title" data-cms-id="101" data-implementation="A">
  <div class="c-wrap">
    <div class="d3-newsbar"><h2 id="news-title">NEWS<span>{br(nw["h2"])}</span></h2>{a(nw["cta"][0], nw["cta"][1], "d3-text-link is-light")}</div>
    <ul class="d3-news">{news}</ul>
  </div>
</section>

<!-- 10 LEARN MORE #top-contact｜方式B：CMS 90 Btn Text ＋ 23 Btn（フル幅ネイビーの締め） -->
<section class="d3-close" id="top-contact" aria-labelledby="close-title" data-cms-id="90,23" data-implementation="B">
  <div class="c-wrap">
    <h2 id="close-title">{cl["h2"][0]}</h2>
    <p>{cl["lead"]}</p>
    <div class="d3-close-actions">{a(cl["cta"][0][0], cl["cta"][0][1], "d3-btn is-white")}{a(cl["cta"][1][0], cl["cta"][1][1], "d3-btn is-line")}</div>
    {a(cl["sub"][0], cl["sub"][1], "d3-sublink")}
  </div>
</section>
'''
    body = body.replace(' d3-clip reveal"', ' d3-clip"').replace(' d3-clip"', ' d3-clip reveal"')
    body = body.replace('class="d3-head', 'class="reveal d3-head')
    return page("p1", "d3", "株式会社久留米興業｜街を支える仕事を、働く人の未来につなげる。（比較用TOP：パターン①×デザイン③）",
                "パターン①（会社理解重視）×デザイン③（現場の迫力・表現重視）の比較用TOP。",
                body, "採用情報", "../../../recruit/index.html")

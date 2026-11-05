# パターン① × デザイン②｜CLEAR STRUCTURE（ミニマル・インフォメーション）
# 白場・直線・番号付き見出し・整列。影と角丸なし、動きはopacityのみ。
from cmp_common import page
from cmp_copy import P1 as C, PH, br, a


def kicker(no, label, ja):
    return f'<p class="d2-kicker"><span class="d2-no">{no:02d}</span><span class="d2-en">{label}</span><span class="d2-ja">{ja}</span></p>'


def build():
    h, ab, bz, va, wk, ws, pp, rc, nw, cl = (C[k] for k in ["hero", "about", "business", "values", "works", "workstyle", "people", "recruit", "news", "close"])
    biz_rows = "".join(
        f'<li><a class="d2-row" href="{href}"><span class="d2-row-no">{i+1:02d}</span><span class="d2-row-main"><strong>{t}</strong><span>{d}</span></span>'
        + (f'<span class="d2-row-thumb"><img src="{PH}{img}" alt="{alt}" loading="lazy"></span>' if img else '<span class="d2-row-thumb is-empty" aria-hidden="true"></span>')
        + '<span class="d2-row-arrow" aria-hidden="true">→</span></a></li>'
        for i, (t, d, img, alt, href) in enumerate(bz["items"]))
    works = "".join(f'<figure class="d2-work"><img src="{PH}{img}" alt="{alt}" loading="lazy"><figcaption>{wk["item_label"]}</figcaption></figure>' for img, alt in wk["items"])
    roles = "".join(f'<div class="d2-summary"><img src="{PH}{img}" alt="{alt}" loading="lazy"><div><h3>{t}</h3><p>{d}</p></div></div>' for t, d, img, alt in ws["roles"])
    people = "".join(f'<a class="d2-person" href="{href}"><span class="d2-person-img"><img src="{PH}{img}" alt="{alt}" loading="lazy"></span><small>{en}</small><strong>{ja}</strong><span>{d}</span></a>' for ja, en, d, img, alt, href in pp["items"])
    recruit = "".join(f'<div class="d2-role"><img src="{PH}{img}" alt="{alt}" loading="lazy"><small>{en}</small><h3>{ja}</h3><p>{d}</p>{a(cta[0], cta[1], "d2-link")}</div>' for ja, en, d, img, alt, cta in rc["items"])
    news = "".join(f'<li><a href="{url}" target="_blank" rel="noopener noreferrer"><time datetime="{iso}">{date}</time><span class="d2-cat">{cat}</span><span class="d2-title">{t}</span><span aria-hidden="true">↗</span><span class="sr-only">（外部サイトが開きます）</span></a></li>' for iso, date, cat, t, url in nw["items"])
    values = "".join(f'<li><strong>{t}</strong><span>{d}</span></li>' for t, d in va["items"])

    body = f'''
<!-- 01 HERO #top-hero｜方式B/C：CMS 734/721。文字と写真を重ねない左右分割 -->
<section class="d2-hero" id="top-hero" aria-labelledby="hero-title" data-cms-id="734,721" data-implementation="B/C">
  <div class="c-wrap d2-grid">
    <div class="d2-hero-copy d2-fade">
      <p class="d2-hero-label">{h["label"]}</p>
      <h1 id="hero-title">{br(h["h1"])}</h1>
      <p class="d2-hero-lead">{h["lead"]}</p>
      <div class="d2-actions">{a(h["cta"][0][0], h["cta"][0][1], "d2-btn is-primary")}{a(h["cta"][1][0], h["cta"][1][1], "d2-btn")}</div>
    </div>
    <figure class="d2-hero-photo d2-fade"><img src="{PH}{h["img"][0]}" alt="{h["img"][1]}" width="941" height="627"><figcaption>{h["caption"]}</figcaption></figure>
  </div>
  <div class="c-wrap"><hr class="d2-rule"></div>
</section>

<!-- 02 ABOUT #top-about｜方式B：CMS 54 Half（写真は本文下の横長1枚） -->
<section class="d2-section" id="top-about" aria-labelledby="about-title" data-cms-id="54" data-implementation="B">
  <div class="c-wrap d2-grid reveal">
    <div class="d2-side">{kicker(2, ab["label"], ab["ja"])}<dl class="d2-since"><div><dt>SINCE</dt><dd>1974</dd></div><div><dt>YEARS</dt><dd>50+</dd></div></dl></div>
    <div class="d2-main">
      <h2 id="about-title">{br(ab["h2"])}</h2>
      {"".join(f"<p>{p}</p>" for p in ab["body"])}
      {a(ab["cta"][0], ab["cta"][1], "d2-link")}
      <figure class="d2-wide"><img src="{PH}{ab["img"][0]}" alt="{ab["img"][1]}" loading="lazy"></figure>
    </div>
  </div>
</section>

<!-- 03 BUSINESS #top-business｜方式B：CMS 16 Card FourをCSSでフラットな番号リストに -->
<section class="d2-section is-gray" id="top-business" aria-labelledby="biz-title" data-cms-id="16" data-implementation="B">
  <div class="c-wrap d2-grid reveal">
    <div class="d2-side">{kicker(3, bz["label"], bz["ja"])}</div>
    <div class="d2-main">
      <h2 id="biz-title">{br(bz["h2"])}</h2>
      <p>{bz["lead"]}</p>
      <ol class="d2-rows">{biz_rows}</ol>
      {a(bz["cta"][0], bz["cta"][1], "d2-link")}
    </div>
  </div>
  <p class="review-note c-wrap">下水道工事は、該当する写真が届くまでサムネイルを空けています。</p>
</section>

<!-- 04 VALUES #top-values｜方式B：CMS 80 H2 Text ＋ 54 Half（中央の一文＋写真1点） -->
<section class="d2-section" id="top-values" aria-labelledby="values-title" data-cms-id="80,54" data-implementation="B">
  <div class="c-wrap d2-grid reveal">
    <div class="d2-side">{kicker(4, va["label"], va["ja"])}</div>
    <div class="d2-values">
      <div><h2 id="values-title" class="d2-statement">{br(va["h2"])}</h2><p>{va["lead"]}</p><ul class="d2-list">{values}</ul>{a(va["cta"][0], va["cta"][1], "d2-link")}</div>
      <figure><img src="{PH}{va["img"][0]}" alt="{va["img"][1]}" loading="lazy"></figure>
    </div>
  </div>
</section>

<!-- 05 WORKS #top-works｜方式A/B：CMS 718 Portfolio（比率を揃えた3枚） -->
<section class="d2-section is-gray" id="top-works" aria-labelledby="works-title" data-cms-id="718" data-implementation="A/B">
  <div class="c-wrap d2-grid reveal">
    <div class="d2-side">{kicker(5, wk["label"], wk["ja"])}</div>
    <div class="d2-main"><h2 id="works-title">{br(wk["h2"])}</h2><p>{wk["lead"]}</p></div>
  </div>
  <div class="c-wrap"><div class="d2-works reveal">{works}</div><div class="d2-right">{a(wk["cta"][0], wk["cta"][1], "d2-link")}</div></div>
</section>

<!-- 06 WORK STYLE #top-workstyle｜方式B：CMS 54 Half ＋ 787 Two Text -->
<section class="d2-section" id="top-workstyle" aria-labelledby="ws-title" data-cms-id="54,787" data-implementation="B">
  <div class="c-wrap d2-grid reveal">
    <div class="d2-side">{kicker(6, ws["label"], ws["ja"])}</div>
    <div class="d2-main d2-split">
      <div><h2 id="ws-title">{br(ws["h2"])}</h2>{"".join(f"<p>{p}</p>" for p in ws["body"])}{a(ws["cta"][0], ws["cta"][1], "d2-link")}</div>
      <div class="d2-summaries">{roles}</div>
    </div>
  </div>
</section>

<!-- 07 PEOPLE #top-people｜方式B：CMS 42 Card Three -->
<section class="d2-section is-gray" id="top-people" aria-labelledby="people-title" data-cms-id="42" data-implementation="B">
  <div class="c-wrap d2-grid reveal">
    <div class="d2-side">{kicker(7, pp["label"], pp["ja"])}</div>
    <div class="d2-main"><h2 id="people-title">{br(pp["h2"])}</h2><p>{pp["lead"]}</p></div>
  </div>
  <div class="c-wrap"><div class="d2-people reveal">{people}</div><div class="d2-right">{a(pp["cta"][0], pp["cta"][1], "d2-link")}</div></div>
</section>

<!-- 08 RECRUIT #top-recruit｜方式B：CMS 787 Two Text ＋ 90 Btn Text（職種比較を同じ位置に） -->
<section class="d2-section" id="top-recruit" aria-labelledby="recruit-title" data-cms-id="787,90" data-implementation="B">
  <div class="c-wrap d2-grid reveal">
    <div class="d2-side">{kicker(8, rc["label"], rc["ja"])}</div>
    <div class="d2-main"><h2 id="recruit-title">{br(rc["h2"])}</h2><p>{rc["lead"]}</p></div>
  </div>
  <div class="c-wrap"><div class="d2-roles reveal">{recruit}</div><div class="d2-center">{a(rc["cta"][0], rc["cta"][1], "d2-btn is-primary")}</div></div>
</section>

<!-- 09 NEWS #top-news｜方式A：CMS 101 Blog Standard（実在記事のみ） -->
<section class="d2-section is-gray" id="top-news" aria-labelledby="news-title" data-cms-id="101" data-implementation="A">
  <div class="c-wrap d2-grid reveal">
    <div class="d2-side">{kicker(9, nw["label"], nw["ja"])}</div>
    <div class="d2-main"><h2 id="news-title">{br(nw["h2"])}</h2><p>{nw["lead"]}</p><ul class="d2-news">{news}</ul>{a(nw["cta"][0], nw["cta"][1], "d2-link")}</div>
  </div>
</section>

<!-- 10 LEARN MORE #top-contact｜方式B：CMS 90 Btn Text ＋ 23 Btn（細い紺帯） -->
<section class="d2-close" id="top-contact" aria-labelledby="close-title" data-cms-id="90,23" data-implementation="B">
  <div class="c-wrap d2-close-inner">
    <div><h2 id="close-title">{br(cl["h2"])}</h2><p>{cl["lead"]}</p></div>
    <div class="d2-close-actions">{a(cl["cta"][0][0], cl["cta"][0][1], "d2-btn is-white")}{a(cl["cta"][1][0], cl["cta"][1][1], "d2-btn is-line")}{a(cl["sub"][0], cl["sub"][1], "d2-sublink")}</div>
  </div>
</section>
'''
    return page("p1", "d2", "株式会社久留米興業｜街を支える仕事を、働く人の未来につなげる。（比較用TOP：パターン①×デザイン②）",
                "パターン①（会社理解重視）×デザイン②（ミニマル・インフォメーション）の比較用TOP。",
                body, "採用情報", "../../../recruit/index.html")

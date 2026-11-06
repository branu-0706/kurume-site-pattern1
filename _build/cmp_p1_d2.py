# 構成① × デザイン②｜OFFICIAL STANDARD（公的・法人向けの信頼感）
# 厳格な12カラム（最大1200px）、直線と薄い罫線、表組み。角丸0〜4px。動きは0.2〜0.35sのフェードと罫線の変化だけ。
# 色は --kk-* のみ（HEX直書きなし）。
from cmp_common import page
from cmp_copy import P1 as C, PH, TEL, ADDRESS, br, a


def head(no, label, ja, h2, hid):
    return (f'<header class="os-head"><p class="os-label"><span class="os-no">{no:02d}</span><span>{label}</span><span class="os-ja">{ja}</span></p>'
            f'<h2 id="{hid}">{br(h2)}</h2></header>')


def build():
    h, ab, bz, ap, wk, ws, pp, rc, nw, ct = (C[k] for k in ["hero", "about", "business", "approach", "works", "workstyle", "people", "recruit", "news", "contact"])
    fields = "".join(f'<li><a href="{href}"><span>{i+1:02d}</span>{t}</a></li>' for i, (t, d, img, alt, href) in enumerate(bz["items"]))
    rows = "".join(
        f'<tr><td class="os-cell-no">{i+1:02d}</td><th scope="row"><a href="{href}">{t}</a></th><td>{d}</td>'
        + (f'<td class="os-cell-img"><img src="{PH}{img}" alt="{alt}" loading="lazy"></td>' if img else '<td class="os-cell-img"><span class="os-noimg">写真準備中</span></td>')
        + '</tr>' for i, (t, d, img, alt, href) in enumerate(bz["items"]))
    steps = "".join(f'<li><small>{en}</small><h3>{t}</h3><p>{d}</p></li>' for en, t, d in ap["steps"])
    works = "".join(f'<figure><img src="{PH}{img}" alt="{alt}" loading="lazy"><figcaption>{cap}</figcaption></figure>' for img, alt, cap in wk["items"])
    facts = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in ab["facts"])
    plinks = "".join(f'<li><a href="{href}"><small>{en}</small><strong>{ja}</strong><span>{d}</span></a></li>' for en, ja, d, href in pp["links"])
    roles = "".join(f'<a class="os-role" href="{href}"><small>{en}</small><strong>{ja}</strong><span>{d}</span></a>' for ja, en, d, img, alt, href in rc["roles"])
    news = "".join(f'<li><a href="{url}" target="_blank" rel="noopener noreferrer">' + (f'<time datetime="{iso}">{date}</time>' if iso else '<span class="os-nodate" aria-hidden="true"></span>') + f'<span class="os-cat">{cat}</span><span class="os-title">{t}</span><span aria-hidden="true">↗</span><span class="sr-only">（外部サイトが開きます）</span></a></li>' for iso, date, cat, t, url in nw["items"])

    body = f'''
<!-- 01 HERO #top-hero｜方式B/C：CMS 721/734。左45%に会社と工種、右55%に施工写真。写真に文字を重ねない -->
<section class="os-hero" id="top-hero" aria-labelledby="hero-title" data-cms-id="721,734" data-implementation="B/C">
  <div class="c-wrap os-grid">
    <div class="os-hero-copy os-fade">
      <p class="os-hero-label">{h["label"]}</p>
      <h1 id="hero-title">{br(h["h1"])}</h1>
      <p class="os-lead">{h["lead"]}</p>
      <div class="os-actions">{a(h["cta"][0][0], h["cta"][0][1], "os-btn is-primary")}{a(h["cta"][1][0], h["cta"][1][1], "os-btn")}</div>
    </div>
    <figure class="os-hero-photo os-fade"><img src="{PH}{h["img"][0]}" alt="{h["img"][1]}" width="941" height="627"><figcaption>{h["caption"]}</figcaption></figure>
  </div>
  <div class="c-wrap"><nav class="os-fields" aria-label="対応する工事（4分類）"><p>対応工事</p><ul>{fields}</ul></nav></div>
</section>

<!-- 02 ABOUT / PROFILE #top-about｜方式B：CMS 54 Half ＋ 43 Title All ＋ 22 Table -->
<section class="os-section" id="top-about" aria-labelledby="about-title" data-cms-id="54,43,22" data-implementation="B">
  <div class="c-wrap os-grid reveal">
    <div class="os-col-5">{head(2, ab["label"], ab["ja"], ab["h2"], "about-title")}<p class="os-body">{ab["body"]}</p>{a(ab["cta"][0], ab["cta"][1], "os-link")}</div>
    <figure class="os-col-7 os-photo"><img src="{PH}{ab["img"][0]}" alt="{ab["img"][1]}" loading="lazy"><figcaption>{ab["caption"]}</figcaption></figure>
  </div>
  <div class="c-wrap"><dl class="os-facts reveal">{facts}</dl></div>
</section>

<!-- 03 BUSINESS #top-business｜方式B：CMS 16 Card Four をフラットな表に（不可なら 54 Half ×4段） -->
<section class="os-section is-soft" id="top-business" aria-labelledby="biz-title" data-cms-id="16,54,43" data-implementation="B">
  <div class="c-wrap reveal">
    <div class="os-split">{head(3, bz["label"], bz["ja"], bz["h2"], "biz-title")}<p class="os-body">{bz["lead"]}</p></div>
    <div class="os-table-wrap"><table class="os-table"><caption class="sr-only">対応する工事（4分類）</caption><thead><tr><th scope="col">No.</th><th scope="col">工種</th><th scope="col">内容</th><th scope="col"><span class="sr-only">写真</span></th></tr></thead><tbody>{rows}</tbody></table></div>
    <div class="os-end">{a(bz["cta"][0], bz["cta"][1], "os-btn is-primary")}</div>
  </div>
  <p class="review-note c-wrap">下水道工事と確認できる写真が届くまで、写真欄は「写真準備中」にしています。未確認の対応範囲・資格・実績数は載せていません。</p>
</section>

<!-- 04 OUR APPROACH #top-process｜方式B：CMS 54 Half / 80 H2 Text（3つの立場の連携図。認証マークなどは置かない） -->
<section class="os-section" id="top-process" aria-labelledby="process-title" data-cms-id="54,80" data-implementation="B">
  <div class="c-wrap reveal">
    <div class="os-split">{head(4, ap["label"], ap["ja"], ap["h2"], "process-title")}<p class="os-body">{ap["lead"]}</p></div>
    <ol class="os-steps">{steps}</ol>
    <p class="os-note">{ap["note"]}</p>
    <div class="os-end is-left">{a(ap["cta"][0][0], ap["cta"][0][1], "os-btn")}{a(ap["cta"][1][0], ap["cta"][1][1], "os-link")}</div>
  </div>
</section>

<!-- 05 WORKS / PHOTO #top-works｜方式A/B：CMS 584 Photo Gallery / 718 Portfolio（同寸の長方形で整列） -->
<section class="os-section is-soft" id="top-works" aria-labelledby="works-title" data-cms-id="584,718" data-implementation="A/B">
  <div class="c-wrap reveal">
    <div class="os-split">{head(5, wk["label"], wk["ja"], wk["h2"], "works-title")}<p class="os-body">{wk["lead"]}</p></div>
    <div class="os-works">{works}</div>
    <div class="os-end">{a(wk["cta"][0][0], wk["cta"][0][1], "os-btn is-primary")}{a(wk["cta"][1][0], wk["cta"][1][1], "os-link")}</div>
  </div>
</section>

<!-- 06 WORK STYLE #top-workstyle｜方式B：CMS 54 Half / 787 Text Two（左に事務所、右に現場、間に短い本文） -->
<section class="os-section" id="top-workstyle" aria-labelledby="ws-title" data-cms-id="54,787" data-implementation="B">
  <div class="c-wrap reveal">
    <div class="os-trio">
      <figure><img src="{PH}{ws["office"][0]}" alt="{ws["office"][1]}" loading="lazy"><figcaption>{ws["office"][2]}</figcaption></figure>
      <div class="os-trio-copy">{head(6, ws["label"], ws["ja"], ws["h2"], "ws-title")}<p class="os-body">{ws["lead"]}</p>{a(ws["cta"][0], ws["cta"][1], "os-link")}</div>
      <figure><img src="{PH}{ws["field"][0]}" alt="{ws["field"][1]}" loading="lazy"><figcaption>{ws["field"][2]}</figcaption></figure>
    </div>
  </div>
</section>

<!-- 07 PEOPLE #top-people｜方式B：CMS 42 Card Three / 54 Half（社内の写真1枚＋役割ごとの入口） -->
<section class="os-section is-soft" id="top-people" aria-labelledby="people-title" data-cms-id="42,54" data-implementation="B">
  <div class="c-wrap os-grid reveal">
    <figure class="os-col-7 os-photo"><img src="{PH}{pp["img"][0]}" alt="{pp["img"][1]}" loading="lazy"></figure>
    <div class="os-col-5">{head(7, pp["label"], pp["ja"], pp["h2"], "people-title")}<p class="os-body">{pp["lead"]}</p><ul class="os-plinks">{plinks}</ul>{a(pp["cta"][0], pp["cta"][1], "os-btn is-primary")}</div>
  </div>
</section>

<!-- 08 RECRUIT #top-recruit｜方式B：CMS 787 Text Two / 42（薄いブルーグレーの水平帯。条件の数字はTOPに出さない） -->
<section class="os-section is-tight" id="top-recruit" aria-labelledby="recruit-title" data-cms-id="787,42" data-implementation="B">
  <div class="c-wrap"><div class="os-band reveal">
    <div>{head(8, rc["label"], rc["ja"], rc["h2"], "recruit-title")}<p class="os-body">{rc["lead"]}</p></div>
    <div class="os-roles">{roles}</div>
    {a(rc["cta"][0], rc["cta"][1], "os-btn is-primary")}
  </div></div>
</section>

<!-- 09 INFORMATION #top-news｜方式A：CMS 101 Blog Standard / 43（実在記事のテキスト索引。日付不明の記事は日付を出さない） -->
<section class="os-section" id="top-news" aria-labelledby="news-title" data-cms-id="101,43" data-implementation="A">
  <div class="c-wrap os-grid reveal">
    <div class="os-col-4">{head(9, nw["label"], nw["ja"], nw["h2"], "news-title")}<p class="os-body">{nw["lead"]}</p>{a(nw["cta"][0], nw["cta"][1], "os-link")}</div>
    <ul class="os-col-8 os-news">{news}</ul>
  </div>
</section>

<!-- 10 CONTACT / NEXT #top-contact｜方式B：CMS 23 Btn / 90 Btn Text / 43（左に法人、右に採用。フォームは新設しない） -->
<section class="os-section is-soft" id="top-contact" aria-labelledby="contact-title" data-cms-id="23,90,43" data-implementation="B">
  <div class="c-wrap reveal">
    <div class="os-split">{head(10, ct["label"], ct["ja"], ct["h2"], "contact-title")}<p class="os-body">{ct["lead"]}</p></div>
    <div class="os-contact">
      <div class="is-client"><p class="os-contact-for">法人・取引先の方</p><dl><div><dt>電話</dt><dd><a href="tel:0333093786">{TEL}</a></dd></div><div><dt>所在地</dt><dd>{ADDRESS}</dd></div></dl><div class="os-actions">{a(ct["client"][0][0], ct["client"][0][1], "os-btn is-primary")}{a(ct["client"][1][0], ct["client"][1][1], "os-link")}</div></div>
      <div class="is-recruit"><p class="os-contact-for">採用をご検討の方</p><p class="os-body">仕事内容、入社後の流れ、待遇・募集条件は採用情報のページでご案内しています。</p>{a(ct["recruit"][0], ct["recruit"][1], "os-btn")}</div>
    </div>
  </div>
</section>
'''
    return page("p1", "d2", "株式会社久留米興業｜道路の復旧舗装から、水道・土木工事まで（比較用TOP：構成①×デザイン② オフィシャル）",
                "構成①（会社理解）×デザイン②（OFFICIAL STANDARD：オフィシャル感強め）の比較用TOP。",
                body, "お問い合わせ", "https://www.kurume-k.jp/contact")

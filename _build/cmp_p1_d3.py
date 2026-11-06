# 構成① × デザイン③｜INFRASTRUCTURE CANVAS（表現力のあるコーポレート）
# 最大1320px、HEROとWORKSは画面全幅。実写の大小・縦横の対比、線と余白の平面構成（斜めは3度以内）。
# 動き：写真のクリップ表示0.55s、線の伸長0.45s、ホバーで写真1.03倍まで。色は --kk-* のみ。
from cmp_common import page
from cmp_copy import P1 as C, PH, TEL, ADDRESS, br, a


from cms_hero import top_hero

def label(no, en, ja):
    return f'<p class="ic-label reveal"><span class="ic-line" aria-hidden="true"></span><span class="ic-no">{no:02d}</span>{en}<span class="ic-ja">{ja}</span></p>'


def build():
    h, ab, bz, ap, wk, ws, pp, rc, nw, ct = (C[k] for k in ["hero", "about", "business", "approach", "works", "workstyle", "people", "recruit", "news", "contact"])
    band = "".join(f'<li><a href="{href}"><span>{i+1:02d}</span>{t}</a></li>' for i, (t, d, img, alt, href) in enumerate(bz["items"]))
    biz = "".join(
        f'<a class="ic-biz-card reveal" href="{href}">'
        + (f'<span class="ic-biz-photo ic-clip"><img src="{PH}{img}" alt="{alt}" loading="lazy"></span>' if img else '<span class="ic-biz-photo is-graphic" aria-hidden="true"><span>SEWERAGE</span><i></i><i></i><i></i></span>')
        + f'<span class="ic-biz-body"><span class="ic-biz-no">{i+1:02d}</span><strong>{t}</strong><span>{d}</span><b aria-hidden="true">→</b></span></a>'
        for i, (t, d, img, alt, href) in enumerate(bz["items"]))
    steps = "".join(f'<li class="reveal" data-delay="{i}"><span class="ic-step-dot" aria-hidden="true"></span><small>{en}</small><h3>{t}</h3><p>{d}</p></li>' for i, (en, t, d) in enumerate(ap["steps"]))
    w = wk["items"]
    facts = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in ab["facts"])
    words = "".join(f'<li><strong>{k}</strong><span>{v}</span></li>' for k, v in ws["words"])
    plinks = "".join(f'<li><a href="{href}"><small>{en}</small><strong>{ja}</strong><span>{d}</span><b aria-hidden="true">→</b></a></li>' for en, ja, d, href in pp["links"])
    roles = "".join(f'<a class="ic-role reveal" href="{href}"><span class="ic-role-photo ic-clip"><img src="{PH}{img}" alt="{alt}" loading="lazy"></span><span class="ic-role-body"><small>{en}</small><strong>{ja}</strong><span>{d}</span><b aria-hidden="true">→</b></span></a>' for ja, en, d, img, alt, href in rc["roles"])
    news = "".join(f'<li><a href="{url}" target="_blank" rel="noopener noreferrer"><span class="ic-serial" aria-hidden="true">{i+1:02d}</span><span class="ic-news-meta">{cat}' + (f'<time datetime="{iso}">{date}</time>' if iso else '') + f'</span><span class="ic-news-title">{t}</span><b aria-hidden="true">↗</b><span class="sr-only">（外部サイトが開きます）</span></a></li>' for i, (iso, date, cat, t, url) in enumerate(nw["items"]))

    body = f'''
{top_hero("top-hero", "hero-title", h["label"], br(h["h1"]), h["lead"], PH + h["img"][0], h["img"][1], cls="is-ic")}

<!-- 02 ABOUT / PROFILE #top-about｜方式B：CMS 54 Half ＋ 22 Table（大きな1974の背景文字、右上に社屋、左下に概要） -->
<section class="ic-section ic-about" id="top-about" aria-labelledby="about-title" data-cms-id="54,22" data-implementation="B">
  <p class="ic-year" aria-hidden="true">1974</p>
  <div class="ic-wrap ic-about-grid">
    <figure class="ic-about-photo ic-clip reveal"><img src="{PH}{ab["img"][0]}" alt="{ab["img"][1]}" loading="lazy"><figcaption>{ab["caption"]}</figcaption></figure>
    <div class="ic-about-copy">
      {label(2, ab["label"], ab["ja"])}
      <h2 id="about-title">{br(ab["h2"])}</h2>
      <p>{ab["body"]}</p>
      <dl class="ic-facts">{facts}</dl>
      {a(ab["cta"][0], ab["cta"][1], "ic-link")}
    </div>
  </div>
</section>

<!-- 03 BUSINESS #top-business｜方式B：CMS 16 Card Four（2×2の大判写真＋大きな工種名。写真のない工種は図柄） -->
<section class="ic-section ic-business" id="top-business" aria-labelledby="biz-title" data-cms-id="16" data-implementation="B">
  <div class="ic-wrap">
    <div class="ic-title-row">{label(3, bz["label"], bz["ja"])}<h2 id="biz-title">{br(bz["h2"])}</h2><p>{bz["lead"]}</p></div>
    <div class="ic-biz">{biz}</div>
    <div class="ic-end">{a(bz["cta"][0], bz["cta"][1], "ic-btn is-primary")}</div>
    <p class="review-note">下水道工事は、工種と一致する写真が届くまで写真なしの図柄で表示しています。</p>
  </div>
</section>

<!-- 04 OUR APPROACH #top-process｜方式B：CMS 54 Half ＋ 80 H2 Text（横の細い線に沿った3段階＋写真の境に淡い面） -->
<section class="ic-section ic-approach" id="top-process" aria-labelledby="approach-title" data-cms-id="54,80" data-implementation="B">
  <div class="ic-wrap">
    <div class="ic-title-row">{label(4, ap["label"], ap["ja"])}<h2 id="approach-title">{br(ap["h2"])}</h2><p>{ap["lead"]}</p></div>
    <ol class="ic-steps"><span class="ic-steps-line reveal" aria-hidden="true"></span>{steps}</ol>
    <p class="ic-note">{ap["note"]}</p>
    <div class="ic-approach-photo"><span class="ic-approach-plate" aria-hidden="true"></span><figure class="ic-clip reveal"><img src="{PH}{ap["img"][0]}" alt="{ap["img"][1]}" loading="lazy"></figure></div>
    <div class="ic-end">{a(ap["cta"][0][0], ap["cta"][0][1], "ic-btn is-primary")}{a(ap["cta"][1][0], ap["cta"][1][1], "ic-link")}</div>
  </div>
</section>

<!-- 05 WORKS / PHOTO #top-works｜方式A/B：CMS 584 Photo Gallery（全幅：施工全景1枚＝7、細部2枚＝5） -->
<section class="ic-works" id="top-works" aria-labelledby="works-title" data-cms-id="584,718" data-implementation="A/B">
  <div class="ic-wrap ic-title-row">{label(5, wk["label"], wk["ja"])}<h2 id="works-title">{br(wk["h2"])}</h2><p>{wk["lead"]}</p></div>
  <div class="ic-mosaic">
    <figure class="is-main ic-clip reveal"><img src="{PH}{w[0][0]}" alt="{w[0][1]}" loading="lazy"><figcaption>{w[0][2]}</figcaption></figure>
    <figure class="ic-clip reveal"><img src="{PH}{w[1][0]}" alt="{w[1][1]}" loading="lazy"><figcaption>{w[1][2]}</figcaption></figure>
    <figure class="ic-clip reveal"><img src="{PH}{w[2][0]}" alt="{w[2][1]}" loading="lazy"><figcaption>{w[2][2]}</figcaption></figure>
  </div>
  <div class="ic-wrap ic-end">{a(wk["cta"][0][0], wk["cta"][0][1], "ic-btn is-primary")}{a(wk["cta"][1][0], wk["cta"][1][1], "ic-link")}</div>
</section>

<!-- 06 WORK STYLE #top-workstyle｜方式B：CMS 54 Half ＋ 787（淡青の帯に事務所全景、右に縦長の現場写真、3つの大きな言葉） -->
<section class="ic-section ic-workstyle" id="top-workstyle" aria-labelledby="ws-title" data-cms-id="54,787" data-implementation="B">
  <div class="ic-wrap ic-ws-grid">
    <div class="ic-ws-copy">
      {label(6, ws["label"], ws["ja"])}
      <h2 id="ws-title">{br(ws["h2"])}</h2>
      <p>{ws["lead"]}</p>
      <ul class="ic-words">{words}</ul>
      {a(ws["cta"][0], ws["cta"][1], "ic-link")}
    </div>
    <figure class="ic-ws-office ic-clip reveal"><img src="{PH}{ws["office"][0]}" alt="{ws["office"][1]}" loading="lazy"><figcaption>{ws["office"][2]}</figcaption></figure>
    <figure class="ic-ws-field ic-clip reveal"><img src="{PH}{ws["field"][0]}" alt="{ws["field"][1]}" loading="lazy"><figcaption>{ws["field"][2]}</figcaption></figure>
  </div>
</section>

<!-- 07 PEOPLE #top-people｜方式B：CMS 54 Half ＋ 42（余白のある横長の写真1枚、写真の外に3列の案内） -->
<section class="ic-section ic-people" id="top-people" aria-labelledby="people-title" data-cms-id="54,42" data-implementation="B">
  <div class="ic-wrap">
    <div class="ic-title-row">{label(7, pp["label"], pp["ja"])}<h2 id="people-title">{br(pp["h2"])}</h2><p>{pp["lead"]}</p></div>
    <figure class="ic-people-photo ic-clip reveal"><img src="{PH}{pp["img"][0]}" alt="{pp["img"][1]}" loading="lazy"></figure>
    <ul class="ic-people-links">{plinks}</ul>
    <div class="ic-end">{a(pp["cta"][0], pp["cta"][1], "ic-btn is-primary")}</div>
  </div>
</section>

<!-- 08 RECRUIT #top-recruit｜方式B：CMS 787 ＋ 42（下部に大きめの2職種入口） -->
<section class="ic-section ic-recruit" id="top-recruit" aria-labelledby="recruit-title" data-cms-id="787,42" data-implementation="B">
  <div class="ic-wrap">
    <div class="ic-title-row">{label(8, rc["label"], rc["ja"])}<h2 id="recruit-title">{br(rc["h2"])}</h2><p>{rc["lead"]}</p></div>
    <div class="ic-roles">{roles}</div>
    <div class="ic-end">{a(rc["cta"][0], rc["cta"][1], "ic-btn is-secondary")}</div>
  </div>
</section>

<!-- 09 INFORMATION #top-news｜方式A：CMS 101 Blog Standard（大きな通番と少数のテキストリンク） -->
<section class="ic-section ic-news" id="top-news" aria-labelledby="news-title" data-cms-id="101,43" data-implementation="A">
  <div class="ic-wrap ic-news-grid">
    <div>{label(9, nw["label"], nw["ja"])}<h2 id="news-title">{br(nw["h2"])}</h2><p>{nw["lead"]}</p>{a(nw["cta"][0], nw["cta"][1], "ic-link")}</div>
    <ol class="ic-news-list">{news}</ol>
  </div>
</section>

<!-- 10 CONTACT / NEXT #top-contact｜方式B：CMS 23/90/43（写真の外側に白い台形のパネル：法人の方／求職者の方） -->
<section class="ic-contact" id="top-contact" aria-labelledby="contact-title" data-cms-id="23,90,43" data-implementation="B">
  <figure class="ic-contact-photo"><img src="{PH}{ct["img"][0]}" alt="{ct["img"][1]}" loading="lazy"></figure>
  <div class="ic-contact-panel reveal">
    {label(10, ct["label"], ct["ja"])}
    <h2 id="contact-title">{br(ct["h2"])}</h2>
    <p>{ct["lead"]}</p>
    <div class="ic-contact-cols">
      <div class="is-client"><h3>法人・取引先の方</h3><dl><div><dt>電話</dt><dd>{TEL}</dd></div><div><dt>所在地</dt><dd>{ADDRESS}</dd></div></dl><div class="ic-contact-actions">{a(ct["client"][0][0], ct["client"][0][1], "ic-btn is-primary")}{a(ct["client"][1][0], ct["client"][1][1], "ic-link")}</div></div>
      <div class="is-career"><h3>採用をご検討の方</h3><p>仕事内容、入社後の流れ、待遇・募集条件をまとめています。</p>{a(ct["recruit"][0], ct["recruit"][1], "ic-btn is-secondary")}</div>
    </div>
  </div>
</section>
'''
    return page("p1", "d3", "株式会社久留米興業｜道路の復旧舗装から、水道・土木工事まで。（比較用TOP：構成①×デザイン③ 表現重視）",
                "構成①（会社理解）×デザイン③ INFRASTRUCTURE CANVAS（表現重視）の比較用TOP。",
                body, "お問い合わせ", ct["client"][0][1])

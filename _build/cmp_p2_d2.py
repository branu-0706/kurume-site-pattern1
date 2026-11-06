# 構成② × デザイン②｜HUMAN ATLAS（人物の視点で読む独自エディトリアル）
# 最大1160pxの誌面グリッド。余白を多く取り、1:1／4:5／16:9の写真を組み合わせる。輪郭線は薄い青灰。
# 動き：スクロールで写真とキャプションが0.3〜0.5秒で段階表示。自動スライドなし。色は --kk-* のみ。
from cmp_common import page
from cmp_copy import P2 as C, PH, FIELDS, br, a


def chapter(no, en, ja):
    return f'<p class="ha-chapter"><span class="ha-ch-no">CHAPTER {no:02d}</span><span class="ha-ch-en">{en}</span><span class="ha-ch-ja">{ja}</span></p>'


def fig(img, cls="", cap=True):
    f, alt = img[0], img[1]
    c = f'<figcaption>{img[2]}</figcaption>' if cap and len(img) > 2 else ""
    return f'<figure class="ha-fig {cls} reveal"><img src="{PH}{f}" alt="{alt}" loading="lazy">{c}</figure>'


def build():
    h, hi, ld, ch, bz, vo, fu, rc, pr, cl = (C[k] for k in ["hero", "history", "leader", "change", "business", "voices", "future", "recruit", "proof", "close"])
    chips = "".join(f'<li><a href="@P2@about/index.html#about-business">{t}</a></li>' for t, _ in FIELDS)
    hero_chips = "".join(f'<li>{t}</li>' for t, _ in FIELDS)
    facts = ld["facts"]
    points = "".join(f'<article class="ha-point reveal" data-delay="{i}"><span class="ha-point-no">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></article>' for i, (t, d) in enumerate(ch["points"]))
    notes = []
    for i, (t, d, img, alt) in enumerate(bz["items"]):
        media = f'<img src="{PH}{img}" alt="{alt}" loading="lazy">' if img else '<span class="ha-note-blank" aria-hidden="true">SEWERAGE</span>'
        notes.append(f'<li class="ha-note is-{i+1} reveal"><span class="ha-note-media">{media}</span><span class="ha-note-tag">FIELD {i+1:02d}</span><h3>{t}</h3><p>{d}</p></li>')
    sales = "".join(f'<a class="ha-person is-{i+1} reveal" href="{url}" target="_blank" rel="noopener noreferrer"><span class="ha-person-photo"><img src="{PH}{img}" alt="営業職の{n}" loading="lazy"></span><span class="ha-person-role">{role}</span><strong>{n}</strong><span class="ha-person-text">{d}</span><span class="ha-more">記事を読む ↗</span><span class="sr-only">（外部サイトが開きます）</span></a>' for i, (n, role, d, img, url) in enumerate(vo["sales"]))
    talk = "".join(f'<div><span class="ha-talk-role">{role}</span><strong>{n}</strong><p>{d}</p></div>' for n, role, d in vo["talk"]["people"])
    roles = "".join(f'<div class="ha-role reveal"><span class="ha-role-photo"><img src="{PH}{img}" alt="{alt}" loading="lazy"></span><div><span class="ha-role-en">{en}</span><h3>{ja}</h3><p>{d}</p>{a("仕事内容を見る", href, "ha-link")}</div></div>' for ja, en, d, img, alt, href in rc["roles"])
    reads = "".join(f'<li><a href="{url}" target="_blank" rel="noopener noreferrer"><span class="ha-read-cat">{cat}</span><span class="ha-read-title">{t}</span><span class="ha-read-go">続きを読む ↗</span><span class="sr-only">（外部サイトが開きます）</span></a></li>' for cat, t, url in pr["reads"])
    exits = "".join(f'<li class="reveal" data-delay="{i}"><span class="ha-exit-sub">{sub}</span>{a(t, u, "ha-exit")}</li>' for i, (t, u, sub) in enumerate(cl["cta"]))

    body = f'''
<!-- 01 HERO / 50 YEARS #top-hero｜方式C：独自HTML＋CSS（事務所の縦長写真と現場の横長写真を並べた二場面。合成しない。CTAなし・画像と文字のみ）。CMS ID参考：734/721 -->
<section class="ha-hero" id="top-hero" aria-labelledby="hero-title" data-cms-id="734,721" data-implementation="C">
  <div class="ha-wrap">
    <div class="ha-hero-copy">
      <p class="ha-hero-label">{h["label"]}</p>
      <h1 id="hero-title">{br(h["h1"])}</h1>
      <p class="ha-hero-lead">{h["lead"]}</p>
      <ul class="ha-chips" aria-label="4つの事業">{hero_chips}</ul>
    </div>
    <div class="ha-hero-scenes">
      <figure class="ha-scene is-office"><img src="{PH}{h["office"][0]}" alt="{h["office"][1]}" width="502" height="627"><figcaption><span>SCENE 01</span>{h["office"][2]}</figcaption></figure>
      <figure class="ha-scene is-site"><img src="{PH}{h["site"][0]}" alt="{h["site"][1]}" width="941" height="627"><figcaption><span>SCENE 02</span>{h["site"][2]}</figcaption></figure>
    </div>
  </div>
</section>

<!-- 02 ORIGIN / HISTORY #top-history｜方式B：CMS 54 Half（社屋写真を余白に独立配置、1974を目次として） -->
<section class="ha-section" id="top-history" aria-labelledby="history-title" data-cms-id="54" data-implementation="B">
  <div class="ha-wrap ha-history">
    <div class="ha-history-copy">
      {chapter(1, hi["label"], hi["ja"])}
      <h2 id="history-title">{br(hi["h2"])}</h2>
      <p>{hi["lead"]}</p>
      <ol class="ha-index" aria-label="会社の歩みの目次"><li><b>1974</b><span>株式会社久留米興業 設立</span></li><li><b>現在</b><span>世田谷区北烏山の社屋で事業を続ける</span></li><li><b>これから</b><span>人と仕事を次の世代へ</span></li></ol>
      {a(hi["cta"][0], hi["cta"][1], "ha-link")}
    </div>
    {fig(hi["img"], "is-isolated")}
    {fig(hi["people_img"], "is-small")}
  </div>
</section>

<!-- 03 LEADERSHIP #top-leader｜方式B：CMS 54 Half（代表写真を中央に大きく、左右に事実だけの短い経歴） -->
<section class="ha-section is-soft" id="top-leader" aria-labelledby="leader-title" data-cms-id="54,43" data-implementation="B">
  <div class="ha-wrap">
    <div class="ha-center-head">{chapter(2, ld["label"], ld["ja"])}<h2 id="leader-title">{br(ld["h2"])}</h2></div>
    <div class="ha-leader gate" data-gate="{ld["gate"]}">
      <div class="ha-fact is-left reveal"><b>{facts[0][0]}</b><span>{facts[0][1]}</span></div>
      <div class="ha-fact is-left2 reveal"><b>{facts[1][0]}</b><span>{facts[1][1]}</span></div>
      {fig(ld["img"], "is-portrait")}
      <div class="ha-fact is-right reveal"><b>{facts[2][0]}</b><span>{facts[2][1]}</span></div>
      <p class="ha-leader-text reveal">{ld["lead"]}</p>
    </div>
    <div class="ha-center">{a(ld["cta"][0], ld["cta"][1], "ha-link")}</div>
  </div>
</section>

<!-- 04 KEEP / CHANGE #top-change｜方式B：CMS 42 Card Three ＋ 54（確認できる3観点を小記事に。写真は職場と現場を対応） -->
<section class="ha-section" id="top-change" aria-labelledby="change-title" data-cms-id="42,54" data-implementation="B">
  <div class="ha-wrap">
    <div class="ha-split-head">{chapter(3, ch["label"], ch["ja"])}<h2 id="change-title">{br(ch["h2"])}</h2><p>{ch["lead"]}</p></div>
    <div class="ha-change">
      <div class="ha-change-photos">{fig(ch["imgs"][0], "is-square")}{fig(ch["imgs"][1], "is-wide")}</div>
      <div class="ha-points">{points}</div>
    </div>
    <p class="ha-honest reveal">{ch["honest"]}</p>
    {a(ch["cta"][0], ch["cta"][1], "ha-link")}
  </div>
</section>

<!-- 05 BUSINESS / SOCIETY #top-business｜方式B：CMS 16 Card Four（4工種の写真と、正式な工種名を目立たせた短い説明） -->
<section class="ha-section is-soft" id="top-business" aria-labelledby="biz-title" data-cms-id="16" data-implementation="B">
  <div class="ha-wrap">
    <div class="ha-split-head">{chapter(4, bz["label"], bz["ja"])}<h2 id="biz-title">{br(bz["h2"])}</h2><p>{bz["lead"]}</p></div>
    <ol class="ha-notes">{"".join(notes)}</ol>
    <div class="ha-row">{fig(bz["life"], "is-life")}<div class="ha-row-text"><p>工事の先には、その道や水道を使う人の毎日があります。</p>{a(bz["cta"][0], bz["cta"][1], "ha-btn is-primary")}</div></div>
  </div>
</section>

<!-- 06 REAL VOICES #top-voices｜方式B：CMS 42 Card Three ＋ 787（営業3名は大きさの違う誌面、現場2名は別サイズの文章ブロック） -->
<section class="ha-section" id="top-voices" aria-labelledby="voices-title" data-cms-id="42,787" data-implementation="B">
  <div class="ha-wrap">
    <div class="ha-split-head">{chapter(5, vo["label"], vo["ja"])}<h2 id="voices-title">{br(vo["h2"])}</h2><p>{vo["lead"]}</p></div>
    <div class="ha-people">{sales}</div>
    <div class="ha-talk reveal"><p class="ha-talk-title">{vo["talk"]["title"]}</p><div class="ha-talk-body">{talk}</div><p class="ha-talk-note">お二人の本人写真は掲載していません。対談の要約です。</p></div>
    <div class="ha-actions is-links">{a(vo["cta"][0][0], vo["cta"][0][1], "ha-link")}{a(vo["cta"][1][0], vo["cta"][1][1], "ha-link")}</div>
  </div>
</section>

<!-- 07 FUTURE #top-future｜方式B：CMS 80 H2 Text ＋ 54（上に現場、下に事務所。継承の意思を縦書きの見出しで） -->
<section class="ha-section is-soft" id="top-future" aria-labelledby="future-title" data-cms-id="80,54" data-implementation="B">
  <div class="ha-wrap ha-future">
    <h2 id="future-title" class="ha-vertical">{br(fu["h2"])}</h2>
    <div class="ha-future-main">
      {chapter(6, fu["label"], fu["ja"])}
      <p class="ha-future-lead">{fu["lead"]}</p>
      {fig(fu["imgs"][0], "is-wide")}
      <div class="ha-future-pair"><div class="reveal"><span class="ha-tag">守る</span><h3>{fu["keep"][0]}</h3><p>{fu["keep"][1]}</p></div><div class="reveal"><span class="ha-tag is-change">変える</span><h3>{fu["change"][0]}</h3><p>{fu["change"][1]}</p></div></div>
      {fig(fu["imgs"][1], "is-office")}
      {a(fu["cta"][0], fu["cta"][1], "ha-btn is-primary")}
    </div>
  </div>
</section>

<!-- 08 RECRUIT #top-recruit｜方式B：CMS 787 Text Two（写真より仕事内容を優先し、条件は採用ページで確認） -->
<section class="ha-section" id="top-recruit" aria-labelledby="recruit-title" data-cms-id="787,42" data-implementation="B">
  <div class="ha-wrap">
    <div class="ha-split-head">{chapter(7, rc["label"], rc["ja"])}<h2 id="recruit-title">{br(rc["h2"])}</h2><p>{rc["lead"]}</p></div>
    <div class="ha-roles">{roles}</div>
    <div class="ha-actions is-links">{a(rc["cta"][0], rc["cta"][1], "ha-btn is-secondary")}{a(rc["conditions"][0], rc["conditions"][1], "ha-link")}</div>
  </div>
</section>

<!-- 09 IN PRACTICE #top-proof｜方式A/B：CMS 584 ＋ 101（社員記事の公開URLと現場写真を「続きを読む」形式で） -->
<section class="ha-section is-soft" id="top-proof" aria-labelledby="proof-title" data-cms-id="584,101" data-implementation="A/B">
  <div class="ha-wrap ha-proof">
    <div>{chapter(8, pr["label"], pr["ja"])}<h2 id="proof-title">{br(pr["h2"])}</h2><p>{pr["lead"]}</p><ul class="ha-reads">{reads}</ul></div>
    <div class="ha-proof-photos">{fig(pr["photos"][0], "is-portrait-sm")}{fig(pr["photos"][1], "is-square")}</div>
  </div>
  <div class="ha-wrap ha-actions is-links">{a(pr["cta"][0][0], pr["cta"][0][1], "ha-link")}{a(pr["cta"][1][0], pr["cta"][1][1], "ha-link")}</div>
</section>

<!-- 10 CONNECT #top-close｜方式B：CMS 90 Btn Text ＋ 23（事業・会社・採用の3つの出口を同じ大きさで） -->
<section class="ha-section ha-close" id="top-close" aria-labelledby="close-title" data-cms-id="90,23" data-implementation="B">
  <div class="ha-wrap">
    <div class="ha-center-head">{chapter(9, cl["label"], "次の一歩")}<h2 id="close-title">{br(cl["h2"])}</h2><p>{cl["lead"]}</p></div>
    <ul class="ha-exits">{exits}</ul>
  </div>
</section>
'''
    return page("p2", "d2", "株式会社久留米興業｜この街とともに、50年以上。（比較用TOP：構成②×デザイン② 独自性重視）",
                "構成②（ビジョン共感）×デザイン② HUMAN ATLAS（独自性重視）の比較用TOP。",
                body, "お問い合わせ", "https://www.kurume-k.jp/contact")

# パターン② × デザイン②｜PERSONAL DOCUMENTARY（読み物のように静かな構成）
# 生成りの白 #F8F8F6、ネイビー文字、ブルーの極細罫線。本文幅940〜1080px、リード650〜760px。動きは初回のopacity 0.3sのみ。
from cmp_common import page
from cmp_copy import P2 as C, PH, br, a


def label(en, ja):
    return f'<p class="d2p-label"><span>{en}</span>{ja}</p>'


def build():
    h, st, ld, ch, wk, vo, nx, rc, pr, cl = (C[k] for k in ["hero", "story", "leader", "change", "work", "voices", "next", "recruit", "proof", "close"])
    chapters = "".join(f'<li><span class="d2p-ch">CHAPTER {i+1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(ch["items"]))
    index = "".join(f'<li><span>{i+1:02d}</span><div><strong>{t}</strong><p>{d}</p></div></li>' for i, (t, d, *_ ) in enumerate(wk["items"]))
    sales = "".join(f'<a class="d2p-person" href="{url}" target="_blank" rel="noopener noreferrer"><img src="{PH}{img}" alt="営業職の{n}" loading="lazy"><small>営業職｜{n}</small><strong>{role}</strong><p>{d}</p><span class="d2p-more">インタビューを読む <b aria-hidden="true">↗</b></span><span class="sr-only">（外部サイトが開きます）</span></a>' for n, role, d, img, url in vo["sales"])
    field = "".join(f'<div class="d2p-field"><small>現場職｜{role}</small><strong>{n}</strong><p>{d}</p></div>' for n, role, d in vo["field"])
    roles = "".join(f'<div class="d2p-role"><small>{en}</small><h3>{t}</h3><p>{d}</p>{a(cta[0], cta[1], "d2p-link")}</div>' for t, en, d, img, alt, cta in rc["items"])
    iso, date, cat, ntitle, nurl = pr["news"]

    body = f'''
<!-- 01 HERO #top-hero｜方式B/C：CMS 734/721（白地の左に大きなH1、右に枠なしの写真1点） -->
<section class="d2p-hero" id="top-hero" aria-labelledby="hero-title" data-cms-id="734,721" data-implementation="B/C">
  <div class="d2p-wrap d2p-hero-grid">
    <div class="d2p-hero-copy d2p-fade">
      <p class="d2p-hero-label">{h["label"]}</p>
      <h1 id="hero-title">{br(h["h1"])}</h1>
      <p class="d2p-lead">{h["lead"]}</p>
      <div class="d2p-actions">{a(h["cta"][0][0], h["cta"][0][1], "d2p-btn")}{a(h["cta"][1][0], h["cta"][1][1], "d2p-link")}</div>
    </div>
    <figure class="d2p-hero-photo d2p-fade"><img src="{PH}{h["img"][0]}" alt="{h["img"][1]}" width="941" height="627"><figcaption>{h["caption"]}</figcaption></figure>
  </div>
</section>

<!-- 02 OUR STORY #top-story｜方式B：CMS 54 Half（1974 — TODAY の細い線、中央640pxの文章、社屋写真を横長で） -->
<section class="d2p-section" id="top-story" aria-labelledby="story-title" data-cms-id="54" data-implementation="B">
  <div class="d2p-wrap reveal">
    <p class="d2p-since" aria-hidden="true"><span>1974</span><i></i><span>TODAY</span></p>
    <div class="d2p-narrow">{label(st["label"], st["ja"])}<h2 id="story-title">{br(st["h2"])}</h2><p>{st["body"]}</p>{a(st["cta"][0], st["cta"][1], "d2p-link")}</div>
    <figure class="d2p-landscape"><img src="{PH}{st["img"][0]}" alt="{st["img"][1]}" loading="lazy"><figcaption>{st["caption"]}</figcaption></figure>
  </div>
</section>

<!-- 03 THE PEOPLE BEHIND CHANGE #top-leader｜方式B：CMS 54 Half（人物写真を左55%に大きく） -->
<section class="d2p-section is-tone" id="top-leader" aria-labelledby="leader-title" data-cms-id="54,35" data-implementation="B">
  <div class="d2p-leader reveal">
    <figure class="d2p-leader-photo"><img src="{PH}{ld["img"][0]}" alt="{ld["img"][1]}" loading="lazy"><figcaption>{ld["caption"]}</figcaption></figure>
    <div class="d2p-leader-copy gate" data-gate="{ld["gate"]}">
      {label(ld["label"], ld["ja"])}
      <h2 id="leader-title">{br(ld["h2"])}</h2>
      <p>{ld["body"]}</p>
      <ol class="d2p-bio">{"".join(f"<li><b>{y}</b><span>{t}</span></li>" for y, t in ld["steps"])}</ol>
      <div class="d2p-stack">{a(ld["cta"][0][0], ld["cta"][0][1], "d2p-link")}{a(ld["cta"][1][0], ld["cta"][1][1], "d2p-link")}</div>
    </div>
  </div>
</section>

<!-- 04 CHANGES IN PRACTICE #top-change｜方式B：CMS 43 ＋ 787（色付きカードではなく細線で区切った3つの章） -->
<section class="d2p-section" id="top-change" aria-labelledby="change-title" data-cms-id="43,787" data-implementation="B">
  <div class="d2p-wrap">
    <div class="d2p-narrow reveal">{label(ch["label"], ch["ja"])}<h2 id="change-title">{br(ch["h2"])}</h2><p>{ch["lead"]}</p></div>
    <ol class="d2p-chapters reveal">{chapters}</ol>
    <p class="d2p-note reveal">{ch["honest"]}</p>
    <div class="d2p-narrow d2p-stack reveal">{a(ch["cta"][0][0], ch["cta"][0][1], "d2p-link")}{a(ch["cta"][1][0], ch["cta"][1][1], "d2p-link")}</div>
  </div>
</section>

<!-- 05 OUR BUSINESS #top-work｜方式B：CMS 54 Half（写真1枚＋4行の目次） -->
<section class="d2p-section is-tone" id="top-work" aria-labelledby="work-title" data-cms-id="54" data-implementation="B">
  <div class="d2p-wrap d2p-work reveal">
    <figure class="d2p-work-photo"><img src="{PH}{wk["items"][0][2]}" alt="{wk["items"][0][3]}" loading="lazy"><figcaption>道路の舗装工事</figcaption></figure>
    <div>{label(wk["label"], wk["ja"])}<h2 id="work-title">{br(wk["h2"])}</h2><p>{wk["lead"]}</p><ol class="d2p-index">{index}</ol>{a(wk["cta"][0], wk["cta"][1], "d2p-link")}</div>
  </div>
</section>

<!-- 06 REAL VOICES #top-voices｜方式B：CMS 42 Card Three（営業）＋ 787 Text Two（現場） -->
<section class="d2p-section" id="top-voices" aria-labelledby="voices-title" data-cms-id="42,787" data-implementation="B">
  <div class="d2p-wrap">
    <div class="d2p-narrow reveal">{label(vo["label"], vo["ja"])}<h2 id="voices-title">{br(vo["h2"])}</h2><p>{vo["lead"]}</p></div>
    <div class="d2p-people reveal">{sales}</div>
    <div class="d2p-fields reveal"><p class="d2p-fields-label">現場の言葉</p>{field}</div>
    <p class="review-note">現場職のお二人は本人写真が未提供のため、名前と説明文だけで紹介しています。</p>
    <div class="d2p-narrow d2p-stack reveal">{a(vo["cta"][1][0], vo["cta"][1][1], "d2p-link")}{a(vo["cta"][0][0], vo["cta"][0][1], "d2p-link")}{a(vo["blog"][0], vo["blog"][1], "d2p-link")}</div>
  </div>
</section>

<!-- 07 FOR THE NEXT 50 YEARS #top-next｜方式B：CMS 80 ＋ 54（大きなネイビー面は使わず、余白の中に見出し） -->
<section class="d2p-section is-tone" id="top-next" aria-labelledby="next-title" data-cms-id="80,54" data-implementation="B">
  <div class="d2p-wrap d2p-next reveal">
    <div>{label(nx["label"], nx["ja"])}<h2 id="next-title">{br(nx["h2"])}</h2><p>{nx["body"]}</p>{a(nx["cta"][0], nx["cta"][1], "d2p-link")}</div>
    <figure class="d2p-next-photo"><img src="{PH}{nx["img"][0]}" alt="{nx["img"][1]}" loading="lazy"><figcaption>{nx["caption"]}</figcaption></figure>
  </div>
</section>

<!-- 08 JOIN OUR TEAM #top-recruit｜方式B：CMS 787 Two Text（文字中心で2職種を並べる） -->
<section class="d2p-section" id="top-recruit" aria-labelledby="recruit-title" data-cms-id="787,90" data-implementation="B">
  <div class="d2p-wrap">
    <div class="d2p-narrow reveal">{label(rc["label"], rc["ja"])}<h2 id="recruit-title">{br(rc["h2"])}</h2><p>{rc["lead"]}</p></div>
    <div class="d2p-roles reveal">{roles}</div>
    <div class="d2p-center reveal">{a(rc["cta"][0], rc["cta"][1], "d2p-btn")}</div>
  </div>
</section>

<!-- 09 WORKS & NEWS #top-workproof｜方式A/B：CMS 718 ＋ 101（誌面のように横長に） -->
<section class="d2p-section is-tone" id="top-workproof" aria-labelledby="proof-title" data-cms-id="718,101" data-implementation="A/B">
  <div class="d2p-wrap">
    <div class="d2p-narrow reveal">{label(pr["label"], pr["ja"])}<h2 id="proof-title">{br(pr["h2"])}</h2><p>{pr["lead"]}</p></div>
    <div class="d2p-proof reveal">
      <figure><img src="{PH}{pr["photos"][0][0]}" alt="{pr["photos"][0][1]}" loading="lazy"><figcaption>施工の様子</figcaption></figure>
      <figure><img src="{PH}{pr["photos"][1][0]}" alt="{pr["photos"][1][1]}" loading="lazy"><figcaption>施工の様子</figcaption></figure>
      <a class="d2p-article" href="{nurl}" target="_blank" rel="noopener noreferrer"><time datetime="{iso}">{date}</time><small>{cat}</small><strong>{ntitle}</strong><span class="d2p-more">記事を読む <b aria-hidden="true">↗</b></span><span class="sr-only">（外部サイトが開きます）</span></a>
    </div>
    <div class="d2p-narrow d2p-stack reveal">{a(pr["cta"][0][0], pr["cta"][0][1], "d2p-link")}{a(pr["cta"][1][0], pr["cta"][1][1], "d2p-link")}</div>
  </div>
</section>

<!-- 10 NEXT STEP #top-footer｜方式B：CMS 90 ＋ 23（幅760pxの静かな白背景、3方向のリンク） -->
<section class="d2p-close" id="top-footer" aria-labelledby="close-title" data-cms-id="90,23" data-implementation="B">
  <div class="d2p-close-inner reveal">
    <h2 id="close-title">{br(cl["h2"])}</h2>
    <p>{cl["lead"]}</p>
    <ul class="d2p-close-links">{"".join(f"<li>{a(t, u)}</li>" for t, u in cl["cta"])}</ul>
  </div>
</section>
'''
    return page("p2", "d2", "株式会社久留米興業｜この街とともに、50年以上。（比較用TOP：パターン②×デザイン②）",
                "パターン②（ビジョン共感）×デザイン②（人物ドキュメンタリー）の比較用TOP。",
                body, "募集要項", "../../../pattern2/recruit/index.html#recruit-offerings")

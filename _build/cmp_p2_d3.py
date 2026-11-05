# パターン② × デザイン③｜NEXT 50 TIMELINE（時間軸のストーリー）
# PCは左から25%の位置に縦の時間軸ラインが全セクションを通る（SPは左端16px）。装飾数字「1974」、紺と白の強い対比。
# 動き：ラインはスクロールで最大0.5秒のclip表示、代表写真はfade＋12px。スナップ・スクロールロック・カウントアップなし。
from cmp_common import page
from cmp_copy import P2 as C, PH, br, a

FUTURE_STEPS = [("これまで", "勤務時間の管理や人員配置を見直してきました。"),
                ("いまの課題", "現場には今も忙しい日や、休憩に余裕を感じにくい日があります。"),
                ("これから", "経験や技術を次の世代へ渡せるよう、教え方を整えていきます。")]


def side(en, ja, light=False):
    return f'<div class="d3t-side{" is-light" if light else ""}"><span class="d3t-dot" aria-hidden="true"></span><p><span>{en}</span>{ja}</p></div>'


def line(light=False):
    return f'<span class="d3t-line{" is-light" if light else ""} reveal" aria-hidden="true"></span>'


def build():
    h, st, ld, ch, wk, vo, nx, rc, pr, cl = (C[k] for k in ["hero", "story", "leader", "change", "work", "voices", "next", "recruit", "proof", "close"])
    branches = "".join(f'<li class="reveal" data-delay="{i}"><span class="d3t-branch" aria-hidden="true"></span><small>{i+1:02d}</small><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(ch["items"]))
    biz = "".join(
        f'<li class="reveal" data-delay="{i}"><span class="d3t-branch" aria-hidden="true"></span>'
        + (f'<img src="{PH}{img}" alt="{alt}" loading="lazy">' if img else '<span class="d3t-noimg" aria-hidden="true">SUPPORT</span>')
        + f'<div><strong>{t}</strong><p>{d}</p></div></li>'
        for i, (t, d, img, alt) in enumerate(wk["items"]))
    sales = "".join(f'<a class="d3t-person" href="{url}" target="_blank" rel="noopener noreferrer"><img src="{PH}{img}" alt="営業職の{n}" loading="lazy"><small>営業職｜{role}</small><strong>{n}</strong><p>{d}</p><span class="d3t-more">インタビューを読む ↗</span><span class="sr-only">（外部サイトが開きます）</span></a>' for n, role, d, img, url in vo["sales"])
    field = "".join(f'<div><small>現場職｜{role}</small><strong>{n}</strong><p>{d}</p></div>' for n, role, d in vo["field"])
    roles = "".join(f'<a class="d3t-role" href="{cta[1]}"><img src="{PH}{img}" alt="{alt}" loading="lazy"><div><small>{en}</small><h3>{t}</h3><p>{d}</p><span class="d3t-more">{cta[0]} →</span></div></a>' for t, en, d, img, alt, cta in rc["items"])
    iso, date, cat, ntitle, nurl = pr["news"]
    steps = "".join(f'<li><b>{k}</b><span>{v}</span></li>' for k, v in FUTURE_STEPS)

    body = f'''
<!-- 01 HERO #top-hero｜方式C：独自HTML＋CSS（道路現場の写真＋左側の巨大H1、端に「1974 → NEXT 50」）。CMS ID参考：734/721 -->
<section class="d3t-hero" id="top-hero" aria-labelledby="hero-title" data-cms-id="734,721" data-implementation="C">
  <img class="d3t-hero-img" src="{PH}{h["img"][0]}" alt="{h["img"][1]}" width="941" height="627">
  <div class="d3t-hero-shade" aria-hidden="true"></div>
  <div class="d3t-in d3t-hero-inner">
    <p class="d3t-hero-label">{h["label"]}</p>
    <h1 id="hero-title"><span>{h["h1"][0]}</span><span>{h["h1"][1]}</span></h1>
    <p class="d3t-hero-lead">{h["lead"]}</p>
    <div class="d3t-actions">{a(h["cta"][0][0], h["cta"][0][1], "d3t-btn is-white")}{a(h["cta"][1][0], h["cta"][1][1], "d3t-btn is-line")}</div>
  </div>
  <p class="d3t-era" aria-hidden="true"><span>1974</span><i></i><span>NEXT 50</span></p>
</section>

<!-- 02 OUR STORY #top-story｜方式B：CMS 54 Half（大きな1974から、以降の全セクションへ縦ラインが続く） -->
<section class="d3t-sec d3t-story" id="top-story" aria-labelledby="story-title" data-cms-id="54" data-implementation="B">
  <div class="d3t-in">
    <p class="d3t-year" aria-hidden="true">1974</p>
    <div class="d3t-row">{line()}
      {side(st["label"], st["ja"])}
      <div class="d3t-main d3t-split">
        <div class="reveal"><h2 id="story-title">{br(st["h2"])}</h2><p>{st["body"]}</p>{a(st["cta"][0], st["cta"][1], "d3t-link")}</div>
        <figure class="reveal"><img src="{PH}{st["img"][0]}" alt="{st["img"][1]}" loading="lazy"><figcaption>{st["caption"]}</figcaption></figure>
      </div>
    </div>
  </div>
</section>

<!-- 03 THE TURNING POINT #top-leader｜方式B：CMS 54 Half（代表写真を右に大きく、左に歩みの要約） -->
<section class="d3t-sec" id="top-leader" aria-labelledby="leader-title" data-cms-id="54" data-implementation="B">
  <div class="d3t-in"><div class="d3t-row">{line()}
    {side("THE TURNING POINT", ld["ja"])}
    <div class="d3t-main d3t-leader">
      <div class="gate" data-gate="{ld["gate"]}">
        <p class="d3t-kicker">{ld["label"]}</p>
        <h2 id="leader-title">{br(ld["h2"])}</h2>
        <p>{ld["body"]}</p>
        <ol class="d3t-ages">{"".join(f"<li><b>{y}</b>{t}</li>" for y, t in ld["steps"])}</ol>
        <div class="d3t-links">{a(ld["cta"][0][0], ld["cta"][0][1], "d3t-link")}{a(ld["cta"][1][0], ld["cta"][1][1], "d3t-link")}</div>
      </div>
      <figure class="d3t-portrait reveal"><img src="{PH}{ld["img"][0]}" alt="{ld["img"][1]}" loading="lazy"><figcaption>{ld["caption"]}</figcaption></figure>
    </div>
  </div></div>
</section>

<!-- 04 CHANGES IN PRACTICE #top-change｜方式B：CMS 42 Card Three（縦ラインから3本の分岐） -->
<section class="d3t-sec is-soft" id="top-change" aria-labelledby="change-title" data-cms-id="42" data-implementation="B">
  <div class="d3t-in"><div class="d3t-row">{line()}
    {side(ch["label"], ch["ja"])}
    <div class="d3t-main">
      <h2 id="change-title" class="reveal">{br(ch["h2"])}</h2><p class="reveal">{ch["lead"]}</p>
      <ol class="d3t-branches">{branches}</ol>
      <p class="d3t-note reveal">{ch["honest"]}</p>
      <div class="d3t-links reveal">{a(ch["cta"][0][0], ch["cta"][0][1], "d3t-link")}{a(ch["cta"][1][0], ch["cta"][1][1], "d3t-link")}</div>
    </div>
  </div></div>
</section>

<!-- 05 OUR BUSINESS #top-work｜方式B：CMS 16 Card Four（時間軸から横に分岐する、今の仕事のリスト） -->
<section class="d3t-sec" id="top-work" aria-labelledby="work-title" data-cms-id="16" data-implementation="B">
  <div class="d3t-in"><div class="d3t-row">{line()}
    {side("NOW", "今、街を支える仕事")}
    <div class="d3t-main">
      <p class="d3t-kicker reveal">{wk["label"]}</p>
      <h2 id="work-title" class="reveal">{br(wk["h2"])}</h2><p class="reveal">{wk["lead"]}</p>
      <ol class="d3t-biz">{biz}</ol>
      {a(wk["cta"][0], wk["cta"][1], "d3t-link")}
    </div>
  </div></div>
</section>

<!-- 06 REAL VOICES #top-voices｜方式B：CMS 42 Card Three ＋ 787 Text Two（ずらした写真と横幅の広い対談パネル） -->
<section class="d3t-sec is-soft" id="top-voices" aria-labelledby="voices-title" data-cms-id="42,787" data-implementation="B">
  <div class="d3t-in"><div class="d3t-row">{line()}
    {side(vo["label"], vo["ja"])}
    <div class="d3t-main">
      <p class="d3t-editorial reveal">道を支えるのは、人。</p>
      <h2 id="voices-title" class="reveal">{br(vo["h2"])}</h2><p class="reveal">{vo["lead"]}</p>
      <div class="d3t-people reveal">{sales}</div>
      <div class="d3t-duo reveal"><p class="d3t-duo-title">現場職の二人</p>{field}</div>
      <div class="d3t-links reveal">{a(vo["cta"][1][0], vo["cta"][1][1], "d3t-link")}{a(vo["cta"][0][0], vo["cta"][0][1], "d3t-link")}{a(vo["blog"][0], vo["blog"][1], "d3t-link")}</div>
    </div>
  </div></div>
</section>

<!-- 07 FOR THE NEXT 50 YEARS #top-next｜方式B：CMS 80 ＋ 54（縦ラインが濃紺の面へ入っていく） -->
<section class="d3t-sec is-navy" id="top-next" aria-labelledby="next-title" data-cms-id="80,54" data-implementation="B">
  <div class="d3t-in"><div class="d3t-row">{line(True)}
    {side(nx["label"], nx["ja"], light=True)}
    <div class="d3t-main">
      <h2 id="next-title" class="d3t-xl reveal">{br(nx["h2"])}</h2>
      <p class="reveal">{nx["body"]}</p>
      <ol class="d3t-steps reveal">{steps}</ol>
      <figure class="d3t-next-photo reveal"><img src="{PH}{nx["img"][0]}" alt="{nx["img"][1]}" loading="lazy"></figure>
      {a(nx["cta"][0], nx["cta"][1], "d3t-btn is-white")}
    </div>
  </div></div>
</section>

<!-- 08 JOIN OUR TEAM #top-recruit｜方式B：CMS 787 Two Text ＋ 90（左に営業、右に現場、下に条件への直接リンク） -->
<section class="d3t-sec" id="top-recruit" aria-labelledby="recruit-title" data-cms-id="787,90" data-implementation="B">
  <div class="d3t-in"><div class="d3t-row">{line()}
    {side(rc["label"], rc["ja"])}
    <div class="d3t-main">
      <h2 id="recruit-title" class="reveal">{br(rc["h2"])}</h2><p class="reveal">{rc["lead"]}</p>
      <div class="d3t-roles reveal">{roles}</div>
      {a(rc["cta"][0], rc["cta"][1], "d3t-btn is-navy")}
    </div>
  </div></div>
</section>

<!-- 09 WORKS & NEWS #top-workproof｜方式A/B：CMS 718 ＋ 101（実写真の帯と記事） -->
<section class="d3t-sec is-soft" id="top-workproof" aria-labelledby="proof-title" data-cms-id="718,101" data-implementation="A/B">
  <div class="d3t-in"><div class="d3t-row">{line()}
    {side(pr["label"], pr["ja"])}
    <div class="d3t-main">
      <h2 id="proof-title" class="reveal">{br(pr["h2"])}</h2><p class="reveal">{pr["lead"]}</p>
      <div class="d3t-strip reveal">
        <figure><img src="{PH}{pr["photos"][0][0]}" alt="{pr["photos"][0][1]}" loading="lazy"></figure>
        <figure><img src="{PH}{pr["photos"][1][0]}" alt="{pr["photos"][1][1]}" loading="lazy"></figure>
        <a class="d3t-news" href="{nurl}" target="_blank" rel="noopener noreferrer"><time datetime="{iso}">{date}</time><small>{cat}</small><strong>{ntitle}</strong><span class="d3t-more">記事を読む ↗</span><span class="sr-only">（外部サイトが開きます）</span></a>
      </div>
      <div class="d3t-links reveal">{a(pr["cta"][0][0], pr["cta"][0][1], "d3t-link")}{a(pr["cta"][1][0], pr["cta"][1][1], "d3t-link")}</div>
    </div>
  </div></div>
</section>

<!-- 10 NEXT STEP #top-footer｜方式B：CMS 90 ＋ 23（時間軸のラインが3本のリンクへ分岐） -->
<section class="d3t-sec is-navy d3t-close" id="top-footer" aria-labelledby="close-title" data-cms-id="90,23" data-implementation="B">
  <div class="d3t-in"><div class="d3t-row">{line(True)}
    {side(cl["label"], "次の一歩", light=True)}
    <div class="d3t-main">
      <h2 id="close-title" class="reveal">{br(cl["h2"])}</h2><p class="reveal">{cl["lead"]}</p>
      <ul class="d3t-fork">{"".join(f'<li class="reveal" data-delay="{i}"><span class="d3t-branch" aria-hidden="true"></span>{a(t, u)}</li>' for i, (t, u) in enumerate(cl["cta"]))}</ul>
    </div>
  </div></div>
</section>
'''
    return page("p2", "d3", "株式会社久留米興業｜この街とともに、50年以上。（比較用TOP：パターン②×デザイン③）",
                "パターン②（ビジョン共感）×デザイン③（時間軸のストーリー）の比較用TOP。",
                body, "募集要項", "../../../pattern2/recruit/index.html#recruit-offerings")

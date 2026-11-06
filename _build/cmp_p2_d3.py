# 構成② × デザイン③｜KEEP / CHANGE（2つの時間軸が交わるユニーク表現）
# 「守る＝インフラ・信頼」（左のKEEPレール）と「変える＝働き方・次世代」（右のCHANGEレール）を二本のレールで対比し、
# 最後に一本に合流してから3つの導線へ開く。PCのみ二軸、SPは1列でKEEP→CHANGEの順に読む。
# 動き：レールの描画0.45s、章ごとに濃淡を変える（色相は変えない）。スクロール固定なし。色は --kk-* のみ。
from cmp_common import page
from cmp_copy import P2 as C, PH, FIELDS, br, a


def rails(extra=""):
    return f'<span class="kc-rail is-keep reveal" aria-hidden="true"></span><span class="kc-rail is-change reveal{extra}" aria-hidden="true"></span>'


def tag(kind):
    return '<span class="kc-tag is-keep">KEEP｜守る</span>' if kind == "keep" else '<span class="kc-tag is-change">CHANGE｜変える</span>'


def fig(img, cls=""):
    return f'<figure class="kc-fig {cls}"><img src="{PH}{img[0]}" alt="{img[1]}" loading="lazy">' + (f'<figcaption>{img[2]}</figcaption>' if len(img) > 2 else "") + '</figure>'


def head(label, ja, h2, hid, lead=None):
    return (f'<div class="kc-head"><p class="kc-label"><span>{label}</span>{ja}</p><h2 id="{hid}">{br(h2)}</h2>'
            + (f'<p class="kc-lead">{lead}</p>' if lead else "") + '</div>')


def build():
    h, hi, ld, ch, bz, vo, fu, rc, pr, cl = (C[k] for k in ["hero", "history", "leader", "change", "business", "voices", "future", "recruit", "proof", "close"])
    chips = "".join(f'<li><a href="@P2@about/index.html#about-business">{t}</a></li>' for t, _ in FIELDS)
    hero_chips = "".join(f'<li>{t}</li>' for t, _ in FIELDS)
    f = ld["facts"]
    keep_list = "".join(f'<li>{t}</li>' for t in ch["keep"])
    points = "".join(f'<li><strong>{t}</strong><span>{d}</span></li>' for t, d in ch["points"])
    biz = "".join(f'<li class="reveal" data-delay="{i}"><span class="kc-biz-no">{i+1:02d}</span>'
                  + (f'<img src="{PH}{img}" alt="{alt}" loading="lazy">' if img else '<span class="kc-biz-blank" aria-hidden="true"></span>')
                  + f'<div><strong>{t}</strong><p>{d}</p></div></li>' for i, (t, d, img, alt) in enumerate(bz["items"]))
    sales = "".join(f'<a class="kc-person reveal" data-delay="{i}" href="{url}" target="_blank" rel="noopener noreferrer"><img src="{PH}{img}" alt="営業職の{n}" loading="lazy"><span class="kc-person-role">{role}</span><strong>{n}</strong><span>{d}</span><span class="kc-more">記事を読む ↗</span><span class="sr-only">（外部サイトが開きます）</span></a>' for i, (n, role, d, img, url) in enumerate(vo["sales"]))
    talk = "".join(f'<div><span class="kc-person-role">{role}</span><strong>{n}</strong><p>{d}</p></div>' for n, role, d in vo["talk"]["people"])
    r0, r1 = rc["roles"]
    role = lambda r: f'<div class="kc-role"><img src="{PH}{r[3]}" alt="{r[4]}" loading="lazy"><span class="kc-role-en">{r[1]}</span><h3>{r[0]}</h3><p>{r[2]}</p>{a("仕事内容を見る", r[5], "kc-link")}</div>'
    reads = "".join(f'<li><a href="{url}" target="_blank" rel="noopener noreferrer"><span>{cat}</span><strong>{t}</strong><b aria-hidden="true">↗</b><span class="sr-only">（外部サイトが開きます）</span></a></li>' for cat, t, url in pr["reads"])
    exits = "".join(f'<li><span>{sub}</span>{a(t, u, "kc-exit")}</li>' for t, u, sub in cl["cta"])

    body = f'''
<!-- 01 HERO / 50 YEARS #top-hero｜方式C：独自HTML＋CSS（独立した白い読み取り領域＋左右2面：守る仕事／変わる会社。CTAなし・画像と文字のみ）。CMS ID参考：734/721 -->
<section class="kc-hero" id="top-hero" aria-labelledby="hero-title" data-cms-id="734,721" data-implementation="C">
  <div class="kc-wrap kc-hero-read">
    <p class="kc-hero-label">{h["label"]}</p>
    <h1 id="hero-title">{br(h["h1"])}</h1>
    <p class="kc-hero-lead">{h["lead"]}</p>
  </div>
  <div class="kc-hero-pair">
    <figure class="kc-hero-panel is-keep"><img src="{PH}{h["site"][0]}" alt="{h["site"][1]}" width="941" height="627"><figcaption>{tag("keep")}<strong>守る仕事</strong><ul class="kc-chips" aria-label="4つの事業">{hero_chips}</ul></figcaption></figure>
    <figure class="kc-hero-panel is-change"><img src="{PH}{h["office"][0]}" alt="{h["office"][1]}" width="1046" height="698"><figcaption>{tag("change")}<strong>変わる会社</strong><span>働き方と、人を育てる仕組み</span></figcaption></figure>
  </div>
</section>

<div class="kc-track">
<!-- 02 ORIGIN / HISTORY #top-history｜方式B：CMS 54 Half（左レール：1974年設立と事業／右レール：現在の職場） -->
<section class="kc-sec" id="top-history" aria-labelledby="history-title" data-cms-id="54" data-implementation="B">
  <div class="kc-wrap">{rails()}
    {head(hi["label"], hi["ja"], hi["h2"], "history-title", hi["lead"])}
    <div class="kc-lanes">
      <div class="kc-lane is-keep reveal">{tag("keep")}<p class="kc-big">1974<small>年設立</small></p><p>道路・水道などの工事を、世田谷を拠点に続けてきました。</p>{fig(hi["img"])}</div>
      <div class="kc-lane is-change reveal">{tag("change")}<p class="kc-big is-word">現在<small>の職場</small></p><p>事務所と現場、それぞれの役割を持つ社員が働いています。</p>{fig(hi["people_img"])}</div>
    </div>
    {a(hi["cta"][0], hi["cta"][1], "kc-link")}
  </div>
</section>

<!-- 03 LEADERSHIP #top-leader｜方式B：CMS 54 Half（代表の経験が二本のレールをつなぐ橋） -->
<section class="kc-sec is-tint" id="top-leader" aria-labelledby="leader-title" data-cms-id="54,43" data-implementation="B">
  <div class="kc-wrap">{rails()}
    {head(ld["label"], ld["ja"], ld["h2"], "leader-title")}
    <div class="kc-bridge gate" data-gate="{ld["gate"]}">
      <span class="kc-bridge-line" aria-hidden="true"></span>
      <div class="kc-bridge-side is-keep reveal">{tag("keep")}<h3>現場の経験</h3><dl><div><dt>{f[0][0]}</dt><dd>{f[0][1]}</dd></div><div><dt>{f[1][0]}</dt><dd>{f[1][1]}</dd></div></dl></div>
      {fig(ld["img"], "kc-bridge-photo")}
      <div class="kc-bridge-side is-change reveal">{tag("change")}<h3>経営と会社づくり</h3><dl><div><dt>{f[2][0]}</dt><dd>{f[2][1]}</dd></div></dl></div>
    </div>
    <p class="kc-center-text">{ld["lead"]}</p>
    <div class="kc-center">{a(ld["cta"][0], ld["cta"][1], "kc-link")}</div>
  </div>
</section>

<!-- 04 KEEP / CHANGE #top-change｜方式B：CMS 787 Text Two（左：守る、右：変える。SPはKEEP→CHANGEの順） -->
<section class="kc-sec" id="top-change" aria-labelledby="change-title" data-cms-id="787,42" data-implementation="B">
  <div class="kc-wrap">{rails()}
    {head(ch["label"], ch["ja"], ch["h2"], "change-title", ch["lead"])}
    <div class="kc-lanes">
      <div class="kc-lane is-keep reveal">{tag("keep")}<h3>守りたいこと</h3><ul class="kc-keep">{keep_list}</ul>{fig(ch["imgs"][1])}</div>
      <div class="kc-lane is-change reveal">{tag("change")}<h3>見直してきたこと</h3><ul class="kc-points">{points}</ul>{fig(ch["imgs"][0])}</div>
    </div>
    <p class="kc-honest">{ch["honest"]}</p>
    {a(ch["cta"][0], ch["cta"][1], "kc-link")}
  </div>
</section>

<!-- 05 BUSINESS / SOCIETY #top-business｜方式B：CMS 16 Card Four ＋ 54（KEEPレーンを約66%に広げて4工種を並べる） -->
<section class="kc-sec is-tint" id="top-business" aria-labelledby="biz-title" data-cms-id="16,54" data-implementation="B">
  <div class="kc-wrap is-wide-keep"><span class="kc-rail is-keep reveal" aria-hidden="true"></span><span class="kc-rail is-change is-shift reveal" aria-hidden="true"></span><span class="kc-jog reveal" aria-hidden="true"></span>
    <div class="kc-lanes is-66">
      <div class="kc-lane is-keep">{head(bz["label"], bz["ja"], bz["h2"], "biz-title", bz["lead"])}{tag("keep")}<ol class="kc-biz">{biz}</ol>{a(bz["cta"][0], bz["cta"][1], "kc-btn is-primary")}</div>
      <div class="kc-lane is-change reveal">{tag("change")}{fig(bz["life"], "is-tall")}<p>工事の先には、その道や水道を使う人の毎日があります。</p></div>
    </div>
  </div>
</section>

<!-- 06 REAL VOICES #top-voices｜方式B：CMS 42 Card Three ＋ 787（営業3名は二本のレールをまたぐ小カード、現場2名は左右をつなぐ文章カード） -->
<section class="kc-sec" id="top-voices" aria-labelledby="voices-title" data-cms-id="42,787" data-implementation="B">
  <div class="kc-wrap">{rails()}
    {head(vo["label"], vo["ja"], vo["h2"], "voices-title", vo["lead"])}
    <div class="kc-people">{sales}</div>
    <div class="kc-talk reveal"><p class="kc-talk-title">{vo["talk"]["title"]}</p><div class="kc-talk-body">{talk}</div><p class="kc-talk-note">お二人の本人写真は掲載していません。対談の要約です。</p></div>
    <div class="kc-links">{a(vo["cta"][0][0], vo["cta"][0][1], "kc-link")}{a(vo["cta"][1][0], vo["cta"][1][1], "kc-link")}</div>
  </div>
</section>

<!-- 07 FUTURE #top-future｜方式B：CMS 80 H2 Text ＋ 787（「工事を次世代へ」と「育成・環境を整える」を2つの大見出しに） -->
<section class="kc-sec is-strong" id="top-future" aria-labelledby="future-title" data-cms-id="80,787" data-implementation="B">
  <div class="kc-wrap">{rails()}
    {head(fu["label"], fu["ja"], fu["h2"], "future-title", fu["lead"])}
    <div class="kc-lanes">
      <div class="kc-lane is-keep reveal">{tag("keep")}<h3 class="kc-xl">{fu["keep"][0]}</h3><p>{fu["keep"][1]}</p>{fig(fu["imgs"][0])}</div>
      <div class="kc-lane is-change reveal">{tag("change")}<h3 class="kc-xl">{fu["change"][0]}</h3><p>{fu["change"][1]}</p>{fig(fu["imgs"][1])}</div>
    </div>
    <div class="kc-center">{a(fu["cta"][0], fu["cta"][1], "kc-btn is-primary")}</div>
  </div>
</section>

<!-- 08 RECRUIT #top-recruit｜方式B：CMS 787 Text Two（営業・現場の2職種を左右のレーンへ、入口は1つ） -->
<section class="kc-sec" id="top-recruit" aria-labelledby="recruit-title" data-cms-id="787,23" data-implementation="B">
  <div class="kc-wrap">{rails()}
    {head(rc["label"], rc["ja"], rc["h2"], "recruit-title", rc["lead"])}
    <div class="kc-lanes"><div class="kc-lane is-keep reveal">{role(r0)}</div><div class="kc-lane is-change reveal">{role(r1)}</div></div>
    <div class="kc-center">{a(rc["cta"][0], rc["cta"][1], "kc-btn is-secondary")}<br>{a(rc["conditions"][0], rc["conditions"][1], "kc-link")}</div>
  </div>
</section>

<!-- 09 IN PRACTICE #top-proof｜方式A/B：CMS 584 ＋ 101（左：施工写真、右：社員記事。写真を加工して時代比較にしない） -->
<section class="kc-sec is-tint" id="top-proof" aria-labelledby="proof-title" data-cms-id="584,101" data-implementation="A/B">
  <div class="kc-wrap">{rails()}
    {head(pr["label"], pr["ja"], pr["h2"], "proof-title", pr["lead"])}
    <div class="kc-lanes">
      <div class="kc-lane is-keep reveal">{tag("keep")}<div class="kc-photo-pair">{fig(pr["photos"][0])}{fig(pr["photos"][1])}</div>{a(pr["cta"][0][0], pr["cta"][0][1], "kc-link")}</div>
      <div class="kc-lane is-change reveal">{tag("change")}<ul class="kc-reads">{reads}</ul>{a(pr["cta"][1][0], pr["cta"][1][1], "kc-link")}</div>
    </div>
  </div>
</section>

<!-- 10 CONNECT #top-close｜方式B：CMS 90 ＋ 23（二本のレールが合流し、3つの導線へ開く装飾線） -->
<section class="kc-sec kc-close" id="top-close" aria-labelledby="close-title" data-cms-id="90,23" data-implementation="B">
  <div class="kc-wrap">
    <svg class="kc-merge" viewBox="0 0 1000 220" preserveAspectRatio="none" aria-hidden="true"><path class="is-keep" d="M0 0 V60 C0 130 500 90 500 150"/><path class="is-change" d="M532 0 V60 C532 120 500 100 500 150"/><path class="is-out" d="M500 150 V180 M500 180 C500 205 167 195 167 220 M500 180 V220 M500 180 C500 205 833 195 833 220"/></svg>
    <div class="kc-close-head"><p class="kc-label"><span>{cl["label"]}</span>次の一歩</p><h2 id="close-title">{br(cl["h2"])}</h2><p class="kc-lead">{cl["lead"]}</p></div>
    <ul class="kc-exits">{exits}</ul>
  </div>
</section>
</div>
'''
    return page("p2", "d3", "株式会社久留米興業｜この街とともに、50年以上。（比較用TOP：構成②×デザイン③ ユニーク表現）",
                "構成②（ビジョン共感）×デザイン③ KEEP / CHANGE（ユニーク表現）の比較用TOP。",
                body, "お問い合わせ", "https://www.kurume-k.jp/contact")

from p2common import *

P = "@R@assets/photos/"

BODY = f'''
<!-- 01 HERO / 50 YEARS #top-hero｜方式C：独自HTML＋CSS（office.css の .story-hero）。CMS ID参考：734/721。HERO内に4つの事業を明示 -->
<section class="story-hero" id="top-hero" aria-labelledby="hero-title" data-cms-id="734,721" data-implementation="C">
  <div class="wrap story-hero-grid">
    <div class="story-hero-copy">
      <p class="story-hero-label anim-enter">1974 / TODAY / NEXT</p>
      <h1 id="hero-title" class="anim-enter" style="--delay:.1s">この街とともに、50年以上。<br><span>信頼をつなぎ、次の時代へ。</span></h1>
      <p class="story-hero-lead anim-enter" style="--delay:.18s">ガス管取替後の復旧舗装工事や水道・土木工事。1974年から積み重ねた仕事と、人を大切にする会社づくり。久留米興業の歩みと、これからを紹介します。</p>
      <div class="story-hero-actions anim-enter" style="--delay:.26s"><a class="btn btn-dark" href="@P2@about/index.html">久留米興業について <span aria-hidden="true">→</span></a><a class="btn btn-outline-light" href="@P2@about/index.html#about-business">事業を知る <span aria-hidden="true">→</span></a></div>
    </div>
    <figure class="story-hero-media anim-enter" style="--delay:.14s"><img src="{P}field-work-street.jpg" alt="重機とともに歩道の路盤をつくる施工中の現場" width="941" height="627"><figcaption>施工中の様子</figcaption></figure>
  </div>
  <div class="story-hero-fields anim-enter" style="--delay:.3s">
    <div class="wrap"><p>4 BUSINESS FIELDS</p><ul aria-label="久留米興業の事業">
      <li><a href="@P2@about/index.html#about-business">ガス管取替後の復旧舗装工事</a></li>
      <li><a href="@P2@about/index.html#about-business">水道工事</a></li>
      <li><a href="@P2@about/index.html#about-business">一般土木工事</a></li>
      <li><a href="@P2@about/index.html#about-business">下水道工事</a></li>
    </ul></div>
  </div>
</section>

<!-- 02 OUR STORY #top-story｜方式B：CMS 54 Half -->
<section class="section" id="top-story" aria-labelledby="story-title" data-cms-id="54" data-implementation="B">
  <div class="wrap half reveal" style="grid-template-columns:1fr 1.1fr">
    <div class="half-copy">
      <p class="section-kicker">OUR STORY <span>会社の歩み</span></p>
      <h2 class="section-title" id="story-title">1974年から、<br>街の日常と向き合ってきた。</h2>
      <p class="p2-year" aria-hidden="true">1974</p>
      <p>世田谷を拠点に、道路の舗装復旧や維持、水道工事に携わってきた久留米興業。半世紀以上の歩みの先にあるのは、これからも街の暮らしを支えていくという仕事です。</p>
      <a class="text-link" href="@P2@about/index.html#about-history">会社の歩みと事業を見る <span aria-hidden="true">→</span></a>
    </div>
    <div class="half-media"><img src="{P}entrance-sunny.jpg" alt="「(株)久留米興業」の看板が掲げられた現在の本社入口" loading="lazy" width="941" height="705"><p class="caption">現在の本社（東京都世田谷区北烏山）</p></div>
  </div>
</section>

<!-- 03 THE PEOPLE BEHIND CHANGE #top-leader｜方式B：CMS 54 Half ＋ 35 Title Sub -->
<section class="section bg-soft" id="top-leader" aria-labelledby="leader-title" data-cms-id="54,35" data-implementation="B">
  <div class="wrap half reveal" style="grid-template-columns:.9fr 1.1fr">
    <div class="half-media is-portrait"><img src="{P}ceo-portrait.jpg" alt="代表取締役 川島 和範" loading="lazy" width="502" height="627"><p class="caption">代表取締役　川島 和範</p></div>
    <div class="half-copy gate" data-gate="代表の経歴は代表インタビューの再構成原稿：本人確認待ち">
      <p class="section-kicker">THE PEOPLE BEHIND CHANGE <span>代表の歩み</span></p>
      <h2 class="section-title" id="leader-title">「何のために働くのか」を、<br>考えたことがあるから。</h2>
      <p>18歳で現場に入り、24歳で一度会社を離れた川島代表。現場・管理・経営を経験し、今は働く時間や人の負担にも目を向けながら、次の世代へつながる会社づくりを考えています。</p>
      <div class="cta-row"><a class="btn btn-dark" href="@P2@about/index.html#about-representative">川島代表の歩みと想い <span aria-hidden="true">→</span></a><a class="text-link" href="@P2@people/index.html#people-president">代表と働く人を知る <span aria-hidden="true">→</span></a></div>
    </div>
  </div>
</section>

<!-- 04 CHANGES IN PRACTICE #top-change｜方式B：CMS 42 Card Three ＋ CSS（淡いネイビー背景・装飾数字） -->
<section class="section p2-tint" id="top-change" aria-labelledby="change-title" data-cms-id="42" data-implementation="B">
  <div class="wrap">
    <div class="section-heading section-heading-split reveal"><div><p class="section-kicker">CHANGES IN PRACTICE <span>働き方の見直し</span></p><h2 class="section-title" id="change-title">守るために、<br>変えるという選択。</h2></div><p class="section-heading-desc">昔からのやり方を続けるだけでは、働く人も仕事も守り続けられない。久留米興業では、現場の経験を持つ代表が、働き方の見直しに向き合ってきました。</p></div>
    <div class="card-grid is-3 p2-num-cards">
      <article class="info-card reveal"><span class="p2-bignum" aria-hidden="true">01</span><h3>勤務時間を見直す</h3><p>定時を意識し、残業時間を管理することから働き方を見直してきました。</p></article>
      <article class="info-card is-blue reveal" data-delay="1"><span class="p2-bignum" aria-hidden="true">02</span><h3>現場の負担を分け合う</h3><p>一人だけに無理を集中させず、人員の配置にも目を向けています。</p></article>
      <article class="info-card reveal" data-delay="2"><span class="p2-bignum" aria-hidden="true">03</span><h3>個性を同じ型にはめない</h3><p>得意なことや仕事の進め方が違っても、同じ目標へ進める関係を大切にしています。</p></article>
    </div>
    <p class="p2-honest reveal">これは代表の取り組みと方針です。現場には今も忙しい日や体力的な負担があり、その実際は採用情報の「仕事のリアル」でお伝えしています。</p>
    <div class="cta-row reveal"><a class="btn btn-dark" href="@P2@about/index.html#about-change">変化の理由と現在を知る <span aria-hidden="true">→</span></a><a class="text-link" href="@P2@future/index.html#future-workstyle">これからの課題を見る <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<!-- 05 OUR BUSINESS #top-work｜方式B：CMS 16 Card Four ＋ CSS -->
<section class="section business-section" id="top-work" aria-labelledby="work-title" data-cms-id="16" data-implementation="B">
  <div class="wrap">
    <div class="section-heading section-heading-split reveal"><div><p class="section-kicker">OUR BUSINESS <span>事業</span></p><h2 class="section-title" id="work-title">社会に必要な工事を、<br>毎日の現場で。</h2></div><p class="section-heading-desc">道路を元の状態に戻し、地域の水道・下水道や土木の仕事に携わる。仕事の形は異なっても、その先には利用する人の生活があります。</p></div>
    <div class="business-grid">
      <a class="business-card reveal" href="@P2@about/index.html#about-business"><div class="business-image"><img src="{P}paving-roller.jpg" alt="ローラーで舗装を転圧している現場" loading="lazy"><span>01</span></div><div class="business-card-body"><h3>ガス管取替後の<br>復旧舗装工事</h3><p>ガス管取替後の道路を舗装復旧する工事。</p></div></a>
      <a class="business-card reveal" href="@P2@about/index.html#about-business" data-delay="1"><div class="business-image"><img src="{P}water-pipe.jpg" alt="掘削した溝に水道管を布設している現場" loading="lazy"><span>02</span></div><div class="business-card-body"><h3>水道工事</h3><p>水道管の布設・布設替など、供給基盤に関わる工事。</p></div></a>
      <a class="business-card reveal" href="@P2@about/index.html#about-business" data-delay="2"><div class="business-image"><img src="{P}civil-road.jpg" alt="カラー舗装で仕上げた道路" loading="lazy"><span>03</span></div><div class="business-card-body"><h3>一般土木工事</h3><p>道路の維持・改良など、地域の土木工事。</p></div></a>
      <a class="business-card reveal" href="@P2@about/index.html#about-business" data-delay="3"><div class="business-image"><div class="pattern-art" style="height:100%;aspect-ratio:auto"><span>SEWERAGE</span></div><span>04</span></div><div class="business-card-body"><h3>下水道工事</h3><p>下水道整備など、生活基盤に関わる工事。</p></div></a>
    </div>
    <p class="p2-honest reveal">このほか、自治体からの要請に応じた雪かきや土嚢作成などにも対応しています。</p>
    <p class="review-note">事業名は構成①と同じ正式な4分類にそろえました。下水道工事と確認できる写真が届くまでは、写真ではない図柄で表示しています。</p>
    <div class="section-footer reveal"><a class="btn btn-dark" href="@P2@about/index.html#about-business">久留米興業の仕事を知る <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<!-- 06 REAL VOICES #top-voices｜方式B：CMS 42 Card Three（営業）＋ 787 Text Two（現場）。5人を1つのSectionに詰めず分割 -->
<section class="section bg-soft" id="top-voices" aria-labelledby="voices-title" data-cms-id="42,787" data-implementation="B">
  <div class="wrap">
    <div class="section-heading section-heading-split reveal"><div><p class="section-kicker">REAL VOICES <span>社員の声</span></p><h2 class="section-title" id="voices-title">どんな人が働いているのか。<br>答えは、社員の言葉にある。</h2></div><p class="section-heading-desc">同じ会社でも、入社のきっかけや仕事の覚え方は人それぞれ。営業と現場、実際に働く人の経験から、久留米興業の姿を見てください。</p></div>
    <p class="p2-group-label reveal">営業職</p>
    <div class="card-grid is-3 p2-voice-grid">
      <a class="link-card reveal" href="{BLOG_NEGISHI}" target="_blank" rel="noopener noreferrer"><div class="lc-media p2-portrait"><img src="{P}member-n.jpg" alt="営業職の根岸さん" loading="lazy"></div><div class="lc-body"><small>SALES｜根岸さん</small><h3>異業種から現場代理人へ</h3><p>お茶の営業から転職し、公共工事の現場調整と資格取得へ。</p><span class="mini-link">インタビュー全文を読む <b aria-hidden="true">↗</b></span></div><span class="sr-only">（外部サイトが開きます）</span></a>
      <a class="link-card reveal" href="{BLOG_TAKAHATA}" target="_blank" rel="noopener noreferrer" data-delay="1"><div class="lc-media p2-portrait"><img src="{P}member-t2.jpg" alt="営業職の高畑さん" loading="lazy"></div><div class="lc-body"><small>SALES｜高畑さん</small><h3>新卒から営業を経験</h3><p>業界用語も分からない時期に先輩の支えを受け、仕事を覚えてきた。</p><span class="mini-link">インタビュー全文を読む <b aria-hidden="true">↗</b></span></div><span class="sr-only">（外部サイトが開きます）</span></a>
      <a class="link-card reveal" href="{BLOG_IMAI}" target="_blank" rel="noopener noreferrer" data-delay="2"><div class="lc-media p2-portrait"><img src="{P}member-i2.jpg" alt="営業職の今井さん" loading="lazy"></div><div class="lc-body"><small>SALES｜今井さん</small><h3>広告業界から転職</h3><p>現場での衝突を経験し、職人との対話を通じて調整力を磨いた。</p><span class="mini-link">インタビュー全文を読む <b aria-hidden="true">↗</b></span></div><span class="sr-only">（外部サイトが開きます）</span></a>
    </div>
    <p class="p2-group-label reveal">現場職</p>
    <div class="text-two p2-duo reveal">
      <article class="p2-duo-card"><small>FIELD｜班長</small><h3>松野さん</h3><p>長年の現場経験から、役割分担と新人の成長について話しています。</p></article>
      <article class="p2-duo-card"><small>FIELD｜現場職</small><h3>奥居さん</h3><p>建築から土木へ。先輩に聞きながら仕事を覚え、現場の大変さも率直に話しています。</p></article>
    </div>
    <p class="review-note">松野さん・奥居さんの本人写真は対談資料に含まれていないため、名前と役割の文字カードで表示しています。写真が提供されたら差し替えます。</p>
    <div class="cta-row reveal"><a class="btn btn-dark" href="@P2@recruit/index.html#recruit-voices">社員の実話から仕事を知る <span aria-hidden="true">→</span></a>{ext(BLOG_LIST, '公開中の営業社員インタビュー <span aria-hidden="true">↗</span>', 'text-link')}</div>
  </div>
</section>

<!-- 07 FOR THE NEXT 50 YEARS #top-next｜方式B：CMS 80 H2 Text ＋ 54 Half（ネイビーを部分的に使用） -->
<section class="section navy-band" id="top-next" aria-labelledby="next-title" data-cms-id="80,54" data-implementation="B">
  <div class="wrap half reveal is-rev" style="grid-template-columns:1fr 1fr">
    <div class="half-copy">
      <p class="section-kicker section-kicker-light">FOR THE NEXT 50 YEARS <span>これから</span></p>
      <h2 class="section-title" id="next-title">仕事が続くために、<br>人が育つ会社でありたい。</h2>
      <p>これからも街のインフラを守っていくには、次の世代へ経験や技術を渡していく必要があります。未完成なところも見直しながら、人が長く働ける会社を目指しています。</p>
      <a class="text-link text-link-light" href="@P2@future/index.html">久留米興業の未来を見る <span aria-hidden="true">→</span></a>
    </div>
    <div class="half-media"><img src="{P}field-team-back.jpg" alt="歩道の工事で、それぞれの持ち場で作業する現場職" loading="lazy" width="941" height="627"></div>
  </div>
</section>

<!-- 08 JOIN OUR TEAM #top-recruit｜方式B：CMS 787 Two Text ＋ 54 Half、2列CTA -->
<section class="section" id="top-recruit" aria-labelledby="recruit-title" data-cms-id="787,54" data-implementation="B">
  <div class="wrap">
    <div class="section-heading section-heading-split reveal"><div><p class="section-kicker">JOIN OUR TEAM <span>採用情報</span></p><h2 class="section-title" id="recruit-title">仕事の中身も、大変さも<br>知ってから選んでほしい。</h2></div><p class="section-heading-desc">取引先と現場をつなぐ営業職。現場で手を動かし、街を整える現場職。仕事の種類も、最初に覚えることも違います。入社後を想像できるよう、実際の情報をご案内します。</p></div>
    <div class="card-grid is-2">
      <a class="link-card reveal" href="@P2@recruit/index.html#recruit-role-sales"><div class="lc-media"><img src="{P}office-pc.jpg" alt="事務所で資料を確認する社員" loading="lazy"></div><div class="lc-body"><small>SALES</small><h3>営業職｜人と現場をつなぐ仕事</h3><p>相談・見積・段取り・現場との連携。</p><span class="mini-link">営業職の仕事を見る <b aria-hidden="true">→</b></span></div></a>
      <a class="link-card reveal" href="@P2@recruit/index.html#recruit-role-field" data-delay="1"><div class="lc-media"><img src="{P}field-worker-helmet.jpg" alt="ヘルメットをかぶって作業する現場職" loading="lazy"></div><div class="lc-body"><small>FIELD WORK</small><h3>現場職｜仲間とつくる仕事</h3><p>現場の流れを学び、安全を守りながら施工に携わる。</p><span class="mini-link">現場職の仕事を見る <b aria-hidden="true">→</b></span></div></a>
    </div>
    <div class="section-footer reveal"><a class="btn btn-dark" href="@P2@recruit/index.html#recruit-offerings">待遇・募集要項を確認する <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<!-- 09 WORKS & NEWS #top-workproof｜方式A/B：CMS 718 Portfolio ＋ 101 Blog（連動不可なら手動カード） -->
<section class="section bg-soft" id="top-workproof" aria-labelledby="proof-title" data-cms-id="718,101" data-implementation="A/B">
  <div class="wrap">
    <div class="section-heading section-heading-split reveal"><div><p class="section-kicker">WORKS &amp; NEWS <span>実際の仕事</span></p><h2 class="section-title" id="proof-title">言葉の先にある、<br>実際の仕事。</h2></div><p class="section-heading-desc">現場の写真や会社の活動にも、久留米興業の日常が表れています。施工の様子と、地域に関わる取り組みをご紹介します。</p></div>
    <div class="p2-proof">
      <a class="p2-proof-photo reveal" href="{OFFICIAL_WORKS}" target="_blank" rel="noopener noreferrer"><img src="{P}work-kamisoshigaya.jpg" alt="歩道の舗装を終えた現場と工事黒板" loading="lazy"><span>施工の様子</span><span class="sr-only">（外部サイトが開きます）</span></a>
      <a class="p2-proof-photo reveal" href="{OFFICIAL_WORKS}" target="_blank" rel="noopener noreferrer" data-delay="1"><img src="{P}work-chisaki.jpg" alt="新しく舗装した生活道路と工事黒板" loading="lazy"><span>施工の様子</span><span class="sr-only">（外部サイトが開きます）</span></a>
      <a class="p2-proof-news reveal" href="{DISASTER}" target="_blank" rel="noopener noreferrer" data-delay="2"><time datetime="2024-03-08">2024.03.08</time><small>会社の活動</small><h3>令和6年度能登半島地震に伴う災害救援隊について</h3><span class="mini-link">記事を読む <b aria-hidden="true">↗</b></span><span class="sr-only">（外部サイトが開きます）</span></a>
    </div>
    <div class="cta-row reveal">{ext(OFFICIAL_WORKS, '実際の施工を見る <span aria-hidden="true">↗</span>', 'btn btn-dark')}{ext(OFFICIAL_NEWS, '企業の取り組みを見る <span aria-hidden="true">↗</span>', 'text-link')}</div>
  </div>
</section>

<!-- 10 LAST CTA #top-footer｜方式B：CMS 90 Btn Text ＋ 23 Btn -->
<section class="contact-section" id="top-footer" aria-labelledby="last-title" data-cms-id="90,23" data-implementation="B"><div class="wrap contact-layout reveal"><div><p class="section-kicker section-kicker-light">NEXT STEP</p><h2 id="last-title">久留米興業を、<br>もう少し知ってみませんか。</h2><p>仕事のこと、会社の歩み、実際に働く人のこと。<br>気になるところから、詳しく見ていただけます。</p></div><div class="contact-links"><a href="@P2@about/index.html">会社の歩みと想いを知る <span aria-hidden="true">→</span></a><a href="@P2@people/index.html">働く人の声を読む <span aria-hidden="true">→</span></a><a href="@P2@recruit/index.html">募集・働き方を知る <span aria-hidden="true">→</span></a></div></div></section>
'''


def build():
    return p2_page("top", "株式会社久留米興業｜この街とともに、50年以上。働き方も、未来も、変えていく。",
                   "この街とともに、50年以上。道路を直し、水道を支える久留米興業が、守ってきたものと変えようとしていることをご紹介します。",
                   1, BODY)

from p2common import *

P = "@R@assets/photos/"

BODY = f'''
<!-- 01 ABOUT HERO #about-hero｜方式B：CMS 734 H1 Center ＋ CSS -->
<section class="page-hero" id="about-hero" aria-labelledby="about-title" data-cms-id="734" data-implementation="B" data-mark="ABOUT">
  <div class="page-hero-img" style="background-image:url('{P}field-sidewalk.jpg');background-position:60% 55%" role="img" aria-label="歩道の工事を進める現場職"></div>
  <div class="wrap">
    <p class="eyebrow anim-enter"><span class="line"></span>ABOUT KURUME KOGYO</p>
    <h1 id="about-title" class="anim-enter" style="--delay:.1s">守ってきたもの。<br>変えていくもの。</h1>
    <p class="lead anim-enter" style="--delay:.2s">1974年の設立から、道路や水道など、街の日常に関わる仕事を続けてきた久留米興業。長く続けてきたからこそ、守るものと変えるものがある。これまでの歩みと、これからの会社づくりをご紹介します。</p>
  </div>
</section>
<!--CRUMB-->

<!-- 02 HISTORY #about-history｜方式B：CMS 761 Flow Cards ＋ 54 Half -->
<section class="section" id="about-history" aria-labelledby="history-title" data-cms-id="761,54" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker">OUR JOURNEY <span>会社の歩み</span></p><h2 class="section-title" id="history-title">この街の仕事とともに、<br>半世紀以上。</h2></div>
      <div class="body"><p>世田谷を拠点に、道路の舗装復旧や維持、水道管工事など、街の暮らしを支える仕事に携わってきました。</p></div>
    </div>
    <figure class="p2-shot reveal"><img src="{P}yard-overhead.jpg" alt="重機と資材が並ぶ北烏山の資材置き場" loading="lazy" width="1600" height="1066"></figure>
    <ol class="p2-timeline reveal">
      <li><span class="when">1974</span><div><h3>株式会社久留米興業 設立</h3><p>3月4日設立。世田谷区北烏山を拠点に事業を始める。</p></div></li>
      <li><span class="when">これまで</span><div><h3>道路・水道などの工事を続ける</h3><p>ガス管取替後の復旧舗装、路面の改良・維持、水道管の布設など、街の暮らしに関わる工事に携わってきました。</p></div></li>
      <li class="is-sub"><span class="when">2018</span><div><h3>関連会社 KRM株式会社 設立</h3><p>同じ敷地内に、道路工事に使う資材の販売や受け入れを行う関連会社を設立。</p></div></li>
      <li><span class="when">2024</span><div><h3>能登半島地震に伴う災害救援活動</h3><p>被災地での救援活動に参加しました。{ext(DISASTER, '当時のお知らせを読む ↗', 'inline-link')}</p></div></li>
      <li class="is-next"><span class="when">これから</span><div><h3>事業の継承と働き方の見直し</h3><p>仕事を次の世代へ渡していくために、働き方や教え方を見直し続けていきます。</p></div></li>
    </ol>
    <p class="review-note">2024年の救援活動は、派遣期間・規模・担当内容を元記事と照合してから詳しい説明を追加します。</p>
    <p class="p2-closing reveal">施工する人、取引先、地域の方々との関係。その積み重ねを、次の世代へ渡していきます。</p>
  </div>
</section>

<!-- 03 REPRESENTATIVE #about-representative｜方式B：CMS 54 Half ＋ 761 Flow Cards -->
<section class="section bg-soft" id="about-representative" aria-labelledby="rep-title" data-cms-id="54,43,761" data-implementation="B">
  <div class="wrap">
    <div class="half reveal" style="grid-template-columns:1fr 1fr">
      <div class="half-media"><img src="{P}ceo-desk.jpg" alt="応接スペースで話す代表取締役 川島 和範" loading="lazy" width="941" height="627"><p class="caption">代表取締役　川島 和範</p></div>
      <div class="half-copy gate" data-gate="代表インタビューを編集した三人称原稿：本人確認待ち">
        <p class="section-kicker">REPRESENTATIVE'S JOURNEY <span>川島代表の歩み</span></p>
        <h2 class="section-title" id="rep-title">働く意味を考え直した経験が、<br>今の会社づくりの原点に。</h2>
        <p>川島代表が久留米興業に入社したのは18歳のとき。現場の見習いから始まり、仕事の厳しさも経験しました。24歳で一度会社を離れ、その後戻って現場の仕事を重ね、30代で管理や取引先との仕事を任されるようになりました。40代で代表に就任し、立場が変わるごとに、見える景色も変わっていきました。</p>
        <p>かつては働く時間の長さに悩み、仕事を離れた時期があったからこそ、働く人にとって仕事だけが人生のすべてではないという考えを持っています。今は、仕事の責任を果たしながら、家族や自分の時間も大切にできる会社を目指しています。</p>
      </div>
    </div>
    <ol class="flow is-4 reveal" style="margin-top:56px">
      <li><span class="num">18歳</span><h3>現場から出発</h3><p>土木の経験がないところから仕事を覚え始める。</p></li>
      <li><span class="num">24歳</span><h3>一度立ち止まる</h3><p>働き方に迷い、会社を離れる経験をする。</p></li>
      <li><span class="num">30代</span><h3>現場の外も知る</h3><p>再入社後、現場の仕事に加えて管理や取引先との関係を学ぶ。</p></li>
      <li><span class="num">40代〜</span><h3>会社と働く人を考える</h3><p>代表として時間管理や人材育成、取引先との関係を見直す。</p></li>
    </ol>
  </div>
</section>

<!-- 04 THE CHANGE #about-change｜方式B：CMS 42 Card Three ＋ 54 Half -->
<section class="section" id="about-change" aria-labelledby="change-title" data-cms-id="42,54" data-implementation="B">
  <div class="wrap">
    <div class="half reveal" style="grid-template-columns:1.1fr .9fr">
      <div class="half-copy">
        <p class="section-kicker">CHANGE IN PRACTICE <span>働き方の見直し</span></p>
        <h2 class="section-title" id="change-title">変えたいと思うだけでは、<br>会社は変わらない。</h2>
        <p>川島代表は、現場で経験した働き方を当然とせず、会社としての時間管理や人員配置を見直してきました。一方、現場の仕事には現在も忙しい日や体力的な負担があります。だからこそ、今も考え続ける必要があります。</p>
      </div>
      <div class="half-media"><img src="{P}process-remove.jpg" alt="重機で古い舗装を撤去している現場" loading="lazy" width="1046" height="698"></div>
    </div>
    <div class="card-grid is-3" style="margin-top:48px">
      <article class="info-card reveal"><small>管理</small><h3>働く時間の管理に向き合う</h3><p>36協定を含めた残業のルールを見直し、定時で帰ることを意識した働き方へ。</p></article>
      <article class="info-card is-blue reveal" data-delay="1"><small>負担</small><h3>一人ひとりの負担を軽くする</h3><p>現場作業を減らせない場面では、人員を増やして負担を分けるという考え方に取り組んできました。</p></article>
      <article class="info-card reveal" data-delay="2"><small>現状</small><h3>変化の途中にある現場</h3><p>現場の松野さん・奥居さんは、忙しさや休憩の取りにくさも率直に語っています。実態に目を向け、改善を続けることが重要です。</p></article>
    </div>
    <p class="p2-honest reveal">どの職種でも、毎日同じ働き方になるわけではありません。道路の現場は、天候や工事内容、夜間作業などに左右されます。社員の声も参考にしながら、仕事内容を理解していただきたいと考えています。</p>
    <div class="cta-row reveal"><a class="btn btn-dark" href="@P2@recruit/index.html#recruit-reality">営業・現場の仕事のリアルを見る <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<!-- 05 WHAT WE VALUE #about-values｜方式B：CMS 43 Title All ＋ 42 Card Three。正式な経営理念ではなく編集案 -->
<section class="section p2-tint" id="about-values" aria-labelledby="values-title" data-cms-id="43,42" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker">WHAT WE VALUE <span>大切にしたいこと</span></p><h2 class="section-title" id="values-title">私たちが、<br>大切にしたいこと。</h2></div>
      <div class="body"><p>久留米興業の仕事をつないできたのは、現場の技術だけではありません。取引先や地域の方、そして一緒に働く人との関わりを大切にしながら、これからも必要とされる会社を目指します。</p></div>
    </div>
    <div class="p2-values gate" data-gate="代表の発言から編集した価値観の案：正式な経営理念ではありません。会社承認待ち">
      <div class="p2-values-media reveal"><img src="{P}office.jpg" alt="事務所で打ち合わせをする社員たち" loading="lazy" width="1046" height="698"></div>
      <div class="card-grid is-3 p2-line-cards">
        <article class="info-card reveal"><small>01</small><h3>人とのつながりを大切にする。</h3><p>現場と事務所、取引先や地域の方々。その関係があってこそ、仕事は前に進んでいきます。</p></article>
        <article class="info-card reveal" data-delay="1"><small>02</small><h3>自分で考え、周りと仕事をつくる。</h3><p>経験や考え方が違っても、自分の役割を考え、必要なときは助け合う姿勢を大切にしています。</p></article>
        <article class="info-card reveal" data-delay="2"><small>03</small><h3>これからも、変わり続ける。</h3><p>長く続いてきたやり方も、今の働く人に合わなければ見直す。その積み重ねを次の世代につなぎます。</p></article>
      </div>
    </div>
  </div>
</section>

<!-- 06 WHAT WE DO #about-business｜方式B：CMS 16 Card Four ＋ 54 Half -->
<section class="section business-section" id="about-business" aria-labelledby="biz-title" data-cms-id="16,54" data-implementation="B">
  <div class="wrap">
    <div class="section-heading section-heading-split reveal"><div><p class="section-kicker">WHAT WE DO <span>事業内容</span></p><h2 class="section-title" id="biz-title">暮らしが止まらないように、<br>今日も現場が動く。</h2></div><p class="section-heading-desc">道路を通れること、水が届くこと。いつもの日常を支えるために、久留米興業は舗装や水道などの工事に取り組んでいます。工事を支えるのは、現場の技術と、準備や段取りをする人たちの連携です。</p></div>
    <div class="business-grid">
      <div class="business-card reveal"><div class="business-image"><img src="{P}work-minamikarasuyama.jpg" alt="舗装を仕上げた道路と工事黒板" loading="lazy"><span>01</span></div><div class="business-card-body"><h3>ガス管取替後の<br>復旧舗装工事</h3><p>ガス管の工事後、道路を舗装し直して街の交通を支える。</p></div></div>
      <div class="business-card reveal" data-delay="1"><div class="business-image"><img src="{P}water-valve.jpg" alt="掘削した地中に設置された水道の設備" loading="lazy"><span>02</span></div><div class="business-card-body"><h3>水道工事</h3><p>水道管の布設・布設替など、日々の暮らしの基盤を支える。</p></div></div>
      <div class="business-card reveal" data-delay="2"><div class="business-image"><img src="{P}road-line.jpg" alt="白線が引かれた整備後の道路" loading="lazy"><span>03</span></div><div class="business-card-body"><h3>一般土木工事</h3><p>道路の改良・維持など、安全に使える環境を守る。</p></div></div>
      <div class="business-card reveal" data-delay="3"><div class="business-image"><div class="pattern-art" style="height:100%;aspect-ratio:auto"><span>SEWERAGE</span></div><span>04</span></div><div class="business-card-body"><h3>下水道工事</h3><p>下水道の整備など、生活環境を支える工事。</p></div></div>
    </div>
    <p class="p2-honest reveal">このほか、自治体からの要請に応じた雪かきや土嚢作成など、地域で必要とされる対応にも取り組んでいます。</p>
    <div class="p2-column reveal"><p class="p2-column-label">工事を支える連携</p><p>工事の前には、依頼内容の確認や見積、必要な人・材料・日程の調整があります。現場では安全を確かめながら、それぞれの担当が作業を進めます。営業と現場、どちらか一方だけでは完成しない仕事です。</p><a class="text-link" href="@P2@recruit/index.html#recruit-roles">営業・現場それぞれの役割を知る <span aria-hidden="true">→</span></a></div>
    <div class="cta-row reveal" style="display:flex;flex-wrap:wrap;gap:12px 24px;margin-top:28px">{ext(OFFICIAL_CONTACT, "工事・事業のお問い合わせフォーム <span aria-hidden=\"true\">↗</span>", "btn btn-dark")}<a class="text-link" href="@P2@company/index.html#company-contact">会社情報・連絡先 <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<!-- 07 HOW WE WORK #about-workstyle｜方式B：CMS 54 Half ＋ 787 Two Text -->
<section class="section bg-soft" id="about-workstyle" aria-labelledby="attitude-title" data-cms-id="54,787" data-implementation="B">
  <div class="wrap">
    <div class="half reveal" style="grid-template-columns:1fr 1fr">
      <div class="half-copy">
        <p class="section-kicker">HOW WE WORK <span>仕事への考え方</span></p>
        <h2 class="section-title" id="attitude-title">工事を終えるだけでは、<br>仕事は終わらない。</h2>
        <p>現場を取り巻くのは、工事に関わる人だけではありません。その道を使う人、近くに住む人、仕事を依頼する人がいます。地域の理解や協力があってこそ施工ができるからこそ、久留米興業は仕事の先にいる人との関係も大切にしています。</p>
      </div>
      <div class="half-media"><img src="{P}work-kyuden.jpg" alt="住宅地の中で舗装を仕上げた車道" loading="lazy" width="930" height="698"></div>
    </div>
    <div class="card-grid is-3" style="margin-top:44px">
      <article class="info-card reveal"><small>01</small><h3>取引先への向き合い方</h3><p>必要な工事を任せてもらえるように、依頼された一つひとつの仕事と関係づくりに向き合う。</p></article>
      <article class="info-card reveal" data-delay="1"><small>02</small><h3>現場での役割分担</h3><p>班長・作業員がそれぞれの役割を担い、必要なときは声を掛け合って1日の仕事を完成させる。</p></article>
      <article class="info-card reveal" data-delay="2"><small>03</small><h3>地域と共存する姿勢</h3><p>騒音や通行の影響もある仕事だからこそ、現場の外にいる人にも配慮する。</p></article>
    </div>
    <div class="p2-column reveal gate" data-gate="代表インタビュー時点の例：現在の実施状況を確認してから公開"><p class="p2-column-label">地域との関わり</p><p>川島代表は、地域の行事で協力を求められたときに協賛したり、余ったインターロッキングブロックを必要な方へ譲ったりしてきたと話しています。大きな活動だけが地域への関わりではないという考えです。</p></div>
  </div>
</section>

<!-- 08 THE NEXT 50 YEARS #about-next｜方式B：CMS 80 H2 Text ＋ 54 Half（濃紺の1セクション＋横長写真） -->
<section class="section navy-band" id="about-next" aria-labelledby="next-title" data-cms-id="80,54" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker section-kicker-light">THE NEXT 50 YEARS <span>次の50年へ</span></p><h2 class="section-title" id="next-title">これからも仕事が続くために、<br>働く人へ目を向ける。</h2></div>
      <div class="body"><p>社会インフラの維持には、これからも現場で働く人の力が必要です。今ある仕事や技術を、次に入ってくる人へどう渡していくか。教育に十分な時間を取れない日もあるからこそ、教える仕組みも、働き方も少しずつ整えていきたいと考えています。</p><p class="p2-emph">完成された会社ではなく、次の世代とともに変わっていく会社へ。</p></div>
    </div>
    <div class="p2-wide reveal"><img src="{P}excavator.jpg" alt="現場で待機する久留米興業の油圧ショベル" loading="lazy" width="927" height="618"></div>
    <div class="cta-row reveal"><a class="btn btn-white" href="@P2@recruit/index.html">この会社で働くことを知る <span aria-hidden="true">→</span></a><a class="text-link text-link-light" href="@P2@future/index.html">久留米興業の未来を見る <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<!-- 09 CTA #about-cta｜方式B：CMS 90 Btn Text ＋ 23 Btn -->
<section class="contact-section" id="about-cta" aria-labelledby="acta-title" data-cms-id="90,23" data-implementation="B"><div class="wrap contact-layout reveal"><div><p class="section-kicker section-kicker-light">NEXT</p><h2 id="acta-title">言葉だけでなく、<br>働く人の声も見てください。</h2><p>代表が考える会社の未来と、日々現場で働く社員の実感。その両方を知ったうえで、久留米興業が自分に合う会社か考えていただけたらと思います。</p></div><div class="contact-links"><a href="@P2@recruit/index.html#recruit-voices">採用情報・社員の声を見る <span aria-hidden="true">→</span></a><a href="@P2@recruit/index.html#recruit-offerings">募集条件を確認する <span aria-hidden="true">→</span></a><a href="@P2@index.html">TOPへ戻る <span aria-hidden="true">→</span></a></div></div></section>
'''


def build():
    return p2_page("about", "久留米興業について｜株式会社久留米興業",
                   "守ってきたもの。変えていくもの。久留米興業の歩み、代表の経験、働き方の見直し、事業と仕事への考え方をご紹介します。",
                   2, BODY, crumb="久留米興業について")

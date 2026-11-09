# -*- coding: utf-8 -*-
"""パターン②（ビジョン → 採用／参考：GTN 採用サイト）の TOP 本文。
軸になる仕掛け：紺の大きな曲面（宣言文を載せる）＋ 巨大な英字。写真は面と曲線で切り分ける。
流れ：宣言（ビジョン）→ 入口（職種・募集要項）→ 会社 → 代表 → 働き方の見直し → 人 → これから → 実際の仕事 → JOIN US。
HTMLは CMS の section（data-cms-id）をそのまま置き、見た目は assets/n/p2*.css、動きは assets/n/n.js。
@R@ はサイトのルート、@P2@ はパターン②TOPへの相対パス（p2common.p2_page が置換）。"""
from common import OFFICIAL_WORKS, OFFICIAL_NEWS, DISASTER, BLOG_NEGISHI, BLOG_TAKAHATA, BLOG_IMAI, BLOG_LIST

P = "@R@assets/photos/"
X = ' target="_blank" rel="noopener noreferrer"'
XS = '<span class="sr-only">（外部サイトが開きます）</span>'


def head(en, ja, hid, light=False):
    return f'<h2 class="m-h2{" is-light" if light else ""}" id="{hid}"><span class="m-en">{en}</span><span class="m-ja">{ja}</span></h2>'


def body():
    return f'''
<!-- 01 MAIN VISUAL｜CMS 721 Mainvisual（写真1枚）＋ 734（キャッチ）。英字は飾り（読み上げない）。CTAなし -->
<section class="m-mv" aria-labelledby="h1" data-cms-id="721,734">
  <figure class="m-mv-photo"><img src="{P}field-work-street.jpg" alt="重機とともに歩道の路盤をつくる施工中の現場" width="1600" height="1066" fetchpriority="high"></figure>
  <p class="m-mv-word" aria-hidden="true"><span>KEEP</span><span>&amp; CHANGE</span></p>
  <div class="m-mv-copy">
    <h1 id="h1"><span class="ln">守るために、</span><span class="ln">変えていく。</span></h1>
    <p>この街とともに、50年以上。<br>道路を直し、水道を支える会社の、これから。</p>
  </div>
</section>

<!-- 02 MANIFESTO｜CMS 80 H2 Text（紺の曲面に宣言文）＋ 右に考え方へのリンク -->
<section class="m-manifesto" aria-labelledby="mani-title" data-cms-id="80">
  <div class="wrap m-mani-grid">
    <div class="m-mani-text">
      <h2 id="mani-title" class="sr-only">久留米興業の考え方</h2>
      <p>1974年から、世田谷の道路と水道の工事に携わってきた。<br>ガス管を取り替えた後の道路を、元の状態に戻す。<br>水道管を布設し、地域の土木を担う。<br>その先には、毎日この道を使う人の暮らしがある。</p>
      <p>けれど、昔のやり方のままでは、<br>働く人も、仕事も守れない。</p>
      <p>だから、勤務時間を見直し、現場の負担を分け合い、<br>個性を同じ型にはめない会社へ。</p>
      <p class="m-mani-last">仕事が続くために、人が育つ会社でありたい。<br>守るために、変えていく。</p>
    </div>
    <ul class="m-mani-links">
      <li><a href="@P2@about/index.html#about-representative"><span>MESSAGE</span><small>代表の歩みと想い</small></a></li>
      <li><a href="@P2@about/index.html#about-change"><span>CHANGE</span><small>変えてきたこと</small></a></li>
      <li><a href="@P2@future/index.html"><span>FUTURE</span><small>これからの会社</small></a></li>
    </ul>
  </div>
  <div class="m-strip" aria-hidden="true">
    <img src="{P}entrance-sunny.jpg" alt="" loading="lazy" width="941" height="705">
    <img src="{P}office-aisle.jpg" alt="" loading="lazy" width="1600" height="1066">
    <img src="{P}crawler-track.jpg" alt="" loading="lazy" width="1600" height="1066">
    <img src="{P}boom-sky.jpg" alt="" loading="lazy" width="1600" height="1066">
  </div>
</section>

<!-- 03 ENTRY｜CMS 42 Card Three（職種と募集要項の入口） -->
<section class="m-sec m-entry" aria-labelledby="entry-title" data-cms-id="42">
  <div class="wrap">
    <h2 class="sr-only" id="entry-title">採用の入口</h2>
    <ul class="m-entry-list">
      <li><a href="@P2@recruit/index.html#recruit-role-sales"><b>営業職</b><small>取引先と現場をつなぐ、見積・調整・手配の仕事。</small><span class="m-entry-media"><img src="{P}office-pc.jpg" alt="事務所で資料を確認する社員" loading="lazy" width="1600" height="1066"><em aria-hidden="true">SALES</em></span></a></li>
      <li><a href="@P2@recruit/index.html#recruit-role-field"><b>現場職</b><small>現場の流れを学び、安全を守りながら施工に携わる。</small><span class="m-entry-media"><img src="{P}field-worker-helmet.jpg" alt="ヘルメットをかぶって作業する現場職" loading="lazy" width="1600" height="1066"><em aria-hidden="true">FIELD</em></span></a></li>
      <li><a href="@P2@recruit/index.html#recruit-offerings"><b>募集要項</b><small>給与・休日・働く時間など、条件を曖昧にせずに。</small><span class="m-entry-media"><img src="{P}excavator-boom-name.jpg" alt="社名の入った重機と資材置き場" loading="lazy" width="1600" height="1066"><em aria-hidden="true">JOBS</em></span></a></li>
    </ul>
  </div>
</section>

<!-- 04 ABOUT US｜CMS 54 Half ＋ 16 Card Four（事業の一覧） -->
<section class="m-sec m-about" aria-labelledby="about-title" data-cms-id="54,16">
  <div class="wrap">
    <div class="m-card-panel">
      <div class="m-about-grid">
        <div>{head("ABOUT US", "私たちについて", "about-title")}
          <p class="m-text">世田谷を拠点に、道路の舗装復旧や維持、水道工事に携わってきた久留米興業。半世紀以上の歩みの先にあるのは、これからも街の暮らしを支えていくという仕事です。</p>
          <a class="m-btn" href="@P2@about/index.html">久留米興業について</a></div>
        <figure class="m-about-photo"><img src="{P}sign-vertical.jpg" alt="「(株)久留米興業」の縦書きの看板" loading="lazy" width="1066" height="1600"></figure>
      </div>
    </div>
    <div class="m-biz">
      {head("BUSINESS", "事業を知る", "biz-title")}
      <ul class="m-biz-list">
        <li><a href="@P2@about/index.html#about-business"><img src="{P}paving-roller.jpg" alt="ローラーで舗装を転圧している現場" loading="lazy" width="1600" height="1066"><b>ガス管取替後の復旧舗装工事</b><small>ガス管取替後の道路を舗装復旧する工事</small></a></li>
        <li><a href="@P2@about/index.html#about-business"><img src="{P}water-pipe.jpg" alt="掘削した溝に水道管を布設している現場" loading="lazy" width="1600" height="1066"><b>水道工事</b><small>水道管の布設・布設替など</small></a></li>
        <li><a href="@P2@about/index.html#about-business"><img src="{P}civil-road.jpg" alt="カラー舗装で仕上げた道路" loading="lazy" width="1600" height="1066"><b>一般土木工事</b><small>道路の維持・改良など、地域の土木工事</small></a></li>
        <li><a href="@P2@about/index.html#about-business"><span class="m-biz-art" aria-hidden="true">04</span><b>下水道工事</b><small>下水道整備など、生活基盤に関わる工事</small></a></li>
      </ul>
    </div>
  </div>
</section>

<!-- 05 THE LEADER｜CMS 54 Half（紺の面と写真を曲線で分ける） -->
<section class="m-sec m-leader" aria-labelledby="leader-title" data-cms-id="54">
  <div class="wrap">
    <div class="m-split">
      <div class="m-split-panel">
        <p class="m-label">THE PEOPLE BEHIND CHANGE</p>
        <h2 id="leader-title">「何のために働くのか」を、<br>考えたことがあるから。</h2>
        <p>18歳で現場に入り、24歳で一度会社を離れた川島代表。現場・管理・経営を経験し、今は働く時間や人の負担にも目を向けながら、次の世代へつながる会社づくりを考えています。</p>
        <a class="m-btn is-light" href="@P2@about/index.html#about-representative">代表の歩みと想い</a>
      </div>
      <figure class="m-split-photo"><img src="{P}ceo-portrait.jpg" alt="代表取締役 川島 和範" loading="lazy" width="502" height="627"><figcaption>代表取締役　川島 和範</figcaption></figure>
    </div>
  </div>
</section>

<!-- 06 CHANGE｜CMS 42 Card Three（働き方の見直し） -->
<section class="m-sec m-change" aria-labelledby="change-title" data-cms-id="42">
  <div class="wrap">
    <div class="m-change-head">{head("CHANGE", "働き方の見直し", "change-title")}<p class="m-text">昔のやり方のままでは、働く人も仕事も守れない。現場を知る代表が、働き方の見直しに向き合ってきました。</p></div>
    <figure class="m-wide"><img src="{P}office-wide-window.jpg" alt="窓際まで机が並ぶ本社の事務所" loading="lazy" width="1600" height="1066"></figure>
    <ol class="m-change-list">
      <li><span>01</span><h3>勤務時間を見直す</h3><p>定時を意識し、残業時間を管理することから働き方を見直してきました。</p></li>
      <li><span>02</span><h3>現場の負担を分け合う</h3><p>一人だけに無理を集中させず、人員の配置にも目を向けています。</p></li>
      <li><span>03</span><h3>個性を同じ型にはめない</h3><p>得意なことや仕事の進め方が違っても、同じ目標へ進める関係を大切にしています。</p></li>
    </ol>
    <p class="m-note">これは代表の取り組みと方針です。現場には今も忙しい日や体力的な負担があり、その実際は採用情報の「仕事のリアル」でお伝えしています。</p>
  </div>
</section>

<!-- 07 PEOPLE｜CMS 42 Card Three（営業）＋ 787 Text Two（現場） -->
<section class="m-sec m-people" aria-labelledby="people-title" data-cms-id="42,787">
  <div class="wrap">
    {head("PEOPLE", "社員の声", "people-title", light=True)}
    <p class="m-text is-light">同じ会社でも、入社のきっかけや仕事の覚え方は人それぞれ。営業と現場、実際に働く人の経験から、久留米興業の姿を見てください。</p>
    <ul class="m-people-list">
      <li><a href="{BLOG_NEGISHI}"{X}><img src="{P}member-n.jpg" alt="営業職の根岸さん" loading="lazy" width="800" height="1000"><span class="m-p-body"><small>SALES｜根岸さん</small><b>異業種から現場代理人へ</b><em>お茶の営業から転職し、公共工事の現場調整と資格取得へ。</em><i>インタビューを読む ↗</i></span>{XS}</a></li>
      <li><a href="{BLOG_TAKAHATA}"{X}><img src="{P}member-t2.jpg" alt="営業職の高畑さん" loading="lazy" width="800" height="1000"><span class="m-p-body"><small>SALES｜高畑さん</small><b>新卒から営業を経験</b><em>業界用語も分からない時期に先輩の支えを受け、仕事を覚えてきた。</em><i>インタビューを読む ↗</i></span>{XS}</a></li>
      <li><a href="{BLOG_IMAI}"{X}><img src="{P}member-i2.jpg" alt="営業職の今井さん" loading="lazy" width="800" height="1000"><span class="m-p-body"><small>SALES｜今井さん</small><b>広告業界から転職</b><em>現場での衝突を経験し、職人との対話を通じて調整力を磨いた。</em><i>インタビューを読む ↗</i></span>{XS}</a></li>
    </ul>
    <div class="m-duo">
      <article><small>FIELD｜班長</small><h3>松野さん</h3><p>長年の現場経験から、役割分担と新人の成長について話しています。</p></article>
      <article><small>FIELD｜現場職</small><h3>奥居さん</h3><p>建築から土木へ。先輩に聞きながら仕事を覚え、現場の大変さも率直に話しています。</p></article>
    </div>
    <div class="m-actions"><a class="m-btn is-light" href="@P2@people/index.html">働くスタッフを知る</a></div>
  </div>
</section>

<!-- 08 FUTURE｜CMS 54 Half -->
<section class="m-sec m-future" aria-labelledby="future-title" data-cms-id="54">
  <div class="wrap">
    <div class="m-split is-rev">
      <figure class="m-split-photo"><img src="{P}field-team-back.jpg" alt="歩道の工事で、それぞれの持ち場で作業する現場職" loading="lazy" width="941" height="627"></figure>
      <div class="m-split-panel">
        <p class="m-label">FOR THE NEXT 50 YEARS</p>
        <h2 id="future-title">仕事が続くために、<br>人が育つ会社でありたい。</h2>
        <p>これからも街のインフラを守っていくには、次の世代へ経験や技術を渡していく必要があります。未完成なところも見直しながら、人が長く働ける会社を目指しています。</p>
        <a class="m-btn is-light" href="@P2@future/index.html">久留米興業の未来</a>
      </div>
    </div>
  </div>
</section>

<!-- 09 WORKS & NEWS｜CMS 718 Portfolio ＋ 101 Blog（横に送るカルーセル） -->
<section class="m-sec m-news" aria-labelledby="news-title" data-cms-id="718,101">
  <div class="wrap">
    <div class="m-news-head">{head("WORKS &amp; NEWS", "実際の仕事とお知らせ", "news-title")}<div class="n-ctrl m-ctrl" data-n-ctrl="m-news"><button type="button" class="n-prev" aria-label="前へ">‹</button><button type="button" class="n-next" aria-label="次へ">›</button></div></div>
    <ul class="m-track" id="m-news" data-n-track>
      <li><a href="{OFFICIAL_WORKS}"{X}><span class="m-tag">施工の様子</span><img src="{P}work-kamisoshigaya.jpg" alt="歩道の舗装を終えた現場と工事黒板" loading="lazy" width="1600" height="1066"><b>道路維持工事（世田谷区上祖師谷）</b>{XS}</a></li>
      <li><a href="{OFFICIAL_WORKS}"{X}><span class="m-tag">施工の様子</span><img src="{P}work-chisaki.jpg" alt="新しく舗装した生活道路と工事黒板" loading="lazy" width="1600" height="1066"><b>地先道路築造工事（世田谷区上祖師谷）</b>{XS}</a></li>
      <li><a href="{DISASTER}"{X}><span class="m-tag">会社の活動</span><span class="m-news-txt"><time datetime="2024-03-08">2024.03.08</time>令和6年度能登半島地震に伴う災害救援隊について</span>{XS}</a></li>
      <li><a href="{BLOG_LIST}"{X}><span class="m-tag">記事</span><span class="m-news-txt">公開中の営業社員インタビュー一覧</span>{XS}</a></li>
      <li><a href="{OFFICIAL_NEWS}"{X}><span class="m-tag">お知らせ</span><span class="m-news-txt">お知らせ一覧</span>{XS}</a></li>
    </ul>
    <div class="n-progress m-progress" aria-hidden="true"><i data-n-progress="m-news"></i></div>
  </div>
</section>

<!-- 10 JOIN US｜CMS 90 Btn Text ＋ 23 Btn（集合写真と巨大な英字） -->
<section class="m-join" aria-labelledby="join-title" data-cms-id="90,23">
  <figure class="m-join-photo"><img src="{P}team.jpg" alt="重機の前に並ぶ久留米興業の社員" loading="lazy" width="1600" height="1066"></figure>
  <p class="m-join-word" aria-hidden="true">JOIN US</p>
  <div class="wrap m-join-body">
    <h2 id="join-title">仕事の中身も、大変さも、<br>知ってから選んでほしい。</h2>
    <div class="m-join-links"><a href="@P2@recruit/index.html#recruit-offerings">募集要項を見る</a><a href="@P2@recruit/index.html">採用情報</a><a href="@P2@people/index.html">働くスタッフ</a></div>
  </div>
</section>
'''

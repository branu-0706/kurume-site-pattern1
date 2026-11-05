from common import *

P = "@R@assets/photos/"

BODY = f'''
<!-- 01 COMPANY HERO｜方式B：CMS 734 H1 Center ＋ CSS -->
<section class="page-hero" id="company-hero" aria-labelledby="company-title" data-cms-id="734" data-implementation="B">
  <div class="page-hero-img" style="background-image:url('{P}entrance.jpg');background-position:40% 45%" role="img" aria-label="「(株)久留米興業」の看板が掲げられた本社の敷地入口"></div>
  <div class="wrap">
    <p class="eyebrow anim-enter"><span class="line"></span>COMPANY / ABOUT US</p>
    <h1 id="company-title" class="anim-enter" style="--delay:.1s">この街とともに歩み、<br>次の世代へつないでいく。</h1>
    <p class="lead anim-enter" style="--delay:.2s">1974年の設立以来、世田谷を拠点に道路や水道などのインフラ工事に携わってきた久留米興業。会社の歩み、仕事への考え方、そして現在の事業基盤をご紹介します。</p>
    <div class="hero-actions anim-enter" style="--delay:.3s"><a class="btn btn-white" href="#company-ceo">代表メッセージを読む <span aria-hidden="true">↓</span></a><a class="btn btn-outline-light" href="#company-overview">会社概要を見る <span aria-hidden="true">↓</span></a></div>
  </div>
</section>
<!--CRUMB-->

<!-- 02 MESSAGE FROM PRESIDENT｜方式B：CMS 54 Half ＋ 80 H2 Text ＋ CSS -->
<section class="section" id="company-ceo" aria-labelledby="cceo-title" data-cms-id="54,80" data-implementation="B">
  <div class="wrap half reveal" style="grid-template-columns:.82fr 1fr">
    <div class="half-media is-portrait"><img src="{P}ceo.jpg" alt="代表取締役 川島 和範" loading="lazy"><p class="caption">代表取締役　川島 和範</p></div>
    <div class="half-copy gate" data-gate="公式の代表挨拶を再編集した原稿：本人承認待ち">
      <p class="section-kicker">MESSAGE FROM PRESIDENT <span>代表メッセージ</span></p>
      <h2 class="section-title" id="cceo-title">当たり前の日常を、<br>これからも支えるために。</h2>
      <p>道を歩くこと、車で移動すること、蛇口をひねれば水が出ること。毎日の生活の中では意識することの少ない、こうした日常を支えるのが私たちの仕事です。</p>
      <p>久留米興業は、地域の道路や水道に関わる工事を通じて、街の暮らしとともに歩んできました。大雪の際の除雪や、災害発生時の復旧支援に関わった経験もあります。工事を終えることだけではなく、その先で生活する人たちの安心に仕事をつなげていきたいと考えています。</p>
      <p>長く事業を続けてこられたのは、取引先や協力会社、地域の皆さま、そして日々現場で働く社員とのつながりがあったからこそです。一つひとつの関係に感謝しながら、これからも街に必要とされる会社を目指してまいります。</p>
      <p style="font-weight:700;color:var(--navy);margin-top:22px">代表取締役　川島 和範</p>
      <a class="text-link" href="@R@people/index.html#people-ceo">代表の人柄と歩みを知る <span aria-hidden="true">↗</span></a>
    </div>
  </div>
</section>

<!-- 03 OUR VALUES｜方式B：CMS 80 H2 Text ＋ 42 Card Three ＋ CSS（正式な理念が未確認のため「大切にしていること」として表示） -->
<section class="section navy-band" id="company-values" aria-labelledby="cvalues-title" data-cms-id="80,42" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker">OUR VALUES <span>大切にしていること</span></p><h2 class="section-title" id="cvalues-title">人とのつながりを、<br>仕事の力に。</h2></div>
      <div class="body"><p>久留米興業が大切にしてきたのは、工事の品質だけではありません。関わる人との信頼、地域への責任、働く人の成長。その一つひとつが、会社を続けていく土台だと考えています。</p></div>
    </div>
    <div class="card-grid is-3 gate" data-gate="編集表現：正式な経営理念があれば最上部に追加し、3枚は具体的な取り組みとして再編集" style="margin-top:44px">
      <div class="info-card reveal" style="background:#eef3f8"><small>01</small><h3>信頼を重ねる</h3><p>取引先や協力会社と、約束を守りながら仕事を進める。一度きりではない関係を大切にしています。</p></div>
      <div class="info-card is-blue reveal" style="background:#eef3f8" data-delay="1"><small>02</small><h3>暮らしに向き合う</h3><p>工事の先には、そこで生活する人たちの日常があります。地域との関係に配慮しながら仕事を続けます。</p></div>
      <div class="info-card reveal" style="background:#eef3f8" data-delay="2"><small>03</small><h3>人とともに変わる</h3><p>働く人が経験を積み、安心して仕事を続けられるよう、仕事の進め方や環境を少しずつ見直していきます。</p></div>
    </div>
  </div>
</section>

<!-- 04 HISTORY（任意）｜方式B：CMS 761 Flow Cards ＋ CSS。事実が確認できた年のみ -->
<section class="section bg-soft" id="company-history" aria-labelledby="history-title" data-cms-id="761" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker">HISTORY <span>会社の歩み</span></p><h2 class="section-title" id="history-title">1974年から、<br>この街で仕事を続けてきました。</h2></div>
      <div class="body"><p>久留米興業は1974年3月に設立され、道路や水道などの施工に携わりながら、世田谷を拠点として事業を続けています。これからも街に必要とされる仕事を、次の世代へつないでいきます。</p></div>
    </div>
    <ol class="flow is-4 reveal" style="grid-template-columns:repeat(3,minmax(0,1fr));margin-top:36px">
      <li><span class="num">1974</span><h3>株式会社久留米興業 設立</h3><p>3月4日設立。世田谷区北烏山を拠点に事業を開始。</p></li>
      <li style="border-top-color:var(--blue)"><span class="num">2018</span><h3>関連会社 KRM株式会社 設立</h3><p>同じ敷地内に、建設資材の販売や受け入れを担う関連会社を設立。</p></li>
      <li><span class="num">NOW</span><h3>次の50年へ</h3><p>ガス管取替後の復旧舗装、水道、一般土木、下水道の4事業。働き方を見直しながら、次の世代へ会社をつなぐ。</p></li>
    </ol>
  </div>
</section>

<!-- 05 COMPANY PROFILE｜方式A/B：CMS 22 Table Border Light -->
<section class="section" id="company-overview" aria-labelledby="overview-title" data-cms-id="22" data-implementation="A/B">
  <div class="wrap" style="max-width:960px">
    <div class="section-heading reveal"><p class="section-kicker">COMPANY PROFILE</p><h2 class="section-title" id="overview-title">会社概要</h2></div>
    <div class="table-wrap reveal">
      <table class="spec-table"><tbody>
        <tr><th scope="row">社名</th><td>株式会社久留米興業</td></tr>
        <tr><th scope="row">代表者</th><td>代表取締役　川島 和範</td></tr>
        <tr><th scope="row">所在地</th><td>〒157-0061 東京都世田谷区北烏山6丁目26-28</td></tr>
        <tr><th scope="row">設立</th><td>1974年3月4日</td></tr>
        <tr><th scope="row">資本金</th><td>20,000,000円</td></tr>
        <tr><th scope="row">電話番号</th><td><a href="tel:0333093786">03-3309-3786</a></td></tr>
        <tr><th scope="row">事業内容</th><td>ガス管取替後の復旧舗装工事、道路改良・維持工事、水道工事、一般土木工事、下水道工事</td></tr>
        <tr class="gate review-only" data-gate="許可番号：最新の許可票を受領するまで非表示"><th scope="row">建設業許可</th><td class="tbd">【要最新照合】既存の公式表記は旧年度（特29・般29）</td></tr>
        <tr class="gate review-only" data-gate="最新の許可情報を受領するまで非表示"><th scope="row">指定工事店・産業廃棄物収集運搬</th><td class="tbd">【要最新照合】更新状況・地域・条件</td></tr>
        <tr class="gate" data-gate="求人票（2026-11-05）の記載。行政情報は30人。基準日を確認"><th scope="row">従業員数</th><td>37名</td></tr>
        <tr class="gate" data-gate="求人票で公開済み。HPへの社名掲載の可否を確認"><th scope="row">主な取引先</th><td>世田谷区、東京都水道局、日鉄P&amp;E株式会社、株式会社NIPPO ほか</td></tr>
        <tr><th scope="row">関連会社</th><td>KRM株式会社（<a href="#company-krm">下記参照</a>）</td></tr>
      </tbody></table>
    </div>
  </div>
</section>

<!-- 06 AFFILIATED COMPANY｜方式B：CMS 54 Half ＋ 90 Btn Text ＋ CSS -->
<section class="section bg-soft" id="company-krm" aria-labelledby="krm-title" data-cms-id="54,90" data-implementation="B">
  <div class="wrap half reveal">
    <div class="half-media"><div class="photo-slot review-only"><div><strong>C-04 KRMの敷地・資材・プラント</strong>社名が確認できる横長写真を受領後に配置</div></div><div class="pattern-art gate-hide-review" style="aspect-ratio:4/3"><span>KRM CO., LTD.</span></div></div>
    <div class="half-copy"><p class="section-kicker">GROUP / AFFILIATED COMPANY <span>関連会社</span></p><h2 class="section-title" id="krm-title">街の工事を、<br>資材の面からも支える。</h2>
      <p>久留米興業と同じ世田谷区北烏山の敷地内には、関連会社のKRM株式会社があります。KRMでは、再生アスファルト合材や再生砕石などの販売、残土・アスファルトガラ・コンクリートガラなどの受け入れを行っています。</p>
      <p>現場で必要とされる工事と、その工事に関わる資材。二つの仕事を知ることで、道路や土木に関わる仕事の幅広さを感じられます。</p>
      <table class="spec-table gate" data-gate="KRMの会社情報：公開前に最新照合" style="font-size:12.5px;margin:6px 0 22px"><tbody><tr><th scope="row">社名</th><td>KRM株式会社（関連会社）</td></tr><tr><th scope="row">設立</th><td>2018年10月30日</td></tr><tr><th scope="row">所在地</th><td>久留米興業と同所</td></tr><tr><th scope="row">代表者</th><td>代表取締役　川島 和範</td></tr></tbody></table>
      {ext(KRM, 'KRM株式会社の公式サイトへ <span aria-hidden="true">↗</span>', 'btn btn-dark')}</div>
  </div>
</section>

<!-- 07 ACCESS｜方式B：CMS 54 Half／22 Table ＋ 地図（api_map の可否を実CMSで確認。不可ならC：iframe＋CSS） -->
<section class="section" id="company-access" aria-labelledby="access-title" data-cms-id="54,22,api_map" data-implementation="B（地図はCMS確認）">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">ACCESS</p><h2 class="section-title" id="access-title">アクセス</h2></div>
    <div class="access reveal">
      <div>
        <table class="spec-table"><tbody>
          <tr><th scope="row">住所</th><td>〒157-0061<br>東京都世田谷区北烏山6丁目26-28</td></tr>
          <tr><th scope="row">電話</th><td><a href="tel:0333093786">03-3309-3786</a></td></tr>
          <tr><th scope="row">交通</th><td>京王線「千歳烏山駅」より徒歩15分<br>自転車・バイク通勤OK（社員）</td></tr>
          <tr class="gate review-only" data-gate="来訪用入口・駐車場：確認後に掲載"><th scope="row">来訪時</th><td class="tbd">【要確認】来訪用の入口、駐車場の有無</td></tr>
        </tbody></table>
        <p class="gate review-only" data-gate="事前連絡の要否を確認" style="font-size:13px;margin-top:16px">お越しになる際は、事前にご連絡いただけますとスムーズです。</p>
        <div class="cta-row">{ext(MAPS, 'Googleマップで見る <span aria-hidden="true">↗</span>', 'btn btn-dark')}</div>
      </div>
      <div class="map-box"><div><strong>地図（埋め込み予定）</strong>〒157-0061 東京都世田谷区北烏山6丁目26-28<br><span class="caption">CMSの地図機能、またはGoogleマップの埋め込みコードを本番で確認して配置します。</span></div></div>
    </div>
  </div>
</section>

<!-- 08 LINKS｜方式B：CMS 16 Card Four ＋ 90 Btn Text -->
<section class="section bg-blueish" id="company-links" aria-labelledby="clinks-title" data-cms-id="16,90" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><h2 class="section-title" id="clinks-title">会社を知った、その先へ。</h2><p class="section-heading-desc" style="max-width:640px">私たちが手がける仕事、そして働く人たち。久留米興業をもう少し詳しく知りたい方はこちらをご覧ください。</p></div>
    <div class="card-grid is-3">
      <a class="link-card reveal" href="@R@business/index.html"><div class="lc-media"><img src="{P}paving-roller.jpg" alt="舗装を転圧するローラー" loading="lazy"></div><div class="lc-body"><small>BUSINESS</small><h3>事業内容を見る</h3><span class="mini-link">事業内容へ <b aria-hidden="true">↗</b></span></div></a>
      <a class="link-card reveal" href="@R@people/index.html" data-delay="1"><div class="lc-media"><img src="{P}team.jpg" alt="久留米興業の社員たち" loading="lazy"></div><div class="lc-body"><small>PEOPLE</small><h3>働くメンバーを見る</h3><span class="mini-link">働くメンバーへ <b aria-hidden="true">↗</b></span></div></a>
      <a class="link-card reveal" href="@R@recruit/index.html" data-delay="2"><div class="lc-media"><img src="{P}field-crew.jpg" alt="現場で作業する社員" loading="lazy"></div><div class="lc-body"><small>RECRUIT</small><h3>採用情報を見る</h3><span class="mini-link">採用情報へ <b aria-hidden="true">↗</b></span></div></a>
    </div>
  </div>
</section>
'''


def build():
    return page("company", "会社情報｜株式会社久留米興業",
                "この街とともに歩み、次の世代へつないでいく。久留米興業の代表メッセージ、大切にしていること、会社概要、関連会社、アクセスをご紹介します。",
                1, BODY, crumb="会社情報")

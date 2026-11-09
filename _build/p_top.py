from common import *

P = "@R@assets/photos/"

from cms_hero import top_hero, ink_hero
HERO = ink_hero('top', 'hero-title', 'INFRASTRUCTURE / KURUME KOGYO', '<span class="ln">道路の復旧舗装から、</span><br><span class="ln">水道・土木工事まで。</span>', '世田谷を拠点に、1974年から。道路と街のインフラに関わる工事を担っています。', [(P + 'field-work-street.jpg', '重機とともに歩道の路盤をつくる施工中の現場')], 'Since 1974', cls='is-p1')

BODY = f'''
{HERO}

<!-- 02 ABOUT / PROFILE｜方式B：CMS 54 Half ＋ 22 Table（会社の基本情報） -->
<section class="section" id="about" aria-labelledby="about-title" data-cms-id="54,22" data-implementation="B">
  <div class="wrap">
    <div class="half reveal" style="grid-template-columns:1fr 1.05fr">
      <div class="half-copy">
        <p class="section-kicker">SINCE 1974 <span>会社概要</span></p>
        <h2 id="about-title" class="section-title">1974年から、<br>現場と地域に向き合う。</h2>
        <p>久留米興業は1974年設立。道路や水道に関わる工事を通じ、地域の暮らしを支えてきました。現在の会社の姿と、取り組んできた事業を知っていただけるページです。</p>
        <a class="text-link" href="@R@company/index.html#company-overview">会社の概要を見る <span aria-hidden="true">→</span></a>
      </div>
      <div class="half-media"><img src="{P}entrance.jpg" alt="「(株)久留米興業」の看板が掲げられた本社の敷地入口" loading="lazy" width="1046" height="698"><p class="caption">現在の本社（東京都世田谷区北烏山）</p></div>
    </div>
    <dl class="profile-strip reveal">
      <div><dt>設立</dt><dd>1974年3月4日</dd></div>
      <div><dt>所在地</dt><dd>東京都世田谷区北烏山6丁目26-28</dd></div>
      <div><dt>主な事業</dt><dd>復旧舗装・水道・一般土木・下水道</dd></div>
      <div><dt>関連会社</dt><dd>KRM株式会社</dd></div>
    </dl>
  </div>
</section>

<!-- 03 BUSINESS｜方式B：CMS 16 Card Four ＋ CSS（正式な工種名を見出しに） -->
<section class="section business-section bg-soft" id="business" aria-labelledby="business-title" data-cms-id="16" data-implementation="B">
  <div class="wrap">
    <div class="section-heading section-heading-split reveal">
      <div><p class="section-kicker">OUR WORK <span>事業内容</span></p><h2 class="section-title" id="business-title">対応する工事を、明確に。</h2></div>
      <p class="section-heading-desc">ガス管取替後の道路復旧から、水道・土木・下水道工事まで。主な事業領域を整理しました。発注内容に近い分野から詳しい情報をご覧ください。</p>
    </div>
    <div class="business-grid">
      <a class="business-card reveal" href="@R@business/index.html#service-gas" data-delay="0">
        <div class="business-image"><img src="{P}paving-roller.jpg" alt="ローラーで舗装を転圧している現場" loading="lazy"><span>01</span></div>
        <div class="business-card-body"><h3>ガス管取替後の<br>復旧舗装工事</h3><p>ガス管の取替後に行う道路の舗装復旧工事。</p><span class="mini-link">詳しく見る <b aria-hidden="true">→</b></span></div>
      </a>
      <a class="business-card reveal" href="@R@business/index.html#service-water" data-delay="1">
        <div class="business-image"><img src="{P}water-pipe.jpg" alt="掘削した溝に配水管を布設している現場" loading="lazy"><span>02</span></div>
        <div class="business-card-body"><h3>水道工事</h3><p>水道管の布設・布設替など、給水インフラに関わる工事。</p><span class="mini-link">詳しく見る <b aria-hidden="true">→</b></span></div>
      </a>
      <a class="business-card reveal" href="@R@business/index.html#service-civil" data-delay="2">
        <div class="business-image"><img src="{P}civil-road.jpg" alt="カラー舗装で仕上げた道路" loading="lazy"><span>03</span></div>
        <div class="business-card-body"><h3>一般土木工事</h3><p>道路の改良・維持など、公共空間の基盤に関わる土木工事。</p><span class="mini-link">詳しく見る <b aria-hidden="true">→</b></span></div>
      </a>
      <a class="business-card reveal" href="@R@business/index.html#service-sewer" data-delay="3">
        <div class="business-image"><div class="pattern-art" style="height:100%;aspect-ratio:auto"><span>SEWERAGE</span></div><span>04</span></div>
        <div class="business-card-body"><h3>下水道工事</h3><p>下水道の整備など、生活環境を支える工事。</p><span class="mini-link">詳しく見る <b aria-hidden="true">→</b></span></div>
      </a>
    </div>
    <p class="review-note">下水道工事と確認できる写真が届くまで、04は写真ではない図柄で表示しています。「自社施工一貫対応」「24時間対応」などの未確認の表現は使っていません。</p>
    <div class="section-footer reveal"><a class="btn btn-dark" href="@R@business/index.html">施工領域を詳しく見る <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<!-- 04 OUR APPROACH｜方式B：CMS 54 Half ＋ 80 H2 Text（連携の考え方を図で。一般的な説明で、同社の標準工程と誤認させない） -->
<section class="section" id="approach" aria-labelledby="approach-title" data-cms-id="54,80" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker">COORDINATION <span>仕事の進め方</span></p><h2 class="section-title" id="approach-title">施工の先にある、<br>信頼まで。</h2></div>
      <div class="body"><p>工事は、取引先・現場・協力会社・地域の方々との連携によって進みます。担当する仕事の内容だけでなく、現場を円滑に進めるための関係づくりも大切にしています。</p></div>
    </div>
    <ol class="approach-flow reveal">
      <li><small>CLIENT</small><h3>取引先・発注者</h3><p>工事の内容や場所、時期などのご相談を受けて、仕事が始まります。</p></li>
      <li><small>COORDINATION</small><h3>営業・調整</h3><p>現地の確認、見積、人や材料・日程の段取りを整え、現場とつなぎます。</p></li>
      <li><small>CONSTRUCTION</small><h3>現場・施工</h3><p>安全を確かめながら班で役割を分け、近隣にも配慮して施工を進めます。</p></li>
    </ol>
    <p class="fine-note">仕事の進め方を説明するための図です。工事ごとの詳しい流れは、事業内容のページでご案内しています。</p>
    <div class="cta-row reveal" style="display:flex;flex-wrap:wrap;gap:12px 24px;margin-top:24px"><a class="btn btn-dark" href="@R@business/index.html#business-process">仕事内容を知る <span aria-hidden="true">→</span></a><a class="text-link" href="@R@company/index.html#company-values">会社の考え方を見る <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<!-- 05 WORKS / PHOTO｜方式A/B：CMS 718 Portfolio Standard（施工実績を見るに掲載の工事名のみ） -->
<section class="section works-section bg-soft" id="works" aria-labelledby="works-title" data-cms-id="718" data-implementation="A/B">
  <div class="wrap">
    <div class="section-heading section-heading-split reveal"><div><p class="section-kicker">PROJECT SCENES <span>施工の様子</span></p><h2 class="section-title" id="works-title">現場を、写真で確かめる。</h2></div><p class="section-heading-desc">施工内容を検討する際には、言葉だけでなく実際の現場の様子も大切な判断材料です。久留米興業の仕事を、確認できた写真とともにご紹介します。</p></div>
    <div class="works-grid">
      <a class="work-card work-card-main reveal" href="{OFFICIAL_WORKS}" target="_blank" rel="noopener noreferrer"><div class="work-media"><img src="{P}work-kamisoshigaya.jpg" alt="歩道の舗装を終えた現場と工事黒板" loading="lazy"></div><div class="work-caption"><span>ROAD MAINTENANCE</span><h3>令和3年度 道路維持工事（世田谷区上祖師谷）</h3><span class="circle-arrow" aria-hidden="true">↗</span></div></a>
      <a class="work-card reveal" href="{OFFICIAL_WORKS}" target="_blank" rel="noopener noreferrer"><div class="work-media"><img src="{P}work-kyuden.jpg" alt="舗装を仕上げた車道" loading="lazy"></div><div class="work-caption"><span>SURFACE IMPROVEMENT</span><h3>世田谷区給田（表層改良）</h3><span class="circle-arrow" aria-hidden="true">↗</span></div></a>
      <a class="work-card reveal" href="{OFFICIAL_WORKS}" target="_blank" rel="noopener noreferrer"><div class="work-media"><img src="{P}work-chisaki.jpg" alt="新しく舗装した生活道路と工事黒板" loading="lazy"></div><div class="work-caption"><span>ROAD CONSTRUCTION</span><h3>世田谷区上祖師谷（地先道路築造工事）</h3><span class="circle-arrow" aria-hidden="true">↗</span></div></a>
    </div>
    <div class="section-footer reveal" style="display:flex;flex-wrap:wrap;gap:12px 24px;justify-content:center;align-items:center"><a class="btn btn-dark" href="@R@business/index.html">対応工事を詳しく見る <span aria-hidden="true">→</span></a>{ext(OFFICIAL_WORKS, '施工実績を見る <span aria-hidden="true">↗</span>', 'text-link')}</div>
  </div>
</section>

<!-- 06 WORK STYLE｜方式B：CMS 54 Half ＋ 787 Text Two（事務所と現場の実写。写っている人の職種は断定しない） -->
<section class="section" id="workstyle" aria-labelledby="workstyle-title" data-cms-id="54,787" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker">OUR TEAMWORK <span>働き方</span></p><h2 class="section-title" id="workstyle-title">施工を支えるのは、<br>人と段取り。</h2></div>
      <div class="body"><p>現場で施工する人、取引先と現場をつなぐ人。それぞれの役割や働き方を紹介しています。仕事の進め方を知ることは、会社を理解することにもつながります。</p><a class="text-link" href="@R@work-environment/index.html">労働環境を見る <span aria-hidden="true">→</span></a></div>
    </div>
    <div class="duo-photos reveal">
      <figure><img src="{P}member-t3.jpg" alt="事務所のデスクで書類を確認する社員" loading="lazy"><figcaption>事務所</figcaption></figure>
      <figure><img src="{P}field-worker-helmet.jpg" alt="ヘルメットをかぶって作業する社員" loading="lazy"><figcaption>現場</figcaption></figure>
    </div>
  </div>
</section>

<!-- 07 PEOPLE｜方式B：CMS 54 Half ＋ 42 Card Three（写真の人物に役職名を付けない） -->
<section class="section bg-soft" id="people" aria-labelledby="people-title" data-cms-id="54,42" data-implementation="B">
  <div class="wrap">
    <div class="half reveal" style="grid-template-columns:1fr 1fr">
      <div class="half-media"><img src="{P}member-i-helmet.jpg" alt="作業着とヘルメット姿の社員" loading="lazy" width="930" height="698"></div>
      <div class="half-copy">
        <p class="section-kicker">OUR MEMBERS <span>働くメンバー</span></p>
        <h2 class="section-title" id="people-title">現場と事務所、<br>役割は違っても。</h2>
        <p>工事は一人では完成しません。営業、現場、管理を担う人たちのそれぞれの視点から、久留米興業で働く実像をご紹介します。</p>
        <ul class="p1-role-links">
          <li><a href="@R@people/index.html#people-ceo"><small>PRESIDENT</small>代表の歩み<b aria-hidden="true">→</b></a></li>
          <li><a href="@R@people/index.html#people-sales"><small>SALES</small>営業職の仕事<b aria-hidden="true">→</b></a></li>
          <li><a href="@R@people/index.html#people-field"><small>FIELD</small>現場職の仕事<b aria-hidden="true">→</b></a></li>
        </ul>
        <a class="btn btn-dark" href="@R@people/index.html">働くメンバーを知る <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>
</section>

<!-- 08 RECRUIT｜方式B：CMS 787 Text Two ＋ 90 Btn Text（ページ後半に、薄いブルーグレーの帯として配置） -->
<section class="section" id="recruit" aria-labelledby="recruit-title" data-cms-id="787,90" data-implementation="B">
  <div class="wrap">
    <div class="p1-recruit-band reveal">
      <div><p class="section-kicker">CAREERS <span>採用情報</span></p><h2 class="section-title" id="recruit-title">次のインフラを支える仲間へ。</h2><p>営業職と現場職、それぞれの仕事には異なる専門性があります。入社後の流れ、評価、働く環境、募集条件は採用情報ページで詳しく紹介しています。</p></div>
      <div class="p1-recruit-roles">
        <a href="@R@recruit/index.html#career-sales"><small>SALES</small><strong>営業職</strong><span>取引先と現場をつなぐ、見積・調整・手配の仕事。</span></a>
        <a href="@R@recruit/index.html#career-field"><small>FIELD WORK</small><strong>現場職</strong><span>道路やインフラ工事の現場で、チームとともに施工する仕事。</span></a>
      </div>
      <a class="btn btn-dark" href="@R@recruit/index.html">採用情報・募集条件を見る <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<!-- 09 INFORMATION｜方式A：CMS 101 Blog Standard（確認できた公開記事のみ） -->
<section class="section news-section bg-soft" id="news" aria-labelledby="news-title" data-cms-id="101" data-implementation="A">
  <div class="wrap news-layout"><div class="news-heading reveal"><p class="section-kicker">JOURNAL <span>取り組み</span></p><h2 id="news-title" class="section-title">久留米興業の<br>取り組みを知る。</h2><p class="p1-news-lead">仕事の取り組みや社員へのインタビューなど、会社の実際の姿を伝える記事をご案内します。</p>{ext(BLOG_LIST, '公開記事一覧を見る <span aria-hidden="true">↗</span>', 'text-link')}</div><div class="news-list reveal"><a class="news-row" href="{DISASTER}" target="_blank" rel="noopener noreferrer"><time datetime="2024-03-08">2024.03.08</time><span class="news-category">お知らせ</span><span class="news-title">令和6年度能登半島地震に伴う災害救援隊について</span><b aria-hidden="true">↗</b></a><a class="news-row" href="{BLOG_NEGISHI}" target="_blank" rel="noopener noreferrer"><time aria-label="掲載日は記事でご確認ください">—</time><span class="news-category">社員インタビュー</span><span class="news-title">営業職・根岸さんのインタビュー</span><b aria-hidden="true">↗</b></a><a class="news-row" href="{OFFICIAL_NEWS}" target="_blank" rel="noopener noreferrer"><time aria-label="一覧ページ">—</time><span class="news-category">お知らせ</span><span class="news-title">お知らせ一覧</span><b aria-hidden="true">↗</b></a><p class="review-note">インタビュー記事の掲載日は元記事と照合してから表示します。CMS移植後はブログ機能と連携します。</p></div></div>
</section>

<!-- 10 CONTACT / NEXT｜方式B：CMS 90 Btn Text ＋ 23 Btn（法人向けの窓口を先に。フォームは新設せず公式の窓口へ） -->
<section class="contact-section" id="contact" aria-labelledby="contact-title" data-cms-id="90,23" data-implementation="B">
  <div class="wrap reveal">
    <p class="section-kicker">GET IN TOUCH <span>お問い合わせ</span></p>
    <h2 id="contact-title" class="section-title">工事のご相談から、<br>会社のことまで。</h2>
    <p style="max-width:720px;margin:0 0 32px">事業内容や会社概要をご覧いただき、工事に関するお問い合わせは正式な窓口へ。久留米興業で働くことに関心のある方には、採用情報もご案内しています。</p>
    <div class="contact-split">
      <div><small>FOR CLIENTS</small><h3>法人・取引先の方</h3><dl><dt>電話</dt><dd><a href="tel:0333093786">03-3309-3786</a></dd><dt>所在地</dt><dd>東京都世田谷区北烏山6丁目26-28</dd></dl><div class="cta-row">{ext(OFFICIAL_CONTACT, 'お問い合わせフォーム <span aria-hidden="true">↗</span>', 'btn btn-dark')}<a class="text-link" href="@R@company/index.html">会社情報を見る <span aria-hidden="true">→</span></a></div></div>
      <div><small>CAREERS</small><h3>採用をご検討の方</h3><p>仕事内容、入社後の流れ、待遇・募集条件をまとめています。</p><a class="btn btn-outline-light" href="@R@recruit/index.html">採用情報を見る <span aria-hidden="true">→</span></a></div>
    </div>
  </div>
</section>
'''


def build():
    return page("top", "株式会社久留米興業｜道路の復旧舗装から、水道・土木工事まで",
                "世田谷を拠点に、ガス管取替後の復旧舗装工事をはじめ、水道・一般土木・下水道工事に携わる株式会社久留米興業のWebサイトです。",
                0, BODY)

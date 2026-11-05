from common import *

P = "@R@assets/photos/"

BODY = f'''
<!-- 01 HERO｜方式C：独自HTML＋CSS（同一コード）、JSは別管理（site.js）。CMS ID参考：734/721 -->
<section class="hero" id="top" aria-labelledby="hero-title" data-cms-id="custom" data-implementation="C">
  <div class="hero-image" role="img" aria-label="道路の舗装工事で、つるはしを使って作業する人たち"></div>
  <div class="hero-veil"></div>
  <div class="hero-grid" aria-hidden="true"></div>
  <div class="wrap hero-content">
    <p class="eyebrow hero-eyebrow anim-enter"><span class="line"></span> KURUME KOGYO</p>
    <h1 id="hero-title" class="anim-enter" style="--delay:.12s">街を支える仕事を、<br><em>働く人の<br class="mobile-break">未来につなげる。</em></h1>
    <p class="hero-lead anim-enter" style="--delay:.22s">道路や水道など、暮らしに欠かせないインフラを支えてきた久留米興業。<br class="wide-only">積み重ねてきた技術と人とのつながりを大切に、街と働く人のこれからをつくっていきます。</p>
    <div class="hero-actions anim-enter" style="--delay:.32s">
      <a class="btn btn-white" href="@R@company/index.html">久留米興業について <span aria-hidden="true">↗</span></a>
      <a class="btn btn-outline-light" href="@R@recruit/index.html">採用情報を見る <span aria-hidden="true">↗</span></a>
    </div>
  </div>
  <div class="hero-bottom wrap"><span class="hero-bottom-left">SINCE 1974 · SETAGAYA, TOKYO</span><a class="scroll-link" href="#about">SCROLL <span></span></a></div>
  <div class="hero-side-label" aria-hidden="true">01 / KURUME KOGYO</div>
</section>

<!-- 02 ABOUT｜方式B：CMS 54 Half ＋ CSS -->
<section class="section about-section" id="about" aria-labelledby="about-title" data-cms-id="54" data-implementation="B">
  <div class="wrap">
    <div class="about-shell reveal">
      <div class="about-copy">
        <p class="section-kicker">ABOUT US <span>久留米興業について</span></p>
        <h2 id="about-title" class="section-title">街と、人と。<br>積み重ねてきた<span class="accent-word">50年以上。</span></h2>
        <p>株式会社久留米興業は、1974年の設立以来、道路や水道など、暮らしに欠かせないインフラ工事に取り組んできました。</p>
        <p>私たちが大切にしてきたのは、工事を完成させることだけではありません。その先にいる人とのつながりを大切にしながら、一つひとつの仕事に向き合ってきました。</p>
        <a class="text-link" href="@R@company/index.html">久留米興業を知る <span aria-hidden="true">↗</span></a>
      </div>
      <div class="about-media">
        <img src="{P}entrance.jpg" alt="「(株)久留米興業」の看板が掲げられた本社の敷地入口" loading="lazy" width="1046" height="698">
        <div class="about-media-caption"><strong>50<span>+</span></strong><small>YEARS OF HISTORY<br>1974 – PRESENT</small></div>
      </div>
    </div>
  </div>
</section>

<!-- 03 BUSINESS｜方式B：CMS 16 Card Four ＋ CSS -->
<section class="section business-section" id="business" aria-labelledby="business-title" data-cms-id="16" data-implementation="B">
  <div class="wrap">
    <div class="section-heading section-heading-split reveal">
      <div><p class="section-kicker">BUSINESS <span>事業内容</span></p><h2 class="section-title" id="business-title">何気なく通る道にも、<br>私たちの仕事がある。</h2></div>
      <p class="section-heading-desc">毎日の「当たり前」を支えるために。<br>道路・水道をはじめ、街のさまざまな場所で私たちの仕事が続いています。</p>
    </div>
    <div class="business-grid">
      <a class="business-card reveal" href="@R@business/index.html#service-gas" data-delay="0">
        <div class="business-image"><img src="{P}paving-roller.jpg" alt="久留米興業のローラーで舗装を転圧している現場" loading="lazy"><span>01</span></div>
        <div class="business-card-body"><h3>ガス管取替後の<br>復旧舗装工事</h3><p>ガス管を取り替えたあとの道路を、また使える状態へ。</p><span class="mini-link">復旧舗装について <b aria-hidden="true">↗</b></span></div>
      </a>
      <a class="business-card reveal" href="@R@business/index.html#service-water" data-delay="1">
        <div class="business-image"><img src="{P}water-pipe.jpg" alt="掘削した溝に配水管を布設している現場" loading="lazy"><span>02</span></div>
        <div class="business-card-body"><h3>水道工事</h3><p>配水管の新設や給水管の取替など、水の通り道を整える。</p><span class="mini-link">水道工事について <b aria-hidden="true">↗</b></span></div>
      </a>
      <a class="business-card reveal" href="@R@business/index.html#service-civil" data-delay="2">
        <div class="business-image"><img src="{P}civil-road.jpg" alt="カラー舗装で仕上げた道路" loading="lazy"><span>03</span></div>
        <div class="business-card-body"><h3>一般土木工事</h3><p>路面の改良・維持など、毎日使われる街の基盤を整える。</p><span class="mini-link">一般土木について <b aria-hidden="true">↗</b></span></div>
      </a>
      <a class="business-card reveal" href="@R@business/index.html#service-sewer" data-delay="3">
        <div class="business-image"><div class="pattern-art" style="height:100%;aspect-ratio:auto"><span>SEWERAGE</span></div><span>04</span></div>
        <div class="business-card-body"><h3>下水道工事</h3><p>下水道の整備を通じて、暮らしを支える地下のインフラに携わる。</p><span class="mini-link">下水道工事について <b aria-hidden="true">↗</b></span></div>
      </a>
    </div>
    <p class="review-note">【差替】旧デモの04下水道カードに使われていたP2180039.JPGは水道（配水管）の写真のため外しました。下水道工事と確認できる写真が届くまで、写真ではない図柄で表示しています。</p>
    <div class="section-footer reveal"><a class="btn btn-dark" href="@R@business/index.html">事業内容を詳しく見る <span aria-hidden="true">↗</span></a></div>
  </div>
</section>

<!-- 04 VALUES｜方式B：CMS 80 H2 Text ＋ 54 Half ＋ CSS -->
<section class="values-section" id="values" aria-labelledby="values-title" data-cms-id="80,54" data-implementation="B">
  <div class="wrap values-layout">
    <div class="values-intro reveal"><p class="section-kicker section-kicker-light">OUR VALUES <span>大切にしていること</span></p><h2 class="section-title" id="values-title">仕事をつなぐのは、<br>いつだって<span class="values-highlight">人だ。</span></h2><p>どんな仕事にも、その先に人がいる。<br>取引先、地域の方々、そしてともに働く仲間。<br>久留米興業は、その一つひとつのつながりを大切にしています。</p><a class="text-link text-link-light" href="@R@company/index.html#company-values">大切にしていることを読む <span aria-hidden="true">↗</span></a></div>
    <div class="values-items reveal">
      <div class="value-item"><span>01</span><div><h3>人とのつながり</h3><p>頼り、頼られる関係を、仕事の土台に。</p></div></div>
      <div class="value-item"><span>02</span><div><h3>街の暮らしへの責任</h3><p>目に見える仕事も、見えない仕事も、丁寧に。</p></div></div>
      <div class="value-item"><span>03</span><div><h3>働く人とつくる未来</h3><p>一人ひとりが、次の一歩を踏み出せる会社へ。</p></div></div>
    </div>
  </div>
  <span class="values-watermark" aria-hidden="true">CONNECT</span>
</section>

<!-- 05 WORKS｜方式A/B：CMS 718 Portfolio Standard。詳細は公式サイトの実績紹介へ（⑦は新規制作しない） -->
<section class="section works-section" id="works" aria-labelledby="works-title" data-cms-id="718" data-implementation="A/B">
  <div class="wrap">
    <div class="section-heading section-heading-split reveal"><div><p class="section-kicker">WORKS <span>施工実績</span></p><h2 class="section-title" id="works-title">一つひとつの現場が、<br>街のこれからをつくる。</h2></div>{ext(OFFICIAL_WORKS, '施工実績を見る <span aria-hidden="true">↗</span>', 'text-link desktop-link')}</div>
    <div class="works-grid">
      <a class="work-card work-card-main reveal" href="{OFFICIAL_WORKS}" target="_blank" rel="noopener noreferrer"><div class="work-media"><img src="{P}work-kamisoshigaya.jpg" alt="歩道の舗装を終えた現場と工事黒板" loading="lazy"></div><div class="work-caption"><span>ROAD MAINTENANCE</span><h3>令和3年度 道路維持工事（世田谷区上祖師谷）</h3><span class="circle-arrow" aria-hidden="true">↗</span></div></a>
      <a class="work-card reveal" href="{OFFICIAL_WORKS}" target="_blank" rel="noopener noreferrer"><div class="work-media"><img src="{P}work-kyuden.jpg" alt="舗装を仕上げた車道" loading="lazy"></div><div class="work-caption"><span>SURFACE IMPROVEMENT</span><h3>世田谷区給田（表層改良）</h3><span class="circle-arrow" aria-hidden="true">↗</span></div></a>
      <a class="work-card reveal" href="{OFFICIAL_WORKS}" target="_blank" rel="noopener noreferrer"><div class="work-media"><img src="{P}work-chisaki.jpg" alt="新しく舗装した生活道路と工事黒板" loading="lazy"></div><div class="work-caption"><span>ROAD CONSTRUCTION</span><h3>世田谷区上祖師谷（地先道路築造工事）</h3><span class="circle-arrow" aria-hidden="true">↗</span></div></a>
    </div>
    <p class="fine-note">工事名は現行の公式サイト「実績紹介」の掲載表記です。</p>
    <div class="mobile-only section-footer">{ext(OFFICIAL_WORKS, '施工実績を見る <span aria-hidden="true">↗</span>', 'btn btn-dark')}</div>
  </div>
</section>

<!-- 06 WORK STYLE｜方式B：CMS 54 Half ＋ CSS -->
<section class="section workstyle-section" id="workstyle" aria-labelledby="workstyle-title" data-cms-id="54" data-implementation="B">
  <div class="wrap workstyle-layout">
    <div class="workstyle-visual reveal"><div class="workstyle-visual-image" role="img" aria-label="現場で舗装の下地をつくる社員たち"></div><div class="workstyle-badge"><span>WORK STYLE</span><strong>仕事に向き合う時間も、<br>自分の時間も。</strong></div></div>
    <div class="workstyle-copy reveal"><p class="section-kicker">WORK STYLE <span>労働環境</span></p><h2 class="section-title" id="workstyle-title">長く働ける会社は、<br>変わり続ける会社だ。</h2><p>現場で働いてきた代表自身の経験があるからこそ、働き方にも目を向けてきました。</p><p>仕事への責任と、自分らしい暮らし。そのどちらも大切にできる会社を目指して、少しずつ変化を続けています。</p><div class="workstyle-tags"><span>働き方の見直し</span><span>資格取得への支援</span><span>現場を支えるチーム</span></div><a class="text-link" href="@R@work-environment/index.html">働く環境を知る <span aria-hidden="true">↗</span></a></div>
  </div>
</section>

<!-- 07 PEOPLE｜方式B：CMS 42 Card Three ＋ CSS。人物写真は承認後に差替 -->
<section class="section people-section" id="people" aria-labelledby="people-title" data-cms-id="42" data-implementation="B">
  <div class="wrap"><div class="section-heading section-heading-split reveal"><div><p class="section-kicker">PEOPLE <span>働くメンバー</span></p><h2 class="section-title" id="people-title">同じ人はいない。<br>だから、チームは面白い。</h2></div><p class="section-heading-desc">現場、営業、会社を支えるさまざまな人たち。<br>それぞれの経験と個性が、久留米興業の仕事をつくっています。</p></div>
    <div class="people-grid">
      <a class="person-card reveal" href="@R@people/index.html#people-ceo"><div class="person-art person-art-1"><span class="person-symbol">K</span><span class="person-phototag review-only">人物写真は承認後に差替</span></div><div class="person-info"><span>PRESIDENT</span><h3>代表の歩み</h3><p>現場から経営まで。人と働くことへの考え。</p><span class="person-arrow" aria-hidden="true">↗</span></div></a>
      <a class="person-card reveal" href="@R@people/index.html#people-sales"><div class="person-photo"><img src="{P}member-t2.jpg" alt="事務所で仕事をする営業職の社員" loading="lazy"></div><div class="person-info"><span>SALES TEAM</span><h3>営業職の仕事</h3><p>異業種から転職した社員も。取引先と現場をつなぐ。</p><span class="person-arrow" aria-hidden="true">↗</span></div></a>
      <a class="person-card reveal" href="@R@people/index.html#people-field"><div class="person-photo"><img src="{P}field-veteran.jpg" alt="現場の班長" loading="lazy"></div><div class="person-info"><span>FIELD TEAM</span><h3>現場職の仕事</h3><p>約30年続ける班長と、7〜12名の自社チームで。</p><span class="person-arrow" aria-hidden="true">↗</span></div></a>
    </div>
    <div class="section-footer reveal"><a class="btn btn-dark" href="@R@people/index.html">働くメンバーを見る <span aria-hidden="true">↗</span></a></div>
  </div>
</section>

<!-- 08 RECRUIT｜方式B：CMS 54 Half ＋ 90 Btn Text ＋ CSS -->
<section class="recruit-section" id="recruit" aria-labelledby="recruit-title" data-cms-id="54,90" data-implementation="B">
  <div class="wrap recruit-inner"><div class="recruit-heading reveal"><p class="section-kicker section-kicker-light">RECRUIT <span>採用情報</span></p><h2 id="recruit-title">今できることより、<br>これからできることを。</h2><p>最初から何でもできなくていい。<br>学び、考え、自分の仕事を少しずつ広げていく。<br>久留米興業で、あなたの次の一歩を。</p></div>
  <div class="recruit-entry-grid"><a class="recruit-entry reveal" href="@R@recruit/index.html#recruit-career"><span class="entry-icon">01</span><div><small>SALES</small><h3>営業職のキャリアを見る</h3><p>取引先と現場をつなぎ、仕事を前に進める。</p></div><b aria-hidden="true">↗</b></a><a class="recruit-entry reveal" href="@R@recruit/index.html#career-field"><span class="entry-icon">02</span><div><small>FIELD WORK</small><h3>現場職のキャリアを見る</h3><p>仲間と力を合わせ、街の基盤をつくる。</p></div><b aria-hidden="true">↗</b></a><a class="recruit-entry reveal" href="@R@recruit/index.html#recruit-anxiety"><span class="entry-icon">03</span><div><small>BEFORE YOU APPLY</small><h3>応募前の不安に答えます</h3><p>未経験・休み・給料・体力。社員の言葉でお答えします。</p></div><b aria-hidden="true">↗</b></a></div>
  <a class="recruit-overview-link" href="@R@recruit/index.html#recruit-openings">募集職種と応募方法を見る <span aria-hidden="true">↗</span></a></div>
</section>

<!-- 09 NEWS｜方式A：CMS 101 Blog Standard（連携できるまでは公式サイトの実在記事のみ） -->
<section class="section news-section" id="news" aria-labelledby="news-title" data-cms-id="101" data-implementation="A">
  <div class="wrap news-layout"><div class="news-heading reveal"><p class="section-kicker">NEWS <span>お知らせ</span></p><h2 id="news-title" class="section-title">久留米興業の日々を、<br>もっと身近に。</h2>{ext(OFFICIAL_NEWS, 'お知らせ一覧へ <span aria-hidden="true">↗</span>', 'text-link')}</div><div class="news-list reveal"><a class="news-row" href="{DISASTER}" target="_blank" rel="noopener noreferrer"><time datetime="2024-03-08">2024.03.08</time><span class="news-category">お知らせ</span><span class="news-title">令和6年度能登半島地震に伴う災害救援隊について</span><b aria-hidden="true">↗</b></a><a class="news-row" href="https://www.kurume-k.jp/452874803881/belrfza5rwefayabmajbx6d6kkhafj" target="_blank" rel="noopener noreferrer"><time datetime="2021-11-25">2021.11.25</time><span class="news-category">お知らせ</span><span class="news-title">ホームページをリニューアルしました。</span><b aria-hidden="true">↗</b></a><p class="fine-note">現行の公式サイトに掲載されている記事です。CMS移植後はブログ機能と連携します。</p></div></div>
</section>

<!-- 10 CONTACT｜方式B：CMS 90 Btn Text ＋ 23 Btn -->
<section class="contact-section" id="contact" aria-labelledby="contact-title" data-cms-id="90,23" data-implementation="B"><div class="wrap contact-layout reveal"><div><p class="section-kicker section-kicker-light">CONTACT</p><h2 id="contact-title">久留米興業を、もっと知る。</h2><p>事業のこと、採用のこと。<br>知りたいことに合わせてお進みください。</p></div><div class="contact-links"><a href="@R@business/index.html">事業内容を見る <span aria-hidden="true">↗</span></a><a href="@R@recruit/index.html">採用情報を見る <span aria-hidden="true">↗</span></a><a href="{OFFICIAL_CONTACT}" target="_blank" rel="noopener noreferrer">工事・事業に関するお問い合わせ（公式フォーム） <span aria-hidden="true">↗</span></a></div></div></section>
'''


def build():
    return page("top", "株式会社久留米興業｜街を支える仕事を、働く人の未来につなげる。",
                "街を支える仕事を、働く人の未来につなげる。久留米興業は、道路・水道などのインフラ工事を通して地域の暮らしを支えています。",
                0, BODY)

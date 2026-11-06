from p2common import *

P = "@R@assets/photos/"

BODY = f'''
<!-- 01 HERO #future-hero｜方式B：CMS 734 ＋ 721 ＋ CSS（上部白地にタイトル、下に大判写真とネイビーの細い帯） -->
<section class="section p2-people-hero p2-future-hero" id="future-hero" aria-labelledby="future-title" data-cms-id="734,721" data-implementation="B">
  <div class="wrap">
    <p class="section-kicker anim-enter">THE NEXT 50 YEARS <span>久留米興業の未来</span></p>
    <h1 id="future-title" class="p2-h1 anim-enter" style="--delay:.1s">次の50年も、<br>道を直す人がいる会社であるために。</h1>
    <p class="p2-lead anim-enter" style="--delay:.2s">この街に道路があり、水道があり、暮らしが続く限り、それらを支える仕事は必要です。久留米興業が次の世代につないでいきたいものを、お伝えします。</p>
  </div>
  <div class="wrap p2-wide is-band anim-enter" style="--delay:.35s"><img src="{P}field-crew-hq.jpg" alt="歩道の路盤をつくる現場職のチーム" width="927" height="618"></div>
</section>
<!--CRUMB-->

<!-- 02 VISION #future-vision｜方式B：CMS 54 Half ＋ 43 Title All -->
<section class="section" id="future-vision" aria-labelledby="vision-title" data-cms-id="54,43" data-implementation="B">
  <div class="wrap half reveal" style="grid-template-columns:.95fr 1.05fr">
    <div class="half-media"><img src="{P}yard.jpg" alt="重機や車両が並ぶ久留米興業の敷地" loading="lazy" width="1046" height="698"><p class="caption">本社の敷地</p></div>
    <div class="half-copy">
      <p class="section-kicker">VISION <span>目指す姿</span></p>
      <h2 class="section-title" id="vision-title">会社を次の世代へ。<br>残したいのは、仕事だけではない。</h2>
      <p>久留米興業は、先代から受け継がれ、社員や取引先、地域の方々の協力によって続いてきました。川島代表が目指しているのは、事業を次の世代へつなぐことです。しかし、道路を直す仕事があっても、それを担う人がいなければ会社は続きません。そこで必要になるのが、現場で培った技術や経験を受け継ぐ人、そして、その人たちが長く働ける環境です。</p>
      <p>これまでのやり方をすべて変えるのではなく、守るべきことは残し、時代に合わない部分は見直していく。そうした積み重ねによって、次の世代も必要とされる会社でありたいと考えています。</p>
      <p class="p2-emph-dark">仕事を残すことと、働く人を育てることは、別々ではありません。</p>
    </div>
  </div>
</section>

<!-- 03 ESSENTIAL #future-essential｜方式B：CMS 16 Card Four ＋ 54（写真が足りないため工事名＋短文のカード） -->
<section class="section bg-soft" id="future-essential" aria-labelledby="ess-title" data-cms-id="16,54" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker">ESSENTIAL WORK <span>続いていく仕事</span></p><h2 class="section-title" id="ess-title">使い続ける街には、<br>守り続ける仕事がある。</h2></div>
      <div class="body"><p>道路は毎日の通勤や通学、物流を支えています。地下にはガス管や水道管があり、その工事を終えた後にも道路を安全に使える状態へ戻す仕事があります。久留米興業は、ガス管取替後の復旧舗装、路面の改良・維持、水道工事などに携わってきました。</p><p>変化していく街と、そこで暮らす人たちのために、現場の知識や技術を積み重ねていくことが必要です。</p></div>
    </div>
    <div class="card-grid p2-line-cards" style="margin-top:40px">
      <article class="info-card reveal"><small>01</small><h3>復旧舗装</h3><p>ガス管取替工事の後に、道路を使える状態へ整える。</p></article>
      <article class="info-card reveal" data-delay="1"><small>02</small><h3>水道工事</h3><p>水道管の布設・布設替など、供給の基盤に関わる。</p></article>
      <article class="info-card reveal" data-delay="2"><small>03</small><h3>一般土木工事</h3><p>道路の維持・改良など、地域の土木工事。</p></article>
      <article class="info-card reveal" data-delay="3"><small>04</small><h3>下水道工事</h3><p>下水道整備など、生活の基盤に関わる。</p></article>
    </div>
    <div class="cta-row reveal"><a class="text-link" href="@P2@about/index.html#about-business">事業と会社の歩みを見る <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<!-- 04 KEEP / CHANGE #future-keep-change｜方式B：CMS 787 Text Two ＋ 80 H2 Text -->
<section class="section" id="future-keep-change" aria-labelledby="kc-title" data-cms-id="787,80" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">KEEP / CHANGE <span>守るもの・変えるもの</span></p><h2 class="section-title" id="kc-title">変えない想いと、<br>変えていく働き方。</h2></div>
    <div class="p2-keep-change reveal">
      <div class="is-keep"><small>KEEP</small><h3>守っていきたいもの</h3><p>一つひとつの現場に責任を持つこと。取引先や協力会社、地域の方々との関係を大切にすること。現場の経験を、次の仕事を担う人へ渡していくこと。会社が長く続くなかで培ってきたものを、これからも大切にしていきます。</p></div>
      <div class="is-change"><small>CHANGE</small><h3>変えていきたいもの</h3><p>忙しいからという理由だけで、一人に負担が集中する働き方。経験者の背中を見て覚えるだけに頼る教育。残業や安全、休憩について、従来の慣習を続けてよいのかという問い。仕事を続けるための条件として、今の現場に合った方法を考え直していきます。</p></div>
    </div>
    <p class="fine-note">「変えていきたいもの」には、すでに取り組んでいることと、これからの課題の両方が含まれます。</p>
  </div>
</section>

<!-- 05 WORKSTYLE #future-workstyle｜方式B：CMS 42 Card Three ＋ 54 Half。各カードに「これまで／考え方／これから」の区別 -->
<section class="section p2-tint" id="future-workstyle" aria-labelledby="ws-title" data-cms-id="42,54" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker">WORKSTYLE <span>取り組みの現在地</span></p><h2 class="section-title" id="ws-title">変化は、<br>一度で完成するものではない。</h2></div>
      <div class="body"><p>川島代表が会社の働き方を見直すきっかけになったのは、自身がかつて休みの少ない働き方を経験したこと、そして労務管理について学び直したことでした。少しずつルールを整えてきましたが、現場にはまだ負担の大きい日があります。変わってきたことと、これからの課題を区別して紹介します。</p></div>
    </div>
    <div class="card-grid is-3" style="margin-top:40px">
      <article class="info-card reveal gate" data-gate="現在の運用状況と数値は会社確認待ち"><span class="p2-status">これまでの見直し</span><h3>勤務時間の管理を見直してきた</h3><p>36協定を含めて残業時間を管理し、定時を意識した運用を進めてきました。</p></article>
      <article class="info-card is-blue reveal" data-delay="1"><span class="p2-status">考え方</span><h3>人を増やして負担を分ける</h3><p>現場の人数を厚くすることで、一人ひとりへの負荷を軽くしようとしてきました。</p></article>
      <article class="info-card reveal" data-delay="2"><span class="p2-status is-next">これからの課題</span><h3>教育を整えていきたい</h3><p>今は先輩が日々の現場と並行して教えています。教える側の余裕や仕組みが十分でないことも認識し、経験を次世代へつなぐ方法を考えていきます。</p></article>
    </div>
    <p class="p2-honest reveal">現場職の松野さんと奥居さんは、仕事の状況によって休憩に余裕を感じられない日があると話しています。働き方への考え方と、すべての現場での実態が一致しているとは限りません。だからこそ、現場の声を確認し、必要な改善を続けることが重要です。</p>
  </div>
</section>

<!-- 06 PEOPLE #future-people｜方式B：CMS 761 Flow Cards ＋ 54。正式なキャリア制度ではなく考え方の図 -->
<section class="section" id="future-people" aria-labelledby="fp-title" data-cms-id="761,54" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker">PEOPLE <span>受け継ぐ人</span></p><h2 class="section-title" id="fp-title">仕事を覚えた人が、<br>次の人の力になる。</h2></div>
      <div class="body"><p>どんな現場も、最初から何でもできる人ばかりで成り立っているわけではありません。営業として入社した人が現場を学び、資格を取って現場代理人を目指すこともあれば、現場職として作業の流れを覚え、班長を支える仕事を身につけることもあります。経験を持つ社員と新しく入る人が、日々の仕事を通じて学び合う。久留米興業がこれから整えていきたいのは、そのつながりを続けられる環境です。</p></div>
    </div>
    <ol class="flow is-4 p2-relay reveal" style="margin-top:40px">
      <li><span class="num">01</span><h3>知る</h3><p>現場・会社・仕事の流れを理解する</p></li>
      <li><span class="num">02</span><h3>任される</h3><p>小さな仕事から担当範囲を広げる</p></li>
      <li><span class="num">03</span><h3>支える</h3><p>周囲の動きを見ながら連携・調整する</p></li>
      <li><span class="num">04</span><h3>伝える</h3><p>経験を後輩や次世代へつなぐ</p></li>
    </ol>
    <p class="fine-note">4つの段階は考え方を示した図で、時期や昇格を約束するものではありません。</p>
    <div class="card-grid is-3" style="margin-top:28px">
      <a class="link-card no-media reveal" href="{BLOG_NEGISHI}" target="_blank" rel="noopener noreferrer"><div class="lc-body"><small>根岸さん</small><h3>お茶の営業から土木へ。資格を取り、現場代理人に。</h3><span class="mini-link">記事を読む <b aria-hidden="true">↗</b></span></div><span class="sr-only">（外部サイトが開きます）</span></a>
      <a class="link-card no-media reveal" href="{BLOG_TAKAHATA}" target="_blank" rel="noopener noreferrer" data-delay="1"><div class="lc-body"><small>高畑さん</small><h3>土木を知らない新卒から、現場と営業を学ぶ。</h3><span class="mini-link">記事を読む <b aria-hidden="true">↗</b></span></div><span class="sr-only">（外部サイトが開きます）</span></a>
      <a class="link-card no-media reveal" href="@P2@people/index.html#people-field" data-delay="2"><div class="lc-body"><small>松野さん</small><h3>班長として役割を分け、新人には少しずつ覚えてほしいと話す。</h3><span class="mini-link">働くスタッフで読む <b aria-hidden="true">→</b></span></div></a>
    </div>
  </div>
</section>

<!-- 07 VOICES #future-voices｜方式B：CMS 787 Text Two ＋ 42 -->
<section class="section bg-soft" id="future-voices" aria-labelledby="fv-title" data-cms-id="787,42" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">VOICES <span>現場からの声</span></p><h2 class="section-title" id="fv-title">未来について、<br>現場にいる人も語っている。</h2></div>
    <div class="p2-future-voices reveal">
      <article class="p2-duo-card has-photo"><img src="{P}member-i-helmet.jpg" alt="ヘルメット姿の営業職・今井さん" loading="lazy"><div><small>営業の声｜今井さん</small><p>広告業界から転職した今井さんは、未経験者として現場で学び直し、仕事の仕方を変えてきた人です。将来の専門性や、自分に任される役割を重視して転職した経験から、久留米興業で働くことを考えています。</p>{ext(BLOG_IMAI, '今井さんの全文記事 ↗', 'mini-link')}</div></article>
      <article class="p2-duo-card"><small>現場の声｜松野さん・奥居さん</small><p>現場で働く二人は、仕事の厳しさと、先輩や仲間との連携を率直に語っています。1日を余裕をもって終えたい、少しずつ仕事を覚えてほしいという実感は、これから働く環境を考えるうえで大切な声です。</p><a class="mini-link" href="@P2@people/index.html#people-field">働くスタッフの話を読む <b aria-hidden="true">→</b></a></article>
    </div>
  </div>
</section>

<!-- 08 COMMUNITY #future-community｜方式B：CMS 54 Half ＋ 43（写真なし、本文のみ） -->
<section class="section" id="future-community" aria-labelledby="fc-title" data-cms-id="54,43" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal gate" data-gate="地域行事・ブロックの譲渡は代表インタビュー時点の例：現在の実施状況を確認">
      <div><p class="section-kicker">COMMUNITY <span>地域とのつながり</span></p><h2 class="section-title" id="fc-title">仕事をする街と、<br>これからもつながっていたい。</h2></div>
      <div class="body"><p>建設工事は、周辺に暮らす方々の理解や協力があってこそ進められます。朝の車の出入りや工事中の音など、地域に負担をかけてしまう場面があることも、川島代表は認識しています。久留米興業では、地域の行事やバザーに協力を求められたときに、できる範囲で協賛してきたそうです。また、現場で余ったインターロッキングブロックを希望する方に渡すこともあると話しています。</p><p>大きな宣伝よりも、地域で仕事を続ける会社として、顔の見える関係を大切にしていきたいという思いがあります。</p></div>
    </div>
  </div>
</section>

<!-- 09 TRUST #future-trust｜方式B：CMS 80 H2 Text ＋ 54（大きなネイビーのテキストパネル＋施工後の道路） -->
<section class="section navy-band" id="future-trust" aria-labelledby="trust-title" data-cms-id="80,54" data-implementation="B">
  <div class="wrap reveal" style="max-width:980px">
    <div class="half-copy">
      <p class="section-kicker section-kicker-light">TRUST <span>信頼</span></p>
      <h2 class="section-title p2-xl" id="trust-title">仕事を選べる会社になる。<br>そのために、まず選ばれる会社へ。</h2>
      <p>川島代表が将来の理想として語るのは、技術や信頼を積み重ね、久留米興業を大切にしてくれる取引先と、継続的に仕事ができる会社になることです。すべての依頼を無理に引き受けるだけでは、現場で働く社員の負担が大きくなる場合もあります。施工の品質や対応への信頼を高め、取引先、協力会社、社員それぞれが無理なく仕事を続けられる関係を築くことが、これからの目標です。</p>
    </div>
  </div>
  <p class="review-note wrap">施工後の道路写真は、TOPと同じ写真にならないよう、このページ用の写真が届くまで載せていません。</p>
</section>

<!-- 10 CTA #future-cta｜方式B：CMS 90 ＋ 23 -->
<section class="contact-section" id="future-cta" aria-labelledby="fcta-title" data-cms-id="90,23" data-implementation="B"><div class="wrap contact-layout reveal"><div><p class="section-kicker section-kicker-light">NEXT</p><h2 id="fcta-title">未来をつくる仕事を、<br>あなた自身の目で確かめてください。</h2><p>誰もが最初から明確な目標を持っているわけではありません。どのような仕事をし、誰と働き、何を覚えていけるのか。具体的な仕事内容や社員の声を知ったうえで、自分に合うか考えてみてください。</p></div><div class="contact-links"><a href="@P2@recruit/index.html">募集職種と採用情報を見る <span aria-hidden="true">→</span></a><a href="@P2@people/index.html">働く人の声を見る <span aria-hidden="true">→</span></a><a href="@P2@about/index.html">会社の歩みを見る <span aria-hidden="true">→</span></a></div></div></section>
'''


def build():
    return p2_page("future", "久留米興業の未来｜株式会社久留米興業",
                   "次の50年も、道を直す人がいる会社であるために。これまでの見直し、今の課題、これからの目標を分けてご紹介します。",
                   2, BODY, crumb="久留米興業の未来")

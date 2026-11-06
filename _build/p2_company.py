from p2common import *

P = "@R@assets/photos/"

BODY = f'''
<!-- 01 HERO #company-hero｜方式B：CMS 734 ＋ 721（白基調・社屋写真が主役） -->
<section class="section p2-company-hero" id="company-hero" aria-labelledby="company-title" data-cms-id="734,721" data-implementation="B">
  <div class="wrap half" style="grid-template-columns:1fr 1.1fr">
    <div class="half-copy">
      <p class="section-kicker anim-enter">COMPANY <span>会社情報</span></p>
      <h1 id="company-title" class="p2-h1 anim-enter" style="--delay:.1s">人とのつながりを大切に、<br>街の当たり前を支えていく。</h1>
      <p class="p2-lead anim-enter" style="--delay:.2s">1974年の設立以来、道路や水道など暮らしに欠かせない工事を担ってきました。久留米興業の歩みと、会社としての考え方をお伝えします。</p>
      <div class="cta-row anim-enter" style="--delay:.3s"><a class="btn btn-dark" href="#company-outline">会社概要へ <span aria-hidden="true">↓</span></a><a class="text-link" href="#company-access">アクセス <span aria-hidden="true">↓</span></a></div>
    </div>
    <div class="half-media anim-enter" style="--delay:.25s"><img src="{P}entrance.jpg" alt="「(株)久留米興業」の看板が掲げられた本社の敷地入口" width="1046" height="698"></div>
  </div>
</section>
<!--CRUMB-->

<!-- 02 MESSAGE #company-message｜方式B：CMS 54 Half ＋ 43。取引先・地域・社員に向けた会社としての言葉 -->
<section class="section bg-soft" id="company-message" aria-labelledby="msg-title" data-cms-id="54,43" data-implementation="B">
  <div class="wrap half reveal" style="grid-template-columns:.75fr 1.25fr">
    <div class="half-media is-portrait"><img src="{P}ceo-wide.jpg" alt="代表取締役 川島 和範" loading="lazy" width="941" height="627"><p class="caption">代表取締役　川島 和範</p></div>
    <div class="half-copy gate" data-gate="代表一人称の編集原稿：本人承認前は公開しない">
      <p class="section-kicker">MESSAGE <span>代表メッセージ</span></p>
      <h2 class="section-title" id="msg-title">その「当たり前」を支える仕事に、<br>これからも責任を持つ。</h2>
      <p>道路を安全に通れること。蛇口をひねれば水が使えること。普段の生活では意識する機会が少ないかもしれませんが、私たちの仕事は、そうした毎日を支えています。</p>
      <p>久留米興業は、1974年の設立以来、ガス管取替後の舗装復旧や水道工事、路面の改良・維持などに携わってきました。工事は現場で作業する人だけで完結するものではありません。取引先、協力会社、地域の方々の理解と協力があって、一つの仕事を完成させることができます。</p>
      <p>私自身、現場の作業から仕事を始め、管理や取引先との関係づくり、そして経営を経験してきました。立場が変わるにつれて、それぞれの仕事の大変さと、人とのつながりの大切さを感じるようになりました。</p>
      <p>長年の経験や信頼を大切にしながら、時代に合わせて変えるべきところは見直す。社員が長く働き、取引先からも地域の方々からも頼っていただける会社であり続けたいと考えています。</p>
      <p>これからも、私たちにできる仕事を一つひとつ積み重ねてまいります。</p>
      <p class="p2-sign">株式会社久留米興業　代表取締役　川島 和範</p>
    </div>
  </div>
</section>

<!-- 03 PRINCIPLES #company-philosophy｜方式B：CMS 43 Title All ＋ 42 Card Three。正式な理念ではなく「大切にしていること」 -->
<section class="section" id="company-philosophy" aria-labelledby="phil-title" data-cms-id="43,42" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker">OUR PRINCIPLES <span>大切にしていること</span></p><h2 class="section-title" id="phil-title">仕事も、会社も、<br>人とのつながりから。</h2></div>
      <div class="body"><p>現場では、一人ひとりの役割と、周囲との連携が必要です。取引先や協力会社、地域の方々との関係も、その仕事を支えています。久留米興業は、互いの立場を理解し、一つひとつの仕事を誠実に進める姿勢を大切にしてきました。</p></div>
    </div>
    <div class="card-grid is-3 p2-line-cards gate" data-gate="編集上の案：正式な経営理念があれば原文を優先" style="margin-top:40px">
      <article class="info-card reveal"><small>01</small><h3>人とのつながり</h3><p>仕事を任せてくださる方、現場を支える方、地域で暮らす方。多くの人との関係を大切にして仕事を進めます。</p></article>
      <article class="info-card reveal" data-delay="1"><small>02</small><h3>目の前の仕事に責任を持つ</h3><p>現場の安全や段取りに目を向け、職種が違っても必要な情報をつなぎ、確かな施工を積み重ねます。</p></article>
      <article class="info-card reveal" data-delay="2"><small>03</small><h3>変えるべきことを見直す</h3><p>これまで培った経験を守りながら、今の働く人と仕事に合う形を考え続けます。</p></article>
    </div>
  </div>
</section>

<!-- 04 HISTORY #company-history｜方式B：CMS 761 Flow Cards ＋ 54。正式な記録がある出来事だけ -->
<section class="section bg-soft" id="company-history" aria-labelledby="ch-title" data-cms-id="761,54" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker">HISTORY <span>会社の歩み</span></p><h2 class="section-title" id="ch-title">1974年から、<br>この街で仕事を続けてきた。</h2></div>
      <div class="body"><p>久留米興業は、1974年3月4日に設立されました。道路舗装や水道、公共インフラの工事を通して、地域の暮らしに関わる仕事を続けています。今も必要とされる工事を担いながら、次の世代へ何を残していくかを考えています。</p></div>
    </div>
    <ol class="p2-timeline is-compact reveal">
      <li><span class="when">1974.03</span><div><h3>株式会社久留米興業 設立</h3><p>3月4日設立。</p></div></li>
      <li class="is-sub"><span class="when">2018.10</span><div><h3>関連会社 KRM株式会社 設立</h3><p>10月30日設立。久留米興業とは別の会社です。</p></div></li>
      <li class="is-next"><span class="when">現在</span><div><h3>舗装工事・水道工事などを継続</h3><p>ガス管取替後の復旧舗装、路面改良・維持、水道工事などに携わっています。</p></div></li>
    </ol>
    <p class="review-note">2024年の能登半島地震に伴う救援活動は、活動内容と写真の公開範囲を確認できたら年表に追加します（久留米興業についてのページでは記事へのリンクとして掲載）。</p>
  </div>
</section>

<!-- 05 OUTLINE #company-outline｜方式A/B：CMS 22 Table Border Light -->
<section class="section" id="company-outline" aria-labelledby="outline-title" data-cms-id="22" data-implementation="A/B">
  <div class="wrap" style="max-width:960px">
    <div class="section-heading reveal"><p class="section-kicker">COMPANY PROFILE</p><h2 class="section-title" id="outline-title">会社概要</h2></div>
    <div class="table-wrap reveal"><table class="spec-table p2-profile"><caption class="sr-only">株式会社久留米興業の会社概要</caption><tbody>
      <tr><th scope="row">会社名</th><td>株式会社久留米興業</td></tr>
      <tr><th scope="row">代表者</th><td>代表取締役　川島 和範</td></tr>
      <tr><th scope="row">設立</th><td>1974年3月4日</td></tr>
      <tr><th scope="row">所在地</th><td>〒157-0061 東京都世田谷区北烏山6丁目26-28</td></tr>
      <tr><th scope="row">資本金</th><td>20,000,000円</td></tr>
      <tr><th scope="row">電話番号</th><td><a href="tel:0333093786">03-3309-3786</a></td></tr>
      <tr><th scope="row">主要事業</th><td>ガス管取替後の復旧舗装工事、路面改良・維持、水道工事、一般土木、下水道工事</td></tr>
      <tr><th scope="row">関連会社</th><td>KRM株式会社</td></tr>
      <tr class="gate gate-hide" data-gate="最新の許可証と照合後に掲載"><th scope="row">建設業許可</th><td>【確認待ち】</td></tr>
      <tr class="gate gate-hide" data-gate="集計日と対象範囲を確認後に掲載（37名／30名の差）"><th scope="row">従業員数</th><td>【確認待ち】</td></tr>
    </tbody></table></div>
  </div>
</section>

<!-- 06 GROUP #company-group｜方式B：CMS 54 Half ＋ 42。KRMの写真は未取得のため本文とカードで構成 -->
<section class="section bg-soft" id="company-group" aria-labelledby="group-title" data-cms-id="54,42" data-implementation="B">
  <div class="wrap">
    <div class="lead-block reveal">
      <div><p class="section-kicker">GROUP COMPANY <span>関連会社</span></p><h2 class="section-title" id="group-title">工事の現場を、<br>資材の面からも支える。</h2></div>
      <div class="body"><p>久留米興業の関連会社であるKRM株式会社は、世田谷区北烏山に拠点を置き、道路工事に用いるアスファルト合材や再生砕石などの販売、残土やアスファルトガラなどの受け入れを行っています。道路を整える仕事と、それに必要な資材を扱う仕事。それぞれの役割から、地域の建設・舗装の現場を支えています。</p></div>
    </div>
    <div class="card-grid is-3" style="margin-top:36px">
      <div class="info-card reveal"><small>COMPANY</small><h3>KRM株式会社</h3><p>〒157-0061 東京都世田谷区北烏山6丁目26-28（久留米興業 敷地内）<br>設立：2018年10月30日<br>代表取締役：川島 和範</p></div>
      <div class="info-card is-blue reveal" data-delay="1"><small>取り扱い例</small><h3>道路工事の資材</h3><p>再生密粒アスファルト合材、再生砕石、改良土、川砂</p></div>
      <div class="info-card reveal" data-delay="2"><small>受け入れ例</small><h3>工事で出るもの</h3><p>残土、アスファルトガラ、コンクリートガラ</p></div>
    </div>
    <p class="review-note">KRMの電話番号は掲載先によって異なる（…5222／…5221）ため、確認できるまで表示していません。</p>
    <div class="cta-row reveal">{ext(KRM, 'KRM株式会社のサイトを見る <span aria-hidden="true">↗</span>', 'btn btn-dark')}</div>
  </div>
</section>

<!-- 07 ACCESS #company-access｜方式B：CMS 22 Table ＋ 54 Half。地図は外部リンク（埋め込みはCMSで可否を確認） -->
<section class="section" id="company-access" aria-labelledby="access-title" data-cms-id="22,54" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">ACCESS</p><h2 class="section-title" id="access-title">アクセス</h2><p class="section-heading-desc">株式会社久留米興業の本社は、東京都世田谷区北烏山にあります。面接やご訪問の際は、目的に応じた窓口へ事前にご連絡ください。</p></div>
    <div class="p2-access reveal">
      <dl><div><dt>所在地</dt><dd>〒157-0061<br>東京都世田谷区北烏山6丁目26-28</dd></div><div><dt>電話</dt><dd><a href="tel:0333093786">03-3309-3786</a></dd></div><div class="gate" data-gate="来社経路と所要時間を会社が確認してから確定"><dt>最寄り駅</dt><dd>京王線「千歳烏山駅」</dd></div></dl>
      <div class="p2-map"><p>地図</p><strong>東京都世田谷区北烏山6丁目26-28</strong>{ext(MAPS, 'Googleマップで場所を確認する <span aria-hidden="true">↗</span>', 'btn btn-dark')}</div>
    </div>
  </div>
</section>

<!-- 07B CONTACT #company-contact｜方式B：CMS 90 Btn Text ＋ 23 Btn（法人向けの正式な連絡先。フォームは新設しない） -->
<section class="section bg-soft" id="company-contact" aria-labelledby="ccontact-title" data-cms-id="90,23" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">CONTACT <span>お問い合わせ窓口</span></p><h2 class="section-title" id="ccontact-title">工事・事業に関するお問い合わせ</h2></div>
    <div class="contact-split reveal">
      <div><small>FOR CLIENTS</small><h3>法人・取引先の方</h3><dl><dt>電話</dt><dd><a href="tel:0333093786">03-3309-3786</a></dd><dt>所在地</dt><dd>〒157-0061 東京都世田谷区北烏山6丁目26-28</dd></dl><div class="cta-row">{ext(OFFICIAL_CONTACT, 'お問い合わせフォーム <span aria-hidden="true">↗</span>', 'btn btn-dark')}<a class="text-link" href="@P2@about/index.html#about-business">4つの事業を見る <span aria-hidden="true">→</span></a></div></div>
      <div><small>CAREERS</small><h3>採用をご検討の方</h3><p>仕事内容、仕事のリアル、待遇・募集条件をまとめています。</p><a class="btn btn-outline-light" href="@P2@recruit/index.html">採用情報を見る <span aria-hidden="true">→</span></a></div>
    </div>
  </div>
</section>

<!-- 08 LINKS #company-links｜方式B：CMS 90 Btn Text ＋ 23 Btn -->
<section class="section bg-soft" id="company-links" aria-labelledby="links-title" data-cms-id="90,23" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><h2 class="section-title" id="links-title">久留米興業について、<br>さらに知る。</h2><p class="section-heading-desc">事業の背景を知る、働く人の声を知る、具体的な仕事や募集条件を確かめる。気になる情報からご覧ください。</p></div>
    <div class="card-grid is-3">
      <a class="link-card no-media reveal" href="@P2@about/index.html"><div class="lc-body"><small>ABOUT</small><h3>久留米興業の歩みと考え方</h3><span class="mini-link">見る <b aria-hidden="true">→</b></span></div></a>
      <a class="link-card no-media reveal" href="@P2@people/index.html" data-delay="1"><div class="lc-body"><small>PEOPLE</small><h3>働くメンバーの声</h3><span class="mini-link">見る <b aria-hidden="true">→</b></span></div></a>
      <a class="link-card no-media reveal" href="@P2@recruit/index.html" data-delay="2"><div class="lc-body"><small>RECRUIT</small><h3>仕事内容・募集要項</h3><span class="mini-link">見る <b aria-hidden="true">→</b></span></div></a>
    </div>
    <p class="cta-row reveal"><a class="text-link" href="@P2@future/index.html">久留米興業の未来 <span aria-hidden="true">→</span></a></p>
  </div>
</section>
'''


def build():
    return p2_page("company", "会社情報｜株式会社久留米興業",
                   "人とのつながりを大切に、街の当たり前を支えていく。代表メッセージ、会社概要、関連会社KRM、アクセスをご案内します。",
                   2, BODY, crumb="会社情報")

from common import *

P = "@R@assets/photos/"

FAQ = [
    ("仕事内容", [
        ("建設業の経験がなくても応募できますか？", "営業職は異業種からの応募を想定しており、入社後は先輩社員に同行しながら仕事を覚えていきます。現場職も、経験や適性に応じて仕事を覚えていただく方針です。応募資格は各募集要項をご確認ください。", None),
        ("営業職はいきなり一人で取引先を担当しますか？", "初日から案件を任せるのではなく、入社当初は先輩社員への同行から始める予定です。最低3か月程度は同行を基本とし、習熟度に応じて役割を広げていきます。", None),
    ]),
    ("成長・評価", [
        ("どのような仕事ぶりが評価されますか？", "職種や経験年数によって異なります。学ぶ姿勢、現場との連携、できるようになった作業や業務、資格、取引先・現場からの評価などを大切にしています。", None),
        ("仕事に必要な資格は取得できますか？", "資格取得を支援する制度があります。支援対象となる資格、費用負担、取得条件は募集要項・面談時にご確認ください。", None),
    ]),
    ("働き方・応募", [
        ("現場職の仕事は体力的に大変ですか？", "早朝からの移動や夏場の暑さなど、現場ならではの負担があります。仕事内容や安全対策を含め、<a href=\"@R@work-environment/index.html\">労働環境ページ</a>で紹介しています。", None),
        ("遠方からの応募は可能ですか？", "個室寮の案内があります。空室や費用、入寮条件、勤務地との通勤については応募前にお問い合わせください。", None),
        ("応募前に仕事内容を確認する方法はありますか？", "現場見学をご案内しています。実施可能な日程やオンライン面談の可否は、採用担当と調整のうえご案内します。", "見学・オンライン面談の運用を確認"),
        ("入社までの選考の流れは？", "<span class=\"tbd\">【要確認】応募受付 → 連絡 → 書類確認 → 面談 → 結果連絡 の実際の運用を確定して記入します。</span>", "選考フロー未確定（公開時は非表示）"),
    ]),
]


def faq_html():
    out = []
    for cat, items in FAQ:
        rows = []
        for q, a, gate in items:
            if gate and "非表示" in gate:
                attr = f' class="gate review-only" data-gate="{gate}"'
            elif gate:
                attr = f' class="gate" data-gate="{gate}"'
            else:
                attr = ""
            rows.append(f'<details{attr}><summary>{q}</summary><div class="answer"><p style="margin:0">{a}</p></div></details>')
        out.append(f'<div class="faq-group"><h3>{cat}</h3><div class="faq">{"".join(rows)}</div></div>')
    return "".join(out)


def faq_jsonld():
    import json
    ents = []
    for _, items in FAQ:
        for q, a, gate in items:
            if gate:
                continue
            import re
            ents.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}})
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": ents}, ensure_ascii=False) + "</script>"


BODY = f'''
<!-- 01 RECRUIT HERO｜方式B：CMS 734 H1 Center ＋ CSS -->
<section class="page-hero" id="recruit-hero" aria-labelledby="recruit-title" data-cms-id="734" data-implementation="B">
  <div class="page-hero-img" style="background-image:url('{P}field-crew.jpg');background-position:55% 60%" role="img" aria-label="舗装の下地をつくる久留米興業の現場職"></div>
  <div class="wrap">
    <p class="eyebrow anim-enter"><span class="line"></span>RECRUIT / JOIN OUR TEAM</p>
    <h1 id="recruit-title" class="anim-enter" style="--delay:.1s">これからの自分に、<br>街を支える仕事を。</h1>
    <p class="lead anim-enter" style="--delay:.2s">道路や水道など、毎日の暮らしに欠かせないインフラを支える久留米興業。私たちの仕事には、現場で技術を磨く人も、取引先と現場をつなぐ人も必要です。今できることだけでなく、これから身につける力を大切にしながら、一緒に歩んでいきませんか。</p>
    <div class="hero-actions anim-enter" style="--delay:.3s"><a class="btn btn-white" href="#recruit-career">仕事とキャリアを見る <span aria-hidden="true">↓</span></a><a class="btn btn-outline-light" href="#recruit-openings">募集要項を見る <span aria-hidden="true">↓</span></a></div>
  </div>
</section>
<!--CRUMB-->

<!-- 02 代表採用メッセージ｜方式B：CMS 54 Half ＋ 35 Title Sub ＋ CSS -->
<section class="section" id="recruit-message" aria-labelledby="message-title" data-cms-id="54,35" data-implementation="B">
  <div class="wrap half has-optional-media reveal" style="grid-template-columns:.82fr 1fr">
    <div class="half-media review-only"><div class="photo-slot is-portrait"><div><strong>R-02 代表写真（縦4:5）</strong>川島代表ご本人の写真・掲載承認後に配置<br>※公開時、写真がなければこの枠は出しません</div></div></div>
    <div class="half-copy gate" data-gate="代表ご本人の承認待ち（編集原稿）">
      <p class="section-kicker">MESSAGE FROM CEO <span>代表メッセージ</span></p>
      <h2 class="section-title" id="message-title">最初から、何でもできる<br>必要はありません。</h2>
      <p style="font-weight:700;color:var(--blue);font-size:15px">一人ひとりが、自分の仕事を増やしていける会社に。</p>
      <p>私自身、18歳でこの業界に入り、現場で仕事を覚えるところから始めました。一度は会社を離れましたが、その後また戻り、現場、管理、取引先とのやり取りを経験してきました。今は、働く人それぞれに違う大変さがあることを忘れずに、会社をつくっていきたいと思っています。</p>
      <p>最初から何でもできる人だけを求めているわけではありません。分からないことを聞き、自分でも考え、少しずつできることを増やしてほしい。昨日できなかったことができるようになる。その積み重ねを大切にしたいと思っています。</p>
      <p>仕事だけが人生のすべてではありません。だからこそ、久留米興業で過ごす時間が、その人の技術や経験になり、いつか「ここで働いて良かった」と思ってもらえる会社を目指します。</p>
      <p style="font-weight:700;color:var(--navy);margin-top:22px">代表取締役　川島 和範</p>
      <a class="text-link" href="@R@people/index.html#people-ceo">代表をもっと知る <span aria-hidden="true">↗</span></a>
    </div>
  </div>
</section>

<!-- 03 CAREER PATH｜方式B：CMS 761 Flow Cards ×2（営業・現場）＋ CSS。切替はアンカー（タブUIは使わない） -->
<section class="section bg-soft" id="recruit-career" aria-labelledby="career-title" data-cms-id="761x2" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">CAREER PATH <span>久留米興業で歩むキャリア</span></p><h2 class="section-title" id="career-title">仕事を覚えるほど、<br>任される仕事が変わっていく。</h2><p class="section-heading-desc" style="max-width:700px">同じ「未経験」でも、スタートの仕方や成長の道筋は職種によって違います。ここでは、実際のヒアリングをもとに、久留米興業で仕事を覚えていく過程をご紹介します。年数は標準的な到達保証ではなく、仕事の習得に応じた目安です。</p></div>
    <div class="career-switch" aria-label="職種を選ぶ"><a href="#career-sales">営業職</a><a href="#career-field">現場職</a></div>
    <div class="career">
      <div class="career-col reveal" id="career-sales" style="scroll-margin-top:96px"><small>SALES</small><h3>営業職</h3>
        <ol class="timeline">
          <li><span class="when">入社初日〜1週間</span><h4>仕事の入口を知る</h4><p>PCの設定など準備をした後、先輩に同行し、取引先や現場を訪問。複数の先輩の仕事を見ながら、業界特有の用語や仕事の流れに触れます。</p></li>
          <li><span class="when">入社〜3か月</span><h4>現場と人の関係を覚える</h4><p>先輩同行を基本に、現場でどんな作業が行われ、誰がどの役割を担うのかを学びます。</p></li>
          <li><span class="when">3か月以降</span><h4>少しずつ任される範囲を広げる</h4><p>現地調査、材料の運搬、取引先との会議、緊急対応の補助などに関わり、できることを増やします。</p></li>
          <li><span class="when">半年〜1年を目指す姿</span><h4>現場と取引先の橋渡しに</h4><p>翌日の段取りの補助や社内外の情報共有に携わり、現場と営業をつなぐ役割を担うことを目指します。</p></li>
          <li><span class="when">その先</span><h4>案件を任せられる人へ</h4><p>見積、取引先との打ち合わせ、金銭・外注手配の調整、資格取得などを通して、案件を主体的に進める力を身につけます。</p></li>
        </ol></div>
      <div class="career-col is-field reveal gate" id="career-field" style="scroll-margin-top:96px" data-gate="現場職：具体的な期間・到達基準はヒアリング後に追記"><small>FIELD WORK</small><h3>現場職</h3>
        <ol class="timeline">
          <li><span class="when">入社直後</span><h4>まずは現場を見る・知る</h4><p>入社初期から現場へ入り、作業の流れ、安全上の注意点、道具や機械の使われ方を知るところから始まります。</p></li>
          <li><span class="when">仕事を覚える段階</span><h4>一つずつできることを増やす</h4><p>周囲の作業を見ながら、補助的な作業や道具の扱いを覚え、担当できる範囲を広げていきます。</p></li>
          <li><span class="when">経験を積んだ先</span><h4>次の工程を考えられる人へ</h4><p>「この後に何が必要か」を見ながら動けることが、成長を測る一つの目安になります。</p></li>
          <li><span class="when">さらに先</span><h4>資格や現場の役割を広げる</h4><p>重機に関わる資格や、現場の副責任者に近い業務を目指せる可能性があります。個人の適性・取得要件により異なります。</p></li>
        </ol></div>
    </div>
  </div>
</section>

<!-- 04 GROWTH & EVALUATION｜方式B：CMS 787 Text Two ＋ 22 Table（年収表は承認まで描画しない） -->
<section class="section" id="recruit-income" aria-labelledby="income-title" data-cms-id="787,22" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">GROWTH &amp; EVALUATION <span>キャリアと評価</span></p><h2 class="section-title" id="income-title">年数だけではなく、<br>できるようになった仕事を見ていく。</h2><p class="section-heading-desc" style="max-width:700px">久留米興業では、任せられる仕事の範囲や取引先・現場からの評価、取得した資格などをもとに、一人ひとりの成長を見ていく考えです。入社直後にすべての成果を求めるのではなく、その段階で何を身につけたかを大切にします。</p></div>
    <div class="text-two reveal">
      <div class="info-card" style="background:#f4f6f8"><small>SALES</small><h3>営業職の評価</h3><p>仕事を覚える姿勢や勤務態度から始まり、取引先との関係、現場との連携、見積・提案能力、資格、成果へ。担当できることが増える過程を評価します。</p></div>
      <div class="info-card is-blue" style="background:#f4f6f8"><small>FIELD WORK</small><h3>現場職の評価</h3><p>任せられる作業の幅、次の工程を考える力、職長など現場の責任者からの評価が、成長を見るうえでの重要な要素になります。</p></div>
    </div>
    <p class="gate review-only" data-gate="昇給の表現を統一してから公開" style="margin-top:28px;font-size:13px">昇給：<span class="tbd">【要確認】ヒアリングでは「年1回・7月」、現行の公式採用ページでは「習熟度に応じ随時昇給」。どちらの表現にするか確定してください。</span></p>
    <div class="gate review-only table-wrap" data-gate="年収例：内訳の裏付けまで非公開" style="margin-top:40px">
      <table class="spec-table"><caption class="caption" style="caption-side:top;text-align:left;margin-bottom:8px">年収例（承認後に掲載する形式）</caption>
        <thead><tr><th scope="col">職種・モデル</th><th scope="col">年収例</th><th scope="col">仕事・能力の説明</th></tr></thead>
        <tbody>
          <tr><td>営業A｜未経験入社2年目</td><td class="tbd">【要確認：現行求人に500万円の記載】</td><td>任される業務、資格・手当との関係を確認</td></tr>
          <tr><td>営業B｜経験者</td><td class="tbd">【要確認：現行求人に750万円の記載】</td><td>役割・担当案件・資格を確認</td></tr>
          <tr><td>現場職のモデル</td><td class="tbd">【要確認：金額・給与形態】</td><td>作業範囲・資格・役割の差を確認</td></tr>
        </tbody></table>
    </div>
    <div class="cta-row"><a class="text-link" href="@R@work-environment/index.html#environment-benefits">働く環境と福利厚生を見る <span aria-hidden="true">↗</span></a></div>
  </div>
</section>

<!-- 05 WORK ENVIRONMENT への動線｜方式B：CMS 54 Half ＋ 90 Btn Text -->
<section class="section bg-surface" id="recruit-workstyle" aria-labelledby="rws-title" data-cms-id="54,90" data-implementation="B">
  <div class="wrap half reveal">
    <div class="half-media"><img src="{P}office.jpg" alt="事務所で打ち合わせをする社員たち" loading="lazy"></div>
    <div class="half-copy"><p class="section-kicker">WORK ENVIRONMENT <span>労働環境</span></p><h2 class="section-title" id="rws-title">働く時間も、働く場所も、<br>知ってから選んでほしい。</h2>
      <p>土木の仕事には、早朝の出発や夏場の暑さなど、現場ならではの大変さがあります。一方で、久留米興業では働く人の負担や生活にも目を向け、働き方を見直してきました。勤務時間や休日、福利厚生、実際の仕事の様子を、良い部分も大変な部分も含めてご紹介します。</p>
      <a class="btn btn-dark" href="@R@work-environment/index.html" style="margin-top:10px">労働環境を見る <span aria-hidden="true">↗</span></a></div>
  </div>
</section>

<!-- 06 OPEN POSITIONS｜方式B：CMS 54 Half ×2（職種カード）＋ 22 Table ＋ CSS -->
<section class="section" id="recruit-openings" aria-labelledby="open-title" data-cms-id="54x2,22" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">OPEN POSITIONS <span>募集職種</span></p><h2 class="section-title" id="open-title">あなたが関わりたい仕事は、<br>どちらですか。</h2><p class="section-heading-desc" style="max-width:700px">久留米興業には、工事を支えるさまざまな役割があります。取引先と現場をつなぐ営業職と、施工を担う現場職。それぞれの仕事内容や勤務条件をご確認ください。</p></div>
    <div class="card-grid is-2">
      <article class="link-card reveal" style="background:#f4f6f8" id="opening-sales">
        <div class="lc-media"><img src="{P}office.jpg" alt="事務所で打ち合わせをする営業職" loading="lazy" style="object-position:50% 40%"></div>
        <div class="lc-body"><small>SALES</small><h3>営業職</h3><p>工事の相談を受け、現地調査、見積、材料・日程の調整まで。人との関係づくりを、インフラ工事の専門性へと広げる仕事です。</p>
          <div class="gate" data-gate="掲載前に最新の求人票と照合"><table class="spec-table" style="font-size:12.5px;margin-bottom:18px"><tbody>
            <tr><th scope="row">雇用形態</th><td>正社員</td></tr>
            <tr><th scope="row">勤務地</th><td>東京都世田谷区北烏山6丁目26-28</td></tr>
            <tr><th scope="row">勤務時間</th><td>8:00〜17:00</td></tr>
            <tr><th scope="row">給与</th><td>月給32万円〜</td></tr>
            <tr><th scope="row">休日</th><td>年間休日127日以上<span class="review-only tbd"><br>【要確認】過去の求人票では130日</span></td></tr>
            <tr><th scope="row">昇給・賞与</th><td>昇給年1回・賞与年2回</td></tr>
          </tbody></table>
          <p class="review-only tbd" style="font-size:12px">【要確認】休日出勤の可能性・運転免許要件の記載、採用予定人数（現行「3〜5名」とプロジェクト目標「1名」）</p></div>
          {ext(SALES_JOB, '営業職の募集要項（CAREECON） <span aria-hidden="true">↗</span>', 'btn btn-dark')}</div>
      </article>
      <article class="link-card reveal" style="background:#f4f6f8" id="opening-field" data-delay="1">
        <div class="lc-media"><img src="{P}process-remove.jpg" alt="舗装の撤去作業を行う現場" loading="lazy"></div>
        <div class="lc-body"><small>FIELD WORK</small><h3>現場職</h3><p>舗装・水道・土木工事の現場で、作業の流れと技術を一つずつ習得する仕事です。自分たちが関わった道が、街の日常につながります。</p>
          <div class="gate review-only" data-gate="現場職の募集要項：現行求人票の受領待ち（公開時は非表示）"><p class="tbd" style="font-size:12.5px;margin:0 0 18px">【要確認】雇用形態／勤務地／勤務時間・休憩／休日／給与形態（過去資料に日給14,000〜21,000円の記載。現行条件として扱わない）／手当／試用期間／応募資格／寮の対象</p></div>
          {ext(OFFICIAL_RECRUIT, '現場職の募集要項（公式採用ページ） <span aria-hidden="true">↗</span>', 'btn btn-dark')}</div>
      </article>
    </div>
    <p class="fine-note">応募は各職種の正式な求人ページで受け付けています。最新の条件は求人ページをご確認ください。</p>
  </div>
</section>

<!-- 07 Q&A｜候補：方式B（カタログの faq_accordion をCSSで調整）。不可なら方式C（独自HTML＋CSS、JS別）。本デモは details/summary でJSなしでも開閉 -->
<section class="section bg-soft" id="recruit-faq" aria-labelledby="faq-title" data-cms-id="faq_accordion" data-implementation="B候補/C">
  <div class="wrap" style="max-width:880px">
    <div class="section-heading reveal"><p class="section-kicker">Q&amp;A <span>よくある質問</span></p><h2 class="section-title" id="faq-title">応募前に、気になること。</h2></div>
    <div class="reveal">{faq_html()}</div>
  </div>
</section>

<!-- 08 CTA｜方式B：CMS 90 Btn Text ＋ 23 Btn -->
<section class="recruit-section" id="recruit-cta" aria-labelledby="rcta-title" data-cms-id="90,23" data-implementation="B">
  <div class="wrap recruit-inner"><div class="recruit-heading reveal"><p class="section-kicker section-kicker-light">ENTRY</p><h2 id="rcta-title">少しでも気になったら、<br>まずは仕事を知るところから。</h2><p>募集要項を読んで、働くイメージを確かめてください。仕事内容や応募条件で気になることがあれば、お問い合わせいただけます。</p></div>
  <div class="recruit-entry-grid"><a class="recruit-entry reveal" href="#recruit-openings"><span class="entry-icon">01</span><div><small>ENTRY</small><h3>募集要項・応募へ進む</h3><p>営業職・現場職それぞれの正式な求人ページへ。</p></div><b aria-hidden="true">↓</b></a><a class="recruit-entry reveal" href="@R@people/index.html"><span class="entry-icon">02</span><div><small>PEOPLE</small><h3>働くメンバーを見る</h3><p>どんな人が、どんなキャリアを歩んでいるか。</p></div><b aria-hidden="true">↗</b></a><a class="recruit-entry reveal" href="@R@work-environment/index.html"><span class="entry-icon">03</span><div><small>WORK ENVIRONMENT</small><h3>労働環境を見る</h3><p>1日の仕事、福利厚生、会社の取り組み。</p></div><b aria-hidden="true">↗</b></a></div></div>
</section>
''' + faq_jsonld()


def build():
    return page("recruit", "採用情報｜株式会社久留米興業",
                "これからの自分に、街を支える仕事を。久留米興業の営業職・現場職のキャリア、評価の考え方、募集要項をご紹介します。",
                1, BODY, crumb="採用情報")

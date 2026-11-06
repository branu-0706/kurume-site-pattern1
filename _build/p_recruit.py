from common import *

P = "@R@assets/photos/"

# Q&A：求人票（求人ボックス 2026-11-05版）と社員インタビューに記載がある内容のみ
FAQ = [
    ("仕事内容", [
        ("建設業の経験がなくても応募できますか？", "営業職・現場職とも、学歴や業界経験は問いません。営業職は異業種からの転職者が多く、入社後は先輩社員に同行しながら仕事を覚えていきます。現場職は、道具の名前や資材の準備、清掃など、取り組みやすい仕事から始めます。どちらも普通自動車免許（AT限定可）が必要です。", None),
        ("営業職はいきなり一人で取引先を担当しますか？", "いいえ。入社後はまず先輩社員への同行から始めます。複数の先輩について「取引先によってどう対応するのか」「現場では何を確認するのか」を実際の仕事を見ながら覚え、習熟度に合わせて担当できる仕事を増やしていきます。", None),
        ("現場作業は一人で任されることがありますか？", "ありません。現場は基本的に7〜12名程度の自社チームで動きます。未経験の方を一人で配置したり、分からないまま作業を任せたりすることはなく、先輩社員が近くについて道具の使い方や安全上の注意点を教えます。", "チーム人数：公式サイトは「班長以下7〜8名」。表記の統一を確認"),
    ]),
    ("成長・評価", [
        ("どのような仕事ぶりが評価されますか？", "入社して最初のうちは、仕事を覚えようとする姿勢や勤務態度を見ます。仕事に慣れてきたら、取引先や現場との関係づくり、調整力、さらに見積・提案、資格、成果へと評価の対象が広がります。年数だけでなく、任せられる仕事がどれだけ増えたかを見ていきます。", None),
        ("資格の取得は支援してもらえますか？", "はい。現場職は、準中型・中型・大型自動車免許、車両系建設機械、1級・2級土木施工管理技士などの取得費用（受験料・講習費・交通費など）を会社が負担します。営業職にも資格取得支援制度と資格手当があります。", "営業職の支援範囲（全額負担か）を確認"),
        ("本当に未経験から年収は上がりますか？", "現場職では、未経験で入社して3年で資格を取り、年収を100万円以上上げた先輩がいます。資格を取ってできる仕事が増えれば、資格手当や昇給に反映されます。年収モデル例は上の表をご覧ください。", "求人票記載の実例。本人・内訳の確認推奨"),
    ]),
    ("働き方・応募", [
        ("現場職の仕事は体力的に大変ですか？", "楽な仕事ではありません。夏場の暑さや夜間の作業、その日の作業をその日のうちに終わらせる厳しさがあります。一方で、予定より早く作業が終われば15時ごろでも上がることができ、その日の日給は全額支給されます。詳しくは<a href=\"@R@work-environment/index.html#environment-day\">労働環境ページ</a>で紹介しています。", None),
        ("雨で作業が中止になると、給料は減りますか？", "減りません。雨で現場が早く切り上がった日や、予定より早く終わった日も、その日の日給は全額支給します。", None),
        ("夜勤はどれくらいありますか？", "現場や時期によって、月4回程度（週1回あるかないか）、21:00〜翌6:00の夜勤があります。夜間の道路規制に合わせて行う工事があるためです。夜勤の翌日は体を休められるよう、シフトを調整します。", None),
        ("遠方からの応募は可能ですか？", "可能です。鍵付きの個室寮があります（寮費月3万円・水道光熱費5千円、各部屋に冷暖房・テレビ等）。空室や入寮条件は応募時にご確認ください。", "寮の空室・現在の料金を確認"),
        ("応募前に、話を聞くことはできますか？", "できます。ご希望の方には、カジュアル面談（履歴書不要）や電話面談（15分〜）の場を設けています。会社のこと、取引の実績、将来の年収モデルなどをお話しします。", None),
    ]),
]


def faq_html():
    out = []
    for cat, items in FAQ:
        rows = []
        for q, a, gate in items:
            attr = f' class="gate" data-gate="{gate}"' if gate else ""
            rows.append(f'<details{attr}><summary>{q}</summary><div class="answer"><p style="margin:0">{a}</p></div></details>')
        out.append(f'<div class="faq-group"><h3>{cat}</h3><div class="faq">{"".join(rows)}</div></div>')
    return "".join(out)


def faq_jsonld():
    import json, re
    ents = []
    for _, items in FAQ:
        for q, a, gate in items:
            ents.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}})
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": ents}, ensure_ascii=False) + "</script>"


BODY = f'''
<!-- 01 RECRUIT HERO｜方式B：CMS 734 H1 Center ＋ CSS -->
<section class="page-hero" id="recruit-hero" aria-labelledby="recruit-title" data-cms-id="734" data-implementation="B">
  <div class="page-hero-img" style="background-image:url('{P}field-crew-hq.jpg');background-position:55% 60%" role="img" aria-label="路盤をつくる久留米興業の現場職"></div>
  <div class="wrap">
    <p class="eyebrow anim-enter"><span class="line"></span>RECRUIT / JOIN OUR TEAM</p>
    <h1 id="recruit-title" class="anim-enter" style="--delay:.1s">これからの自分に、<br>街を支える仕事を。</h1>
    <p class="lead anim-enter" style="--delay:.2s">道路や水道など、毎日の暮らしに欠かせないインフラを支える久留米興業。私たちの仕事には、現場で技術を磨く人も、取引先と現場をつなぐ人も必要です。今できることだけでなく、これから身につける力を大切にしながら、一緒に歩んでいきませんか。</p>
  </div>
</section>
<!--CRUMB-->
<!-- ページ内目次｜方式B：CMS multiple_btns（ID要確認）＋ CSS（sticky）。JSなし -->
<nav class="page-nav" aria-label="このページの目次"><ul class="wrap">
  <li><a href="#recruit-facts">数字で見る</a></li>
  <li><a href="#recruit-anxiety">応募前の不安</a></li>
  <li><a href="#recruit-career">キャリア</a></li>
  <li><a href="#recruit-first">最初の1か月</a></li>
  <li><a href="#recruit-income">評価と収入</a></li>
  <li><a href="#recruit-openings">募集要項</a></li>
  <li><a href="#recruit-flow">選考の流れ</a></li>
  <li><a href="#recruit-faq">Q&amp;A</a></li>
</ul></nav>

<!-- 数字で見る｜方式B：CMS 16 Card Four ＋ CSS。良い数字だけでなく、大変さの数字も並べる -->
<section class="section" id="recruit-facts" aria-labelledby="facts-title" data-cms-id="16" data-implementation="B">
  <div class="wrap">
    <div class="section-heading section-heading-split reveal"><div><p class="section-kicker">FACTS <span>数字で見る久留米興業</span></p><h2 class="section-title" id="facts-title">良いことも、大変なことも、<br>数字で先にお伝えします。</h2></div><p class="section-heading-desc">条件は2026年11月時点のものです。グレーの枠は、仕事の大変な面にあたる数字です。</p></div>
    <div class="facts reveal">
      <div class="fact"><small>SALES / 月給</small><strong>32<span>万円〜</span></strong><p>未経験でも同じスタート。経験・資格を考慮して決定。</p></div>
      <div class="fact"><small>SALES / 年間休日</small><strong>130<span>日</span></strong><p>土日祝休み。飛び込み営業・個人ノルマなし。</p></div>
      <div class="fact"><small>FIELD / 日給</small><strong>14,000<span>円〜</span></strong><p>雨や早上がりの日も全額支給。月給換算35.8万円〜。</p></div>
      <div class="fact"><small>FIELD / 資格取得費用</small><strong>全額<span>会社負担</span></strong><p>免許・車両系建設機械・施工管理技士など。</p></div>
      <div class="fact"><small>FIELD / チーム</small><strong>7〜12<span>名</span></strong><p>未経験の方を一人で現場に置くことはありません。</p></div>
      <div class="fact"><small>LIFE / 寮費</small><strong>3<span>万円/月</span></strong><p>鍵付き個室。水道光熱費は月5千円。</p></div>
      <div class="fact is-honest"><small>FIELD / 夜勤</small><strong>月4<span>回程度</span></strong><p>21:00〜翌6:00。夜間の道路規制に合わせた工事。翌日は休めるようにシフトを調整。</p></div>
      <div class="fact is-honest"><small>FIELD / 夏の暑さの対策</small><strong>1日2<span>回のドリンク支給</span></strong><p>夏場は暑さの中での屋外作業があります。10時と15時の小休憩で、会社から冷えたドリンクを支給。</p></div>
    </div>
  </div>
</section>

<!-- 応募前の不安と実際｜方式B：CMS 42 Card Three（2列）＋ CSS -->
<section class="section bg-soft" id="recruit-anxiety" aria-labelledby="anx-title" data-cms-id="42" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">BEFORE YOU APPLY <span>応募前の不安と、実際のところ</span></p><h2 class="section-title" id="anx-title">その不安、<br>社員の言葉と制度でお答えします。</h2><p class="section-heading-desc" style="max-width:720px">建設業への転職でよく聞く不安に、実際に働く社員の言葉と会社の制度でお答えします。良いことだけでなく、大変なことも隠しません。</p></div>
    <div class="anx-grid">
      <article class="anx reveal"><div class="anx-q"><small>不安 01</small><p>未経験で、本当についていける？</p></div><div class="anx-a"><small>実際は</small><h3>営業の多くは異業種から。現場は「カラーコーンを並べる」ところから始めます。</h3><p>営業職の3名は、お茶の営業、広告代理店、土木と関係のない専攻からの入社です。最初は先輩への同行から。現場職は道具の名前や安全ルール、資材準備や清掃など、取り組みやすい仕事から覚えます。</p><blockquote>例えば、カラーコーンを並べるとか、そういうところからでもいいんです。自分もそうでした。<cite>— 奥居さん（現場職・建築から転職）</cite></blockquote><a class="anx-link" href="#recruit-first">入社後の最初の1か月を見る ↓</a></div></article>
      <article class="anx reveal" data-delay="1"><div class="anx-q"><small>不安 02</small><p>職人さんや先輩が怖そう…</p></div><div class="anx-a"><small>実際は</small><h3>「見た目は怖い。でも話すと優しい人が多い」と、社員自身が話しています。</h3><p>入社したばかりの頃は、社長や先輩が先に声をかけてくれた、という声があります。現場では、分からないことは聞けば答えてもらえます。</p><blockquote>社長や先輩たちが本当によく見てくれていて、悩む前に『大丈夫か？』と声をかけてくれた。<cite>— 高畑さん（営業職・新卒入社）</cite></blockquote><a class="anx-link" href="@R@people/index.html">働くメンバーを見る ↗</a></div></article>
      <article class="anx reveal"><div class="anx-q"><small>不安 03</small><p>建設業は休みが少ないのでは？</p></div><div class="anx-a"><small>実際は</small><h3>営業職は土日祝休み・年間休日130日。現場職は第2土曜・日曜・祝日と長期休暇。</h3><p>現場職はGW・夏季・年末年始に、それぞれ6〜9日程度の連休があります。営業の社員は、仕事帰りにジムへ通うなど自分の時間も大切にしています。代表自身、休みの少なさから一度会社を離れた経験があり、働き方の見直しを進めてきました。</p><a class="anx-link" href="@R@work-environment/index.html#environment-roles">職種ごとの休日を見る ↗</a></div></article>
      <article class="anx reveal" data-delay="1"><div class="anx-q"><small>不安 04</small><p>転職で、給料が下がらない？</p></div><div class="anx-a"><small>実際は</small><h3>営業職は月給32万円以上、現場職は日給14,000円から。雨の日も早上がりの日も日給は全額です。</h3><p>現場職は各種手当を含めて、初月から月収35万円以上を目指せます。営業職の年収500万円は「入社すれば自動的に」ではなく、任される仕事が増えた先の目標です。</p><a class="anx-link" href="#recruit-income">評価と収入を見る ↓</a></div></article>
      <article class="anx reveal"><div class="anx-q"><small>不安 05</small><p>営業はノルマに追われる？</p></div><div class="anx-a"><small>実際は</small><h3>新規開拓の飛び込み営業や、個人ノルマはありません。</h3><p>既存の取引先から工事の相談を受け、現場を確認し、見積や段取りを整えるのが中心です。評価するのは売上だけでなく、約束や期限を守ること、正確な書類、取引先や現場と協力して仕事を進めることです。</p><blockquote>やる気さえあれば、どんなバックグラウンドの人でも必ず活躍できる世界ですよ。<cite>— 根岸さん（営業職から現場代理人・異業種から転職）</cite></blockquote></div></article>
      <article class="anx is-honest reveal" data-delay="1"><div class="anx-q"><small>不安 06</small><p>現場は体力的にきつい？</p></div><div class="anx-a"><small>正直に言うと</small><h3>楽な仕事ではありません。だから、負担を分ける仕組みを整えています。</h3><p>夏の暑さ、月4回程度の夜勤、その日の作業をその日のうちに終わらせる厳しさがあります。作業量が多く、休憩の余裕を感じにくい日もあると班長も話しています。会社としては、人を増やして一人あたりの負担を減らし、早く終わった日は早く帰れるようにしています。</p><blockquote>最初から何でもできる必要はありません。……焦ってやらないで、長く続けてもらえればいいんじゃないですか。<cite>— 松野さん（現場の班長・約30年）</cite></blockquote><a class="anx-link" href="@R@work-environment/index.html#environment-honest">大変なことと会社の対応を見る ↗</a></div></article>
      <article class="anx reveal"><div class="anx-q"><small>不安 07</small><p>資格がないと難しい？</p></div><div class="anx-a"><small>実際は</small><h3>入社時に必要なのは普通自動車免許（AT限定可）だけ。資格は入社後に取れます。</h3><p>現場職は、免許や施工管理技士などの取得費用を会社が全額負担します。営業職でも、会社がテキストを用意し、先輩が実務に即して教える中で、1級土木施工管理技士を取った社員がいます。</p></div></article>
      <article class="anx reveal" data-delay="1"><div class="anx-q"><small>不安 08</small><p>いきなり面接は緊張する</p></div><div class="anx-a"><small>実際は</small><h3>履歴書不要のカジュアル面談や、15分からの電話面談ができます。</h3><p>「仕事内容をもっと詳しく知ってから判断したい」という方のための場です。会社のこと、取引の実績、将来の年収モデルをお話しします。遠方の方には、鍵付きの個室寮もあります。</p><a class="anx-link" href="#recruit-flow">選考の流れを見る ↓</a></div></article>
    </div>
  </div>
</section>

<!-- 02 代表採用メッセージ｜方式B：CMS 54 Half ＋ 35 Title Sub ＋ CSS -->
<section class="section" id="recruit-message" aria-labelledby="message-title" data-cms-id="54,35" data-implementation="B">
  <div class="wrap half reveal" style="grid-template-columns:.82fr 1fr">
    <div class="half-media is-portrait"><img src="{P}ceo-portrait.jpg" alt="代表取締役 川島 和範" loading="lazy"><p class="caption">代表取締役　川島 和範</p></div>
    <div class="half-copy gate" data-gate="代表インタビュー（2026-07-17再構成）に基づく編集原稿：本人承認待ち">
      <p class="section-kicker">MESSAGE FROM CEO <span>代表メッセージ</span></p>
      <h2 class="section-title" id="message-title">最初から、何でもできる<br>必要はありません。</h2>
      <p style="font-weight:700;color:var(--blue);font-size:15px">一人ひとりが、自分の仕事を増やしていける会社に。</p>
      <p>私自身、18歳でこの業界に入り、現場作業の見習いから始めました。一度は会社を離れましたが、その後また戻り、現場、管理、取引先とのやり取りを経験してきました。だからこそ、現場にも、営業にも、管理する側にも、それぞれ違った大変さがあることは分かっているつもりです。</p>
      <p>求めているのは、経験よりも、自分で考えて動ける人です。最初から正しい判断ができなくても構いません。分からないことを聞き、自分でも考え、一つずつできる仕事を増やしてほしい。仕事を覚え、人をまとめられるようになれば、その働きは会社として評価したいと思っています。</p>
      <p>仕事だけが人生ではありません。家族との時間を大切にしたい人もいれば、仕事の後にやりたいことがある人もいます。いろいろな個性を持つ人が、それぞれの役割を見つけ、最終的に「ここで働いて良かった」と思える会社を目指しています。</p>
      <p style="font-weight:700;color:var(--navy);margin-top:22px">代表取締役　川島 和範</p>
      <a class="text-link" href="@R@people/index.html#people-ceo">代表の歩みを読む <span aria-hidden="true">↗</span></a>
    </div>
  </div>
</section>

<!-- 03 CAREER PATH｜方式B：CMS 761 Flow Cards ×2（営業・現場）＋ CSS。切替はアンカー -->
<section class="section bg-soft" id="recruit-career" aria-labelledby="career-title" data-cms-id="761x2" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">CAREER PATH <span>久留米興業で歩むキャリア</span></p><h2 class="section-title" id="career-title">仕事を覚えるほど、<br>任される仕事が変わっていく。</h2><p class="section-heading-desc" style="max-width:700px">同じ「未経験」でも、スタートの仕方や成長の道筋は職種によって違います。年数は到達を約束するものではなく、仕事の習得に応じた目安です。</p></div>
    <div class="career-switch" aria-label="職種を選ぶ"><a href="#career-sales">営業職</a><a href="#career-field">現場職</a></div>
    <div class="career">
      <div class="career-col reveal" id="career-sales" style="scroll-margin-top:96px"><small>SALES</small><h3>営業職</h3>
        <ol class="timeline">
          <li><span class="when">入社直後</span><h4>先輩に同行して、仕事の入口を知る</h4><p>複数の先輩について取引先や現場を訪問。「取引先によってどう対応するのか」「現場では何を確認するのか」「工事はどんな流れで進むのか」を、実際の仕事を見ながら覚えます。</p></li>
          <li><span class="when">仕事に慣れてきたら</span><h4>担当できる仕事を増やす</h4><p>現地調査、取引先への対応、現場との調整など、習熟度に合わせて担当範囲を広げます。</p></li>
          <li><span class="when">1〜3年ほど</span><h4>取引先と現場をつなぐ人に</h4><p>取引先との関係づくり、現場社員とのコミュニケーション、工事を円滑に進める調整力を身につけます。</p></li>
          <li><span class="when">その先</span><h4>「この案件なら任せられる」人へ</h4><p>一人での打ち合わせ、見積作成、材料や協力会社の手配、資格の取得。工事の進み方を理解して先回りして調整できるようになると、任される範囲と収入が広がります。</p></li>
          <li><span class="when">さらに先</span><h4>現場代理人や役職へ</h4><p>資格を取り、公共工事の現場代理人として役割を広げた先輩もいます。<a href="@R@people/index.html#member-negishi">根岸さんの例を見る</a></p></li>
        </ol></div>
      <div class="career-col is-field reveal" id="career-field" style="scroll-margin-top:96px"><small>FIELD WORK</small><h3>現場職</h3>
        <ol class="timeline">
          <li><span class="when">入社直後</span><h4>道具・安全・作業の流れを覚える</h4><p>先輩社員と一緒に現場へ入り、道具の名前、安全ルール、作業の流れを覚えます。清掃、資材準備、作業補助など、取り組みやすい仕事から始めます。</p></li>
          <li><span class="when">半年〜1年</span><h4>担当できる作業を増やす</h4><p>現場の流れを理解し、舗装作業や水道工事に伴う道路復旧など、担当できる作業を増やします。必要な資格の取得にも挑戦します。</p></li>
          <li><span class="when">3年目以降</span><h4>責任のある仕事を任される</h4><p>重機や車両の運転、後輩への指導、現場の段取りなど、より責任のある仕事を担当します。</p></li>
          <li><span class="when">その先</span><h4>職長・施工管理・現場代理人へ</h4><p>資格や経験を積み、現場をまとめる立場を目指せます。</p></li>
        </ol></div>
    </div>
  </div>
</section>


<!-- 最初の1か月｜方式B：CMS 761 Flow Cards ×2 ＋ CSS -->
<section class="section" id="recruit-first" aria-labelledby="first-title" data-cms-id="761x2" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">YOUR FIRST MONTH <span>入社してからの最初の1か月</span></p><h2 class="section-title" id="first-title">入社してすぐに、<br>一人で任せることはありません。</h2><p class="section-heading-desc" style="max-width:700px">入社直後に何をするのか。営業職と現場職、それぞれの最初の日々をご紹介します。</p></div>
    <div class="career">
      <div class="career-col reveal"><small>SALES</small><h3>営業職の最初の1か月</h3>
        <ol class="timeline">
          <li><span class="when">初日</span><h4>準備をして、先輩と一緒に動く</h4><p>パソコンの設定など仕事の準備をしたあと、先輩に同行します。</p></li>
          <li><span class="when">最初の数週間</span><h4>先輩が1人つく</h4><p>取引先や現場を一緒に訪問します。分からないことは、その場でも電話でも、すぐに聞けます。</p></li>
          <li><span class="when">1か月ごろ</span><h4>現場を見る</h4><p>根岸さんは、入社1か月後には現場を見ていたそうです。工事でどんな作業が行われ、誰がどの役割を担うのかを知っていきます。</p></li>
          <li><span class="when">それ以降</span><h4>同行を続けながら、できることを増やす</h4><p>少なくとも3か月程度は同行を基本に、習熟度に合わせて担当を広げます。</p></li>
        </ol></div>
      <div class="career-col is-field reveal" data-delay="1"><small>FIELD WORK</small><h3>現場職の最初の1か月</h3>
        <ol class="timeline">
          <li><span class="when">初日</span><h4>8:30に本社集合、チームで現場へ</h4><p>先輩社員と一緒に現場へ移動します。現場は7〜12名程度の自社チームです。</p></li>
          <li><span class="when">最初の数日</span><h4>道具の名前と安全ルール</h4><p>カラーコーンや規制材の設置、資材の準備、清掃など、取り組みやすい仕事から。安全上の注意点を一つずつ覚えます。</p></li>
          <li><span class="when">慣れてきたら</span><h4>班長の動きを見て合わせる</h4><p>班の中では役割分担ができています。分からないことは聞き、周りの動きを見ながら自分の役割を覚えます。</p></li>
          <li><span class="when">1か月ごろ</span><h4>「毎日来ること」が第一歩</h4><p>班長の松野さんは、まず毎日現場に出て流れを知ることが大切だと話します。一度に全部は求めません。</p></li>
        </ol></div>
    </div>
    <p class="fine-note">個人の経験をもとにした目安です。入社時期や担当によって異なります。</p>
  </div>
</section>

<!-- 04 GROWTH & INCOME｜方式B：CMS 787 Text Two ＋ 22 Table -->
<section class="section bg-soft" id="recruit-income" aria-labelledby="income-title" data-cms-id="787,22" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">GROWTH &amp; INCOME <span>評価と収入</span></p><h2 class="section-title" id="income-title">年数だけではなく、<br>できるようになった仕事を見ていく。</h2><p class="section-heading-desc" style="max-width:700px">入社直後からいきなり成果を求めることはありません。仕事を覚える段階に合わせて、評価のポイントも変わっていきます。特に大切にしているのは、「現場で何か困っていないか」「次に何が必要になるのか」と周囲に目を向け、言われる前に気づいて動けることです。</p></div>
    <div class="text-two reveal">
      <div class="info-card"><small>SALES</small><h3>営業職：年収500万円は、成長の先にある目標</h3><p>未経験でも月給32万円以上からスタート。ただし、入社すれば自動的に年収500万円になるわけではありません。取引先と一人で打ち合わせができる、見積を作成できる、材料や協力会社を手配できる、資格を取る。そうした仕事ができるようになるほど、評価される範囲が広がり、その先に年収500万円という目標があります。</p></div>
      <div class="info-card is-blue"><small>FIELD WORK</small><h3>現場職：資格とできる作業が、収入につながる</h3><p>未経験でも日給14,000円から。各種手当を含めて初月から月収35万円以上を目指せます。資格を取り、できる作業が増えれば資格手当や昇給に反映。未経験で入社して3年で資格を取り、年収を100万円以上上げた先輩もいます。</p></div>
    </div>
    <div class="table-wrap reveal gate" data-gate="求人票（2026-11-05）記載のモデル例。内訳の確認推奨" style="margin-top:40px">
      <table class="spec-table"><caption class="caption" style="caption-side:top;text-align:left;margin-bottom:8px">現場職の年収モデル例（経験・資格・担当により異なります）</caption>
        <thead><tr><th scope="col">モデル</th><th scope="col">年収例</th><th scope="col">役割・資格</th></tr></thead>
        <tbody>
          <tr><td>入社1年目（未経験）</td><td>年収480万円〜</td><td>先輩と一緒に、作業補助から</td></tr>
          <tr><td>入社3年目</td><td>年収550万円</td><td>中型自動車免許を取得</td></tr>
          <tr><td>入社5〜7年目</td><td>年収700万円</td><td>現場代理人</td></tr>
        </tbody></table>
    </div>
    <p class="fine-note">昇給：年1回（現場職は作業の習熟に応じて随時昇給）。賞与：年2回。</p>
    <div class="cta-row"><a class="text-link" href="@R@work-environment/index.html#environment-benefits">福利厚生と手当を見る <span aria-hidden="true">↗</span></a></div>
  </div>
</section>

<!-- 05 WORK ENVIRONMENT への動線｜方式B：CMS 54 Half ＋ 90 Btn Text -->
<section class="section" id="recruit-workstyle" aria-labelledby="rws-title" data-cms-id="54,90" data-implementation="B">
  <div class="wrap half reveal">
    <div class="half-media"><img src="{P}office-wide.jpg" alt="事務所で仕事をする社員たち" loading="lazy"></div>
    <div class="half-copy"><p class="section-kicker">WORK ENVIRONMENT <span>労働環境</span></p><h2 class="section-title" id="rws-title">働く時間も、働く場所も、<br>知ってから選んでほしい。</h2>
      <p>土木の仕事には、早朝の出発や夏場の暑さ、夜間の作業など、現場ならではの大変さがあります。一方で、久留米興業では残業のルールや人員体制を見直し、働く人の負担や生活にも目を向けてきました。1日の流れや休日、福利厚生を、良い部分も大変な部分も含めてご紹介します。</p>
      <a class="btn btn-dark" href="@R@work-environment/index.html" style="margin-top:10px">労働環境を見る <span aria-hidden="true">↗</span></a></div>
  </div>
</section>

<!-- 06 OPEN POSITIONS｜方式B：CMS 54 Half ×2（職種カード）＋ 22 Table ＋ CSS -->
<section class="section" id="recruit-openings" aria-labelledby="open-title" data-cms-id="54x2,22" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">OPEN POSITIONS <span>募集要項</span></p><h2 class="section-title" id="open-title">あなたが関わりたい仕事は、<br>どちらですか。</h2><p class="section-heading-desc" style="max-width:700px">取引先と現場をつなぐ営業職と、施工を担う現場職。それぞれの仕事内容と勤務条件です。</p></div>
    <div class="card-grid is-2">
      <article class="link-card reveal" style="background:#f4f6f8" id="opening-sales">
        <div class="lc-body"><small>SALES</small><h3>営業職（法人営業）</h3><p>道路舗装や水道工事が予定どおり進むように、取引先・現場社員・協力会社をつなぐ仕事です。新規開拓の飛び込み営業や個人ノルマはありません。取引先から工事の相談を受け、現場を確認し、見積を作成し、必要な人・材料・日程を整えます。</p>
          <table class="spec-table" style="font-size:12.5px;margin-bottom:18px"><tbody>
            <tr><th scope="row">雇用形態</th><td>正社員</td></tr>
            <tr><th scope="row">勤務地</th><td>東京都世田谷区北烏山6-26-28<br>京王線「千歳烏山駅」徒歩15分／自転車・バイク通勤OK</td></tr>
            <tr><th scope="row">給与</th><td>月給320,000円以上<br>これまでの経験や保有資格を考慮して決定</td></tr>
            <tr><th scope="row">休日</th><td>年間休日130日・土日祝休み</td></tr>
            <tr><th scope="row">手当</th><td>運転無事故手当 月3万円／皆勤手当 月2万円／資格手当</td></tr>
            <tr><th scope="row">待遇</th><td>昇給年1回／賞与年2回／資格取得支援制度／社会保険完備／交通費規定支給／退職金制度／定期健康診断</td></tr>
            <tr><th scope="row">必須</th><td>普通自動車免許（AT限定可）</td></tr>
          </tbody></table>
          <p class="review-only tbd" style="font-size:12px">【要確認】勤務時間が求人ボックス原稿に未記載（CAREECON求人は8:00〜17:00）。CAREECON求人の年間休日127日と、求人ボックスの130日を統一してください。</p>
          {ext(SALES_JOB, '営業職に応募する <span aria-hidden="true">↗</span>', 'btn btn-dark')}</div>
      </article>
      <article class="link-card reveal" style="background:#f4f6f8" id="opening-field" data-delay="1">
        <div class="lc-body"><small>FIELD WORK</small><h3>現場職（建設作業員・土木作業員）</h3><p>東京都内、主に世田谷区周辺の道路舗装工事・水道工事の現場作業です。道具・資材の準備、カラーコーンや規制材の設置、古い舗装の撤去、路盤の整地、アスファルト舗装や転圧の補助、安全確認や誘導など。資格や習熟度に応じて重機・車両の運転も担当します。</p>
          <table class="spec-table" style="font-size:12.5px;margin-bottom:18px"><tbody>
            <tr><th scope="row">雇用形態</th><td>正社員</td></tr>
            <tr><th scope="row">勤務地</th><td>本社集合（東京都世田谷区北烏山6-26-28）後、各現場へ</td></tr>
            <tr><th scope="row">給与</th><td>日給14,000円〜21,000円<br>月給換算 358,000円〜575,000円（基本給＋手当込み）<br>経験やスキルを考慮して決定</td></tr>
            <tr><th scope="row">勤務時間</th><td>8:30〜17:30（実働7.5時間／休憩1.5時間）※現場による<br>早く終われば15時ごろ早上がり（日給は全額支給）<br>現場・時期により月4回程度の夜勤（21:00〜翌6:00）あり</td></tr>
            <tr><th scope="row">休日</th><td>第2土曜日・日曜日・祝日<br>GW・夏季・年末年始（各6〜9日程度の連休）<br>有給休暇・慶弔休暇</td></tr>
            <tr><th scope="row">手当</th><td>運転無事故手当 月3万円／精勤手当 月2万円／資格手当／交通費規定支給（月2万円まで）</td></tr>
            <tr><th scope="row">待遇</th><td>昇給年1回（習熟に応じて随時）／賞与年2回／資格取得費用は会社が全額負担／社会保険完備／退職金制度（勤続3年以上）／鍵付き個室寮／定期健康診断</td></tr>
            <tr><th scope="row">必須</th><td>普通自動車免許（AT限定可）。学歴・職歴・経験は問いません</td></tr>
          </tbody></table>
          {ext(OFFICIAL_RECRUIT, '現場職に応募する <span aria-hidden="true">↗</span>', 'btn btn-dark')}</div>
      </article>
    </div>
    <p class="fine-note">条件は2026年11月時点のものです。最新の条件は各求人ページをご確認ください。</p>
  </div>
</section>

<!-- 07 SELECTION｜方式B：CMS 761 Flow Cards ＋ CSS -->
<section class="section bg-soft" id="recruit-flow" aria-labelledby="flow-title" data-cms-id="761" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">SELECTION <span>選考の流れ</span></p><h2 class="section-title" id="flow-title">いきなり面接が不安な方は、<br>話を聞くところから。</h2></div>
    <ol class="flow reveal">
      <li><span class="num">01</span><h3>応募</h3><p>各求人ページからエントリー。担当者より3営業日以内にご連絡します。</p></li>
      <li><span class="num">02</span><h3>カジュアル面談・電話面談</h3><p>ご希望の方のみ。履歴書不要、電話は15分〜。会社のことや年収モデルをお話しします。</p></li>
      <li><span class="num">03</span><h3>一次面接</h3><p>現場担当または採用担当。これまでの経験よりも「これから」の意欲を重視します。</p></li>
      <li><span class="num">04</span><h3>社長面談</h3><p>最終的な意思確認の場。社長から会社のビジョンを直接お話しします。</p></li>
      <li><span class="num">05</span><h3>採用・入社</h3><p>入社日はご相談に応じます。</p></li>
    </ol>
  </div>
</section>

<!-- 08 Q&A｜候補：方式B（カタログの faq_accordion をCSSで調整）。不可なら方式C。デモは details/summary -->
<section class="section" id="recruit-faq" aria-labelledby="faq-title" data-cms-id="faq_accordion" data-implementation="B候補/C">
  <div class="wrap" style="max-width:880px">
    <div class="section-heading reveal"><p class="section-kicker">Q&amp;A <span>よくある質問</span></p><h2 class="section-title" id="faq-title">応募前に、気になること。</h2></div>
    <div class="reveal">{faq_html()}</div>
  </div>
</section>

<!-- 09 CTA｜方式B：CMS 90 Btn Text ＋ 23 Btn -->
<section class="recruit-section" id="recruit-cta" aria-labelledby="rcta-title" data-cms-id="90,23" data-implementation="B">
  <div class="wrap recruit-inner"><div class="recruit-heading reveal"><p class="section-kicker section-kicker-light">ENTRY</p><h2 id="rcta-title">少しでも気になったら、<br>まずは仕事を知るところから。</h2><p>募集要項を読んで、働くイメージを確かめてください。仕事内容や応募条件で気になることがあれば、カジュアル面談でお話しできます。</p></div>
  <div class="recruit-entry-grid"><a class="recruit-entry reveal" href="#recruit-openings"><span class="entry-icon">01</span><div><small>ENTRY</small><h3>募集要項・応募へ進む</h3><p>営業職・現場職それぞれの求人ページへ。</p></div><b aria-hidden="true">↑</b></a><a class="recruit-entry reveal" href="@R@people/index.html"><span class="entry-icon">02</span><div><small>PEOPLE</small><h3>働くメンバーを見る</h3><p>異業種から転職した営業や、約30年続ける班長を紹介。</p></div><b aria-hidden="true">↗</b></a><a class="recruit-entry reveal" href="@R@work-environment/index.html"><span class="entry-icon">03</span><div><small>WORK ENVIRONMENT</small><h3>労働環境を見る</h3><p>1日の流れ、休日、福利厚生、会社の取り組み。</p></div><b aria-hidden="true">↗</b></a></div></div>
</section>
''' + faq_jsonld()


def build():
    return page("recruit", "採用情報｜株式会社久留米興業",
                "これからの自分に、街を支える仕事を。久留米興業の営業職・現場職のキャリア、評価と収入、募集要項、選考の流れをご紹介します。",
                1, BODY, crumb="採用情報")

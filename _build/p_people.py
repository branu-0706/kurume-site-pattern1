from common import *

P = "@R@assets/photos/"


def member(id_, photo, alt, role, name, title, lead, points, link=None, gate="", rev=False):
    pts = "".join(f"<li><strong>{h}</strong>{t}</li>" for h, t in points)
    lk = ext(link, 'インタビュー全文を読む <span aria-hidden="true">↗</span>', 'text-link') if link else ""
    g = f' gate" data-gate="{gate}' if gate else ""
    media = f'<img src="{P}{photo}" alt="{alt}" loading="lazy">' if photo else '<div class="photo-slot"><div><strong>写真待ち</strong>ご本人の写真を確認のうえ配置</div></div>'
    return f'''<article class="half member{' is-rev' if rev else ''} reveal{g}" id="{id_}" style="scroll-margin-top:96px">
      <div class="half-media">{media}</div>
      <div class="half-copy"><p class="label-num">{role}</p><h3>{title}</h3><p class="member-name">{name}</p><p>{lead}</p><ul class="member-points">{pts}</ul>{lk}</div>
    </article>'''


SALES = [
    member("member-takahata", "member-t.jpg", "笑顔で話す高畑さん", "SALES / 新卒入社", "高畑さん｜営業職（社内で最年少の営業）",
           "「何が分からないかも、分からない」<br>からのスタート。",
           "大学卒業後、最初の会社として久留米興業に入社。専攻は土木と無関係でした。面接で社長と会長に会い、「この人たちの下で頑張りたい」と感じたことが決め手です。",
           [("最初の壁", "現場の用語もルールも分からず、質問したくても言葉が出てこない時期が一番つらかったそうです。社長や先輩が「大丈夫か？」と先に声をかけてくれたことで、立ち直れたと話します。"),
            ("今の仕事", "最初の1〜2年は先輩に同行。今は社長の「断らない営業」という教えを大切に、自ら現場へ足を運んで知識を積み上げています。"),
            ("働き方", "土日祝は基本的に休み。仕事帰りにジムに行くなど、自分の時間も大切にしています。")],
           BLOG_TAKAHATA, gate="採用ブログ・求人票で公開済みの内容を要約。HP転載の承認を確認"),
    member("member-negishi", "member-n2.jpg", "事務所で笑顔を見せる根岸さん", "SALES → SITE AGENT / 異業種から", "根岸さん｜営業職から現場代理人へ",
           "お茶の営業から、<br>道路づくりの現場へ。",
           "前職はお茶屋さんで約12年、営業やパッケージデザインを担当。40歳を目前に、長く安定して働ける国家資格のある仕事を求めて、未経験で土木の世界へ。入社の決め手は社長の人柄でした。",
           [("最初の壁", "最初は用語一つとっても分からない状態。入社後は先輩が1人つき、分からないことはすぐ電話で聞けました。"),
            ("資格", "会社がテキストを用意し、先輩が実務に即して教えてくれる中、3回目の挑戦で1級土木施工管理技士に合格しました。"),
            ("今の仕事", "ガス工事の営業補佐から始まり、現在は世田谷区と年間契約を結んでいる道路の維持工事の現場代理人。協力会社をまとめ、苦情対応から施工の振り分けまでを担っています。"),
            ("働き方", "土日は妻と2人の子どもと過ごす時間。バイク通勤や、社長とのゴルフでオンとオフを切り替えています。")],
           BLOG_NEGISHI, gate="採用ブログ・求人票で公開済みの内容を要約。HP転載の承認を確認", rev=True),
    member("member-imai", "member-i.jpg", "事務所で仕事をする今井さん", "SALES / 40歳で異業種から", "今井さん｜営業職",
           "異業種で積んだ力を、<br>インフラの仕事に。",
           "前職は広告代理店。労働時間が長く、40歳を越えて「この先20年も同じ働き方ができるか」と考え、建設業界へ。若手が少ない業界だからこそ、異業種からでも力を発揮できると考えました。",
           [("最初の壁", "図面を見ても分からない状態で現場へ。職人さんに指摘されることもありましたが、机上の勉強より現場の声を聞くことに徹して、営業としての居場所をつくってきました。"),
            ("大切にしていること", "社内や協力会社との関係づくり。指示は頭ごなしにせず、お願いの形で伝えています。"),
            ("働き方", "営業職は土日が基本的に休みで、連休も取りやすいそうです。週4回ほどジムに通っています。"),
            ("これから", "目標は1級土木施工管理技士の取得です。")],
           BLOG_IMAI, gate="採用ブログ・求人票で公開済みの内容を要約。HP転載の承認を確認"),
]

FIELD = [
    member("member-matsuno", "field-team-back.jpg", "歩道の現場で作業する班のメンバー", "FIELD / 班長・約30年", "松野さん｜現場の班長",
           "一人ひとりが役割を理解して、<br>1日の作業を終わらせる。",
           "入社前はガス関係の個人事業主。友人の紹介で久留米興業に入り、約30年にわたって現場を支えてきました。今は班の段取りや役割分担を担っています。",
           [("現場の進め方", "班の中で役割分担ができていて、細かく指示することはあまりないそうです。進み具合を見て、問題がありそうなら手を加えたり手伝ったりします。"),
            ("変わったこと", "昔はたばこをくわえたまま作業する時代もありましたが、今はヘルメット着用を徹底し、近隣への配慮も含めて安全への意識が大きく変わりました。"),
            ("正直なところ", "その日の作業はその日のうちに終わらせるのが現場の決まり。作業量が多く、休憩を取る余裕を感じにくい日もあります。人が増えれば余裕につながる、と話します。"),
            ("新人へ", "「まずは毎日来ること。最初から何でもできる必要はありません。焦らず、長く続けてもらえれば」")],
           None, gate="対談インタビュー原稿（掲載前）に基づく編集文：本人承認待ち"),
    member("member-okui", "field-boots.jpg", "スコップを持って路盤に立つ現場職の足元", "FIELD / 建築から土木へ・5〜6年", "奥居さん｜現場職",
           "見て覚えて、聞いて覚える。<br>カラーコーンを並べるところから。",
           "建築業界で躯体工事や外構工事、型枠などを経験した後、久留米興業へ。土木の現場は初めてでしたが、松野さんたち先輩と一緒に経験を重ね、5〜6年になります。",
           [("入ってみて", "「最初は皆さん見た目が怖い。でも、話すと優しい人が多い」"),
            ("現場の連携", "作業中は近隣への配慮もあって会話は少なめ。それでも分からないことは聞き、班長の動きを見ながら合わせていきます。「班長がいるといないとじゃ、全然違う」"),
            ("続けている理由", "特別な理由より、毎日現場に出て、合う人たちと仕事をしてきた積み重ね。早く帰れるようにみんなで頑張る感覚もあるそうです。"),
            ("新人へ", "「仕事なのできついこともあります。夏は暑い。でも毎日出ていれば、少しずつ流れは分かってきます」")],
           None, gate="対談インタビュー原稿（掲載前）に基づく編集文：本人承認待ち", rev=True),
]

import hero as _kv
HERO = _kv.frame(sid='people-hero', tid='people-title', no='05', en='OUR PEOPLE', jp='働くメンバー', img='team.jpg', alt='重機の前に並ぶ久留米興業の社員たち', pos='60% 35%', word='PEOPLE', flip=True, h1='同じ人はいない。<br>だから、チームは面白い。', lead='久留米興業には、現場で手を動かす人、取引先との関係をつくる人、その両方をつなぐ人がいます。経験も考え方も違う一人ひとりが、同じ街の仕事を支えています。')

BODY = f'''
{HERO}
<!--CRUMB-->

<!-- 02 ONE TEAM｜方式B：CMS 54 Half ＋ 35 Title Sub ＋ CSS -->
<section class="section" id="people-intro" aria-labelledby="intro-title" data-cms-id="54,35" data-implementation="B">
  <div class="wrap half reveal">
    <div class="half-copy"><p class="section-kicker">ONE TEAM, DIFFERENT STORIES</p><h2 class="section-title" id="intro-title">同じゴールに向かう、<br>いろいろな個性。</h2>
      <p>得意なことも、仕事の覚え方も、人によって違います。久留米興業が大切にしているのは、全員を同じ型にはめることよりも、それぞれが自分の役割を果たしながら協力すること。</p>
      <p>新卒で入った若手、40歳前後で異業種から転職した営業、建築から土木へ移った現場職、30年続ける班長。違う経験を持つ人が集まっているからこそ、現場で気づくこと、取引先に伝えられること、次の仕事につなげられることがあります。</p></div>
    <ul class="member-mix">
      <li><b>新卒</b>土木と関係のない専攻から入社した営業</li>
      <li><b>40歳前後</b>お茶の営業、広告代理店から転職した営業</li>
      <li><b>建築から</b>躯体・外構の経験を経て土木の現場へ</li>
      <li><b>約30年</b>班の段取りを担う現場の班長</li>
    </ul>
  </div>
</section>

<!-- 社員の声｜方式B：CMS 42 Card Three ＋ CSS（スマホは横スクロール、JSなし） -->
<section class="section bg-soft" id="people-voices" aria-labelledby="voices-title" data-cms-id="42" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">VOICES <span>社員の声</span></p><h2 class="section-title" id="voices-title">入社前の不安に、<br>働く社員が答えます。</h2></div>
    <div class="voices reveal gate" data-gate="インタビュー・対談からの引用（原文どおり）。掲載承認を確認">
      <figure class="voice is-field" style="margin:0"><p>最初は、皆さん見た目的には怖いです。でも、話してみると優しい方が多いですよね、やっぱり。</p><footer><div><b>奥居さん</b>現場職・建築から転職</div></footer></figure>
      <figure class="voice" style="margin:0"><p>知識は後からで大丈夫です。</p><footer><div><b>高畑さん</b>営業職・新卒入社</div></footer></figure>
      <figure class="voice" style="margin:0"><p>結局は『人と人』の関わりが、新しい依頼や円滑な現場運営に繋がります。</p><footer><div><b>根岸さん</b>営業職から現場代理人</div></footer></figure>
      <figure class="voice" style="margin:0"><p>社長は意思決定が驚くほど速く、やる気があれば未経験でもチャンスをくれる人です。</p><footer><div><b>今井さん</b>営業職・40歳で異業種から</div></footer></figure>
      <figure class="voice is-field" style="margin:0"><p>まずは、毎日来ることじゃないですかね。最初から何でもできる必要はありません。</p><footer><div><b>松野さん</b>現場の班長・約30年</div></footer></figure>
    </div>
  </div>
</section>

<!-- 03 PRESIDENT｜方式B：CMS 54 Half ＋ 80 H2 Text ＋ 761（歩み）＋ CSS -->
<section class="section" id="people-ceo" aria-labelledby="ceo-title" data-cms-id="54,80,761" data-implementation="B">
  <div class="wrap">
    <div class="half reveal" style="grid-template-columns:.82fr 1fr">
      <div class="half-media is-portrait"><img src="{P}ceo.jpg" alt="代表取締役 川島 和範" loading="lazy"><p class="caption">代表取締役　川島 和範</p></div>
      <div class="half-copy gate" data-gate="代表インタビュー（2026-07-17再構成）に基づく編集文：本人承認待ち">
        <p class="section-kicker">MESSAGE / PRESIDENT <span>代表取締役　川島 和範</span></p>
        <h2 class="section-title" id="ceo-title">自分が苦しかったからこそ、<br>働き方を変えたかった。</h2>
        <p>川島代表は、高校を卒業した18歳で久留米興業に入り、現場作業の見習いから始めました。身内だからと特別扱いされることはなく、一番下からのスタートでした。</p>
        <p>当時は休みが少なく、まとまった休みがあっても体が疲れきっていた。「何のために働いているのか分からない」と感じ、24歳で一度会社を離れます。1年ほど仕事から離れた後に戻り、現場の作業員から管理職へ。35歳ごろからは取引先との会議にも出るようになり、40代で代表に就任しました。</p>
        <p>代表になってから最初に取り組んだのは、三六協定を含めた残業のルールの見直しです。現場の作業そのものは簡単には減らせないため、これまで8人で行っていた仕事を10人で行うように人を増やし、一人ひとりの負担を軽くしてきました。「まだ十分にできていないこともある」と認めながら、変えるべきところは変え続けています。</p>
        <p class="quote-band">最終的に、ここで働いて良かったと<br>思ってもらえる会社へ。</p>
        <div class="cta-row"><a class="text-link" href="@R@recruit/index.html#recruit-message">代表の採用メッセージを見る <span aria-hidden="true">↗</span></a><a class="text-link" href="@R@company/index.html#company-ceo">会社の考え方を見る <span aria-hidden="true">↗</span></a></div>
      </div>
    </div>
  </div>
</section>

<!-- 04 SALES TEAM｜方式B：CMS 42 Card Three ＋ 54 Half（詳細）＋ CSS -->
<section class="section bg-soft" id="people-sales" aria-labelledby="sales-title" data-cms-id="42,54" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">SALES TEAM <span>営業職</span></p><h2 class="section-title" id="sales-title">売るだけではない。<br>人と現場をつなぐ仕事。</h2><p class="section-heading-desc" style="max-width:700px">取引先の相談を受けること、現場の状況を知ること、必要な人や材料、工程をつなぐこと。久留米興業の営業職には、業界未経験から仕事を覚えてきた社員が多くいます。</p></div>
    <div class="people-grid">
      <a class="person-card reveal" href="#member-takahata"><div class="person-photo"><img src="{P}member-t2.jpg" alt="高畑さん" loading="lazy"></div><div class="person-info"><span>SALES / 新卒入社</span><h3>高畑さん</h3><p>「何が分からないかも、分からない」からのスタート。</p><span class="person-arrow" aria-hidden="true">↓</span></div></a>
      <a class="person-card reveal" href="#member-negishi" data-delay="1"><div class="person-photo"><img src="{P}member-n.jpg" alt="根岸さん" loading="lazy"></div><div class="person-info"><span>SALES → SITE AGENT</span><h3>根岸さん</h3><p>お茶の営業から、道路づくりの現場へ。1級土木施工管理技士。</p><span class="person-arrow" aria-hidden="true">↓</span></div></a>
      <a class="person-card reveal" href="#member-imai" data-delay="2"><div class="person-photo"><img src="{P}member-i2.jpg" alt="今井さん" loading="lazy"></div><div class="person-info"><span>SALES / 異業種から</span><h3>今井さん</h3><p>広告代理店から、40歳で建設業界へ。</p><span class="person-arrow" aria-hidden="true">↓</span></div></a>
    </div>
    <div class="members">{"".join(SALES)}</div>
  </div>
</section>

<!-- 05 FIELD TEAM｜方式B：CMS 54 Half ＋ 584 Photo Gallery ＋ CSS -->
<section class="section" id="people-field" aria-labelledby="field-title" data-cms-id="54,584" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">FIELD TEAM <span>現場職</span></p><h2 class="section-title" id="field-title">楽な仕事ではない。<br>けれど、仲間と1日をやり切る仕事。</h2><p class="section-heading-desc" style="max-width:720px">夏場の暑さ、夜間の作業、限られた時間の中で求められる作業量。現場の仕事は決して楽ではありません。それでも、道路は人々の生活に欠かせないもの。約30年現場を見てきた班長と、建築から土木へ移った現場職の2人に話を聞きました。</p></div>
    <div class="members">{"".join(FIELD)}</div>
    
</section>

<!-- 06 WORKING TOGETHER｜方式B：CMS 787 Text Two ／ 761 Flow Cards ＋ CSS -->
<section class="section bg-soft" id="people-together" aria-labelledby="together-title" data-cms-id="787,761" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">WORKING TOGETHER <span>営業と現場</span></p><h2 class="section-title" id="together-title">仕事の役割が違っても、<br>目指す先は同じ。</h2><p class="section-heading-desc" style="max-width:720px">工事の相談を受け、必要な情報を整理する営業職。現場の状況を把握し、実際の施工を進める現場職。週に一度の工程会議で仕事を調整し、夏の暑気払いなどで顔を合わせる機会もあります。</p></div>
    <ol class="flow is-4 reveal gate" data-gate="分担は概略：案件ごとの正式な流れと権限を確認">
      <li><span class="num">01</span><h3>相談・打合せ</h3><p>営業</p></li>
      <li><span class="num">02</span><h3>現地確認・手配</h3><p>営業＋現場</p></li>
      <li style="border-top-color:var(--blue)"><span class="num">03</span><h3>施工</h3><p>現場</p></li>
      <li><span class="num">04</span><h3>完了確認・報告</h3><p>営業・現場の両方</p></li>
    </ol>
    <p class="flow-note">案件によって流れや分担は異なります。</p>
  </div>
</section>

<!-- 07 OUR TEAM｜方式B：CMS 42 Card Three（職場の雰囲気）。人数グラフ（方式C）は基準日が揃うまで非表示 -->
<section class="section" id="people-data" aria-labelledby="data-title" data-cms-id="42,custom" data-implementation="B／グラフのみC">
  <div class="wrap">
    <div class="section-heading reveal"><p class="section-kicker">OUR TEAM <span>職場のこと</span></p><h2 class="section-title" id="data-title">数字と言葉で知る、<br>久留米興業の職場。</h2></div>
    <div class="card-grid is-3 reveal gate" data-gate="従業員数・雰囲気は求人票（2026-11-05）の記載より">
      <div class="info-card"><small>MEMBERS</small><h3>従業員 37名</h3><p>事務所・営業・現場・車両や警備まで、自社のメンバーで仕事を進めています。</p></div>
      <div class="info-card is-blue"><small>ATMOSPHERE</small><h3>落ち着いた職場</h3><p>作業中は黙々と。分からないことは聞けば答えてくれます。男性が多めの職場です。</p></div>
      <div class="info-card"><small>EVALUATION</small><h3>がんばりを評価</h3><p>結果だけでなく、仕事を覚えようとする姿勢と、できるようになった仕事を見ます。</p></div>
    </div>
    <div class="review-only gate" data-gate="年代・勤続・職種別の人数グラフ：基準日・対象範囲が揃うまで非表示" style="margin-top:40px">
      <p class="caption tbd">【要確認】基準日、対象範囲（正社員／役員／パート／協力会社を含むか）。求人票の37名と行政情報の30名の違い。年代・勤続年数・職種別の人数が揃えば、数値表つきの棒グラフ（方式C）で追加します。</p>
    </div>
  </div>
</section>

<!-- 08 CTA｜方式B：CMS 42 Card Three ＋ 90 Btn Text -->
<section class="section bg-blueish" id="people-cta" aria-labelledby="pcta-title" data-cms-id="42,90" data-implementation="B">
  <div class="wrap">
    <div class="section-heading reveal"><h2 class="section-title" id="pcta-title">人を知ったら、<br>次は仕事を知る。</h2><p class="section-heading-desc">社員一人ひとりの経験や考えを知ったら、どのような仕事があり、どんな環境で働くのかも見てみてください。</p></div>
    <div class="card-grid is-3">
      <a class="link-card no-media reveal" href="@R@business/index.html"><div class="lc-body"><small>BUSINESS</small><h3>事業内容を見る</h3><span class="mini-link">事業内容へ <b aria-hidden="true">↗</b></span></div></a>
      <a class="link-card no-media reveal" href="@R@work-environment/index.html" data-delay="1"><div class="lc-body"><small>WORK ENVIRONMENT</small><h3>働く環境を見る</h3><span class="mini-link">労働環境へ <b aria-hidden="true">↗</b></span></div></a>
      <a class="link-card no-media reveal" href="@R@recruit/index.html" data-delay="2"><div class="lc-body"><small>RECRUIT</small><h3>採用情報を見る</h3><span class="mini-link">採用情報へ <b aria-hidden="true">↗</b></span></div></a>
    </div>
    <p class="fine-note" style="margin-top:24px">営業職3名のインタビュー全文は{ext(BLOG_LIST, '採用ブログ')}でご覧いただけます。</p>
  </div>
</section>
'''


def build():
    return page("people", "働くメンバー｜株式会社久留米興業",
                "同じ人はいない。だから、チームは面白い。久留米興業の代表、営業職、現場職のメンバーをご紹介します。",
                1, BODY, crumb="働くメンバー")

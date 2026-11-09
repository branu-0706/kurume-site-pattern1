# -*- coding: utf-8 -*-
"""パターン③（コーポレート／参考：日鉄パイプライン＆エンジニアリング）の TOP 本文。
軸になる仕掛け：道路の断面図（assets/n/cross-section.svg）。舗装の上と、地面の下の仕事を1枚で見せ、4事業の入口にする。
コンテンツ：パターン①（事業・進め方・施工実績・会社情報）＋ パターン②（ビジョン・働き方の見直し・人）のミックス。
HTMLは CMS の section（data-cms-id）をそのまま置き、見た目は assets/n/p3-*.css、動きは assets/n/n.js で付ける。
パスは pattern3/design-x/ から見た相対パス。"""
from common import OFFICIAL_WORKS, OFFICIAL_NEWS, OFFICIAL_CONTACT, DISASTER, BLOG_LIST, BLOG_NEGISHI

R = "../../"
P = R + "assets/photos/"
CS = R + "assets/n/cross-section.svg"
X = ' target="_blank" rel="noopener noreferrer"'
XS = '<span class="sr-only">（外部サイトが開きます）</span>'


def head(en, ja, hid, catch="", lead=""):
    c = f'<p class="n-catch">{catch}</p>' if catch else ""
    l = f'<p class="n-lead">{lead}</p>' if lead else ""
    return f'<div class="n-head"><h2 class="n-h2" id="{hid}"><span class="n-en">{en}</span><span class="n-ja">{ja}</span></h2>{c}{l}</div>'


BIZ = [
    ("01", "service-gas", "ガス管取替後の復旧舗装工事", "ガス管の取替後に行う道路の舗装復旧工事。掘り返した道路を、元の状態に戻します。", "paving-roller.jpg", "ローラーで舗装を締め固める現場"),
    ("02", "service-water", "水道工事", "水道管の布設・布設替など、給水インフラに関わる工事。", "water-pipe.jpg", "掘削した溝に水道管を布設している現場"),
    ("03", "service-civil", "一般土木工事", "道路の改良・維持など、公共空間の基盤に関わる土木工事。", "civil-road.jpg", "カラー舗装で仕上げた道路"),
    ("04", "service-sewer", "下水道工事", "下水道の整備など、生活環境を支える工事。", None, None),
]

WORKS = [
    ("work-kamisoshigaya.jpg", "歩道の舗装を終えた現場と工事黒板", "ROAD MAINTENANCE", "令和3年度 道路維持工事", "世田谷区上祖師谷"),
    ("work-kyuden.jpg", "表層を改良した道路", "SURFACE IMPROVEMENT", "表層改良", "世田谷区給田"),
    ("work-chisaki.jpg", "新しく舗装した生活道路と工事黒板", "ROAD CONSTRUCTION", "地先道路築造工事", "世田谷区上祖師谷"),
]


def body():
    slides = [
        ("field-work-street.jpg", "重機とともに歩道の路盤をつくる施工中の現場", "01", "道路の上の仕事"),
        ("machine.jpg", "社名の入った重機", "02", "重機と資材"),
        ("yard-low-krm.jpg", "重機が並ぶ北烏山の資材置き場", "03", "北烏山の資材置き場"),
    ]
    sl = "".join(f'<figure class="n-slide{" is-on" if i == 0 else ""}" data-label="{lab}"><img src="{P}{f}" alt="{a}" width="1600" height="1066"{" fetchpriority=\"high\"" if i == 0 else " loading=\"lazy\""}></figure>' for i, (f, a, n, lab) in enumerate(slides))

    biz = ""
    for n, anc, h, t, img, alt in BIZ:
        media = (f'<img src="{P}{img}" alt="{alt}" loading="lazy" width="1600" height="1066">' if img else
                 f'<img class="is-diagram" src="{CS}" alt="道路の断面図。地中の下水道管とマンホール" loading="lazy" width="720" height="520">')
        biz += f'<a class="n-biz-item" href="business/index.html#{anc}" data-layer="{n}"><span class="n-num">{n}</span><h3>{h}</h3><p>{t}</p><div class="n-biz-media">{media}</div><span class="n-more">詳しく見る</span></a>'

    works = "".join(f'<li class="n-card"><a href="{OFFICIAL_WORKS}"{X}><div class="n-card-media"><img src="{P}{f}" alt="{a}" loading="lazy" width="1600" height="1066"></div><small>#{en}</small><h3>{t}<br><span>{place}</span></h3><span class="n-more">詳しく見る ↗</span>{XS}</a></li>' for f, a, en, t, place in WORKS)
    works += f'<li class="n-card is-more"><a href="{OFFICIAL_WORKS}"{X}><small>#MORE PROJECTS</small><h3>施工実績を<br>もっと見る</h3><span class="n-more">施工実績の一覧 ↗</span>{XS}</a></li>'

    return f'''
<!-- 01 MAIN VISUAL｜CMS 721 Mainvisual Responsive Slider（写真3枚・自動切替）＋ 734（キャッチ）＋ 画像（道路の断面図）。CTAなし -->
<section class="n-mv" aria-labelledby="h1" data-cms-id="721,734">
  <div class="n-mv-copy">
    <h1 id="h1"><span class="ln">道路の上も、</span><span class="ln">地面の下も。</span></h1>
    <p class="n-mv-en" aria-hidden="true">ROADS, AND WHAT LIES BENEATH</p>
    <p class="n-mv-lead">世田谷を拠点に、1974年から。ガス管取替後の復旧舗装、水道・一般土木・下水道工事を担っています。</p>
  </div>
  <div class="n-mv-photo" data-n-slider>{sl}
    <div class="n-mv-count" aria-hidden="true"><b class="n-cur">01</b><span>/ 03</span><em class="n-lab">道路の上の仕事</em><i class="n-bar"></i></div>
  </div>
  <figure class="n-mv-cs"><img src="{CS}" alt="道路の断面図。舗装の下に路盤があり、地中をガス管・水道管・下水道管が通っている" width="720" height="520"></figure>
  <p class="n-scroll" aria-hidden="true">SCROLL DOWN</p>
</section>

<!-- 02 NEWS（1行）｜CMS 101 Blog の最新1件 -->
<section class="n-ticker" aria-label="最新のお知らせ" data-cms-id="101">
  <div class="wrap"><time datetime="2024-03-08">2024.03.08</time><span class="n-tag">お知らせ</span><a href="{DISASTER}"{X}>令和6年度能登半島地震に伴う災害救援隊について ↗{XS}</a></div>
</section>

<!-- 03 BUSINESS｜CMS 54 Half（縦長の写真＋縦書きの見出し）＋ 16 Card Four（4事業。断面図の番号と対応） -->
<section class="n-sec n-biz" aria-labelledby="biz-title" data-cms-id="54,16">
  <div class="wrap">
    {head("BUSINESS", "事業内容", "biz-title", "道路の上と、地面の下の仕事。", "ガス管取替後の道路復旧から、水道・土木・下水道工事まで。断面図の番号が、それぞれの事業の持ち場です。")}
    <div class="n-biz-grid">
      <figure class="n-biz-tall"><img src="{P}field-worker-helmet.jpg" alt="ヘルメット姿で道路の工事をする現場職" loading="lazy" width="1600" height="1066"><figcaption><b>道路と地中の<br>インフラ工事</b><span>暮らしの足元を、つくり直し、守る。</span></figcaption></figure>
      <div class="n-biz-items">{biz}</div>
    </div>
    <div class="n-actions"><a class="n-btn" href="business/index.html">事業内容を詳しく見る</a></div>
  </div>
</section>

<!-- 04 PICK UP｜CMS 42 Card Three（文字と図形のバナー。写真を使わない） -->
<section class="n-sec n-pick" aria-labelledby="pick-title" data-cms-id="42">
  <div class="wrap">
    {head("PICK UP", "おすすめ", "pick-title")}
    <ul class="n-pick-list">
      <li><a href="{OFFICIAL_WORKS}"{X}><span class="n-pick-en">PROJECT<br>HIGHLIGHTS</span><span class="n-pick-ja">久留米興業が手がけた施工実績 ↗</span>{XS}</a></li>
      <li><a href="{BLOG_LIST}"{X}><span class="n-pick-en">STAFF<br>INTERVIEW</span><span class="n-pick-ja">営業社員のインタビュー記事 ↗</span>{XS}</a></li>
      <li><a href="{DISASTER}"{X}><span class="n-pick-en">DISASTER<br>RELIEF</span><span class="n-pick-ja">能登半島地震の災害救援隊 ↗</span>{XS}</a></li>
    </ul>
  </div>
</section>

<!-- 05 VISION｜CMS 80 H2 Text ＋ 54 Half（パターン②の考え方） -->
<section class="n-sec n-vision" aria-labelledby="vision-title" data-cms-id="80,54">
  <div class="wrap">
    {head("VISION", "これからの会社", "vision-title")}
    <div class="n-vision-grid">
      <div class="n-vision-copy">
        <p class="n-statement">守るために、<br>変えていく。</p>
        <p>昔のやり方のままでは、働く人も仕事も守れない。現場を知る代表が、働き方の見直しに向き合ってきました。仕事が続くために、人が育つ会社でありたいと考えています。</p>
        <ol class="n-points"><li><b>01</b>勤務時間を見直す</li><li><b>02</b>現場の負担を分け合う</li><li><b>03</b>個性を同じ型にはめない</li></ol>
        <p class="n-note">これは代表の取り組みと方針です。現場には今も忙しい日や体力的な負担があり、その実際は採用情報でお伝えしています。</p>
        <div class="n-actions is-left"><a class="n-btn" href="company/index.html">会社の考え方を見る</a><a class="n-link" href="work-environment/index.html">労働環境を見る</a></div>
      </div>
      <figure class="n-vision-photo"><img src="{P}operator-lever.jpg" alt="作業着の袖で重機のレバーを握る手元" loading="lazy" width="1600" height="1066"></figure>
    </div>
  </div>
</section>

<!-- 06 COORDINATION｜CMS 787 Text Three（取引先 → 営業・調整 → 現場・施工） -->
<section class="n-sec n-flow" aria-labelledby="flow-title" data-cms-id="787">
  <div class="wrap">
    {head("COORDINATION", "仕事の進め方", "flow-title", "施工の先にある、信頼まで。", "工事は、取引先・現場・協力会社・地域の方々との連携によって進みます。現場を円滑に進めるための関係づくりも大切にしています。")}
    <ol class="n-flow-list">
      <li><span class="n-step">STEP 01</span><small>CLIENT</small><h3>取引先・発注者</h3><p>工事の内容や場所、時期などのご相談を受けて、仕事が始まります。</p></li>
      <li><span class="n-step">STEP 02</span><small>COORDINATION</small><h3>営業・調整</h3><p>現地の確認、見積、人や材料・日程の段取りを整え、現場とつなぎます。</p></li>
      <li><span class="n-step">STEP 03</span><small>CONSTRUCTION</small><h3>現場・施工</h3><p>安全を確かめながら班で役割を分け、近隣にも配慮して施工を進めます。</p></li>
    </ol>
  </div>
</section>

<!-- 07 PROJECT HIGHLIGHTS｜CMS 718 Portfolio（横に送るカルーセル） -->
<section class="n-sec n-works" aria-labelledby="works-title" data-cms-id="718">
  <div class="wrap">
    <div class="n-works-head">{head("PROJECT HIGHLIGHTS", "施工実績", "works-title", "", "世田谷区内の道路維持・表層改良・道路築造など、確認できた施工の様子をご紹介します。")}
      <div class="n-ctrl" data-n-ctrl="works"><button type="button" class="n-prev" aria-label="前へ">‹</button><button type="button" class="n-next" aria-label="次へ">›</button></div></div>
    <ul class="n-track" id="works" data-n-track>{works}</ul>
    <div class="n-progress" aria-hidden="true"><i data-n-progress="works"></i></div>
  </div>
</section>

<!-- 08 NUMBERS｜CMS 787 Text Four（確認できた事実だけ） -->
<section class="n-sec n-numbers" aria-labelledby="num-title" data-cms-id="787">
  <div class="wrap">
    {head("FACTS", "数字で見る久留米興業", "num-title")}
    <dl class="n-num-list">
      <div><dt>設立</dt><dd><b>1974</b><span>年</span></dd><p>1974年3月4日設立</p></div>
      <div><dt>事業分野</dt><dd><b>4</b><span>分野</span></dd><p>復旧舗装・水道・一般土木・下水道</p></div>
      <div><dt>職種</dt><dd><b>2</b><span>職種</span></dd><p>営業職・現場職</p></div>
      <div><dt>拠点</dt><dd><b>世田谷</b></dd><p>東京都世田谷区北烏山</p></div>
    </dl>
  </div>
</section>

<!-- 09 FOR YOU｜CMS 42 Card Three ×2（写真全面のタイル 2×2） -->
<section class="n-tiles" aria-label="採用・働き方・人・会社" data-cms-id="42">
  <a class="n-tile" href="recruit/index.html"><img src="{P}member-i-helmet.jpg" alt="ヘルメットを手に現場に立つ社員" loading="lazy" width="1600" height="1066"><span class="n-tile-label"><small>#RECRUIT</small><b>採用情報</b><em>営業職・現場職の仕事と募集条件</em></span></a>
  <a class="n-tile" href="work-environment/index.html"><img src="{P}yard-machines.jpg" alt="資材置き場に並ぶ重機と運搬車" loading="lazy" width="1600" height="1066"><span class="n-tile-label"><small>#ENVIRONMENT</small><b>労働環境</b><em>働く時間・休み・現場の1日</em></span></a>
  <a class="n-tile" href="people/index.html"><img src="{P}member-t3.jpg" alt="事務所で働く社員" loading="lazy" width="1600" height="1066"><span class="n-tile-label"><small>#PEOPLE</small><b>働くメンバー</b><em>現場と事務所、それぞれの役割</em></span></a>
  <a class="n-tile" href="company/index.html"><img src="{P}entrance.jpg" alt="「(株)久留米興業」の看板が掲げられた本社の敷地入口" loading="lazy" width="1600" height="1066"><span class="n-tile-label"><small>#COMPANY</small><b>会社情報</b><em>会社概要・沿革・アクセス</em></span></a>
</section>

<!-- 10 NEWS｜CMS 101 Blog -->
<section class="n-sec n-news" aria-labelledby="news-title" data-cms-id="101">
  <div class="wrap">
    {head("NEWS", "お知らせ・取り組み", "news-title")}
    <ul class="n-news-list">
      <li><a href="{DISASTER}"{X}><time datetime="2024-03-08">2024.03.08</time><span class="n-tag">お知らせ</span><span class="n-t">令和6年度能登半島地震に伴う災害救援隊について ↗</span>{XS}</a></li>
      <li><a href="{BLOG_NEGISHI}"{X}><time>—</time><span class="n-tag">インタビュー</span><span class="n-t">営業職・根岸さんのインタビュー ↗</span>{XS}</a></li>
      <li><a href="{OFFICIAL_NEWS}"{X}><time>—</time><span class="n-tag">お知らせ</span><span class="n-t">お知らせ一覧 ↗</span>{XS}</a></li>
    </ul>
    <div class="n-actions"><a class="n-link" href="{BLOG_LIST}"{X}>公開記事一覧を見る ↗{XS}</a></div>
  </div>
</section>

<!-- 11 CONTACT｜CMS 90 Btn Text ＋ 23 Btn -->
<section class="n-sec n-contact" aria-labelledby="contact-title" data-cms-id="90,23">
  <div class="wrap">
    {head("CONTACT", "お問い合わせ", "contact-title", "工事のご相談から、会社のことまで。")}
    <div class="n-contact-grid">
      <div class="n-contact-card"><small>FOR CLIENTS</small><h3>法人・取引先の方</h3><p class="n-tel">TEL <a href="tel:0333093786">03-3309-3786</a></p><p>東京都世田谷区北烏山6丁目26-28</p><a class="n-btn" href="{OFFICIAL_CONTACT}"{X}>お問い合わせフォーム ↗{XS}</a></div>
      <div class="n-contact-card"><small>CAREERS</small><h3>採用をご検討の方</h3><p>仕事内容、入社後の流れ、待遇・募集条件をまとめています。</p><a class="n-btn" href="recruit/index.html">採用情報を見る</a></div>
    </div>
  </div>
</section>
'''

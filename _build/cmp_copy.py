# 比較用TOPの共通文章。同じ構成パターンのデザイン②・③は、このデータだけを使い、文言・写真・リンクを揃える。
# 文言はデザイン①（GitHub上の基準TOP）を優先し、デザイン①にない部分だけ共通文章マスターから補う。
from common import OFFICIAL_CONTACT, OFFICIAL_WORKS, OFFICIAL_NEWS, DISASTER, BLOG_NEGISHI, BLOG_TAKAHATA, BLOG_IMAI, BLOG_LIST

PH = "@R@assets/photos/"

P1 = {
    "hero": {"label": "KURUME KOGYO", "h1": ["街を支える仕事を、", "働く人の未来につなげる。"],
             "lead": "道路や水道など、暮らしに欠かせないインフラを支えてきた久留米興業。積み重ねてきた技術と人とのつながりを大切に、街と働く人のこれからをつくっていきます。",
             "img": ("field-work-street.jpg", "歩道の舗装工事を進める現場職と重機"), "caption": "道路・水道などのインフラ工事",
             "cta": [("久留米興業について", "@P1@company/index.html"), ("採用情報を見る", "@P1@recruit/index.html")]},
    "about": {"label": "ABOUT US", "ja": "久留米興業について", "h2": ["街と、人と。", "積み重ねてきた50年以上。"],
              "body": ["株式会社久留米興業は、1974年の設立以来、道路や水道など、暮らしに欠かせないインフラ工事に取り組んできました。",
                       "私たちが大切にしてきたのは、工事を完成させることだけではありません。その先にいる人とのつながりを大切にしながら、一つひとつの仕事に向き合ってきました。"],
              "img": ("entrance.jpg", "「(株)久留米興業」の看板が掲げられた本社の敷地入口"),
              "cta": ("久留米興業を知る", "@P1@company/index.html")},
    "business": {"label": "BUSINESS", "ja": "事業内容", "h2": ["何気なく通る道にも、", "私たちの仕事がある。"],
                 "lead": "毎日の「当たり前」を支えるために。道路・水道をはじめ、街のさまざまな場所で私たちの仕事が続いています。",
                 "items": [("ガス管取替後の復旧舗装工事", "ガス管を取り替えたあとの道路を、また使える状態へ。", "paving-roller.jpg", "ローラーで舗装を転圧している現場", "@P1@business/index.html#service-gas"),
                           ("水道工事", "配水管の新設や給水管の取替など、水の通り道を整える。", "water-pipe.jpg", "掘削した溝に配水管を布設している現場", "@P1@business/index.html#service-water"),
                           ("一般土木工事", "路面の改良・維持など、毎日使われる街の基盤を整える。", "civil-road.jpg", "カラー舗装で仕上げた道路", "@P1@business/index.html#service-civil"),
                           ("下水道工事", "下水道の整備を通じて、暮らしを支える地下のインフラに携わる。", None, None, "@P1@business/index.html#service-sewer")],
                 "cta": ("事業内容を詳しく見る", "@P1@business/index.html")},
    "values": {"label": "OUR VALUES", "ja": "大切にしていること", "h2": ["仕事をつなぐのは、", "いつだって人だ。"],
               "lead": "どんな仕事にも、その先に人がいる。取引先、地域の方々、そしてともに働く仲間。久留米興業は、その一つひとつのつながりを大切にしています。",
               "items": [("人とのつながり", "頼り、頼られる関係を、仕事の土台に。"), ("街の暮らしへの責任", "目に見える仕事も、見えない仕事も、丁寧に。"), ("働く人とつくる未来", "一人ひとりが、次の一歩を踏み出せる会社へ。")],
               "img": ("office.jpg", "事務所で打ち合わせをする社員たち"),
               "cta": ("大切にしていることを読む", "@P1@company/index.html#company-values")},
    "works": {"label": "WORKS", "ja": "施工の様子", "h2": ["一つひとつの現場が、", "街のこれからをつくる。"],
              "lead": "道路や水道に関わる工事は、地域の暮らしのすぐそばにあります。写真から、実際の仕事の姿をご覧ください。",
              "items": [("work-kamisoshigaya.jpg", "歩道の舗装を終えた現場と工事黒板"), ("work-kyuden.jpg", "舗装を仕上げた車道"), ("work-chisaki.jpg", "新しく舗装した生活道路と工事黒板")],
              "item_label": "施工の一場面",
              "cta": ("施工実績を見る", OFFICIAL_WORKS)},
    "workstyle": {"label": "WORK STYLE", "ja": "労働環境", "h2": ["長く働ける会社は、", "変わり続ける会社だ。"],
                  "body": ["現場で働いてきた代表自身の経験があるからこそ、働き方にも目を向けてきました。",
                           "仕事への責任と、自分らしい暮らし。そのどちらも大切にできる会社を目指して、少しずつ変化を続けています。"],
                  "roles": [("営業職", "取引先と現場の間に立ち、見積や段取りを整える。工事の状況によっては、夜間や休日に連絡が入ることもある。", "office-pc.jpg", "事務所でパソコンに向かう社員"),
                            ("現場職", "班で役割を分けて施工を進める。夏の暑さや夜間作業など、体力的な負担もある。", "field-worker-helmet.jpg", "ヘルメットをかぶり作業する現場職")],
                  "cta": ("働く環境を知る", "@P1@work-environment/index.html")},
    "people": {"label": "PEOPLE", "ja": "働くメンバー", "h2": ["同じ人はいない。", "だから、チームは面白い。"],
               "lead": "現場、営業、会社を支えるさまざまな人たち。それぞれの経験と個性が、久留米興業の仕事をつくっています。",
               "items": [("代表", "PRESIDENT", "現場の経験を、会社づくりへ。", "ceo-portrait.jpg", "代表取締役 川島 和範", "@P1@people/index.html#people-ceo"),
                         ("営業職", "SALES", "取引先と施工現場をつなぐ。", "member-t3.jpg", "事務所で仕事をする営業職の社員", "@P1@people/index.html#people-sales"),
                         ("現場職", "FIELD WORK", "仲間とともに、目の前の仕事を形にする。", "field-crew-hq.jpg", "歩道の路盤をつくる現場職のチーム", "@P1@people/index.html#people-field")],
               "cta": ("働くメンバーを見る", "@P1@people/index.html")},
    "recruit": {"label": "RECRUIT", "ja": "採用情報", "h2": ["今できることより、", "これからできることを。"],
                "lead": "最初から何でもできなくていい。学び、考え、自分の仕事を少しずつ広げていく。久留米興業で、あなたの次の一歩を。",
                "items": [("営業職", "SALES", "取引先への対応、見積、現場の段取りをつなぐ。", "member-i.jpg", "事務所で仕事をする営業職の社員", ("営業職を知る", "@P1@recruit/index.html#recruit-career")),
                          ("現場職", "FIELD WORK", "工事現場で経験を重ね、チームで施工を進める。", "field-sidewalk.jpg", "歩道の工事現場で作業する現場職", ("現場職を知る", "@P1@recruit/index.html#career-field"))],
                "cta": ("募集要項を見る", "@P1@recruit/index.html#recruit-openings")},
    "news": {"label": "NEWS", "ja": "お知らせ", "h2": ["久留米興業の日々を、", "もっと身近に。"],
             "lead": "仕事の取り組みや社員の声など、久留米興業を知るきっかけをお届けします。",
             "items": [("2024-03-08", "2024.03.08", "お知らせ", "令和6年度能登半島地震に伴う災害救援隊について", DISASTER),
                       ("2021-11-25", "2021.11.25", "お知らせ", "ホームページをリニューアルしました。", "https://www.kurume-k.jp/452874803881/belrfza5rwefayabmajbx6d6kkhafj")],
             "cta": ("お知らせ一覧へ", OFFICIAL_NEWS)},
    "close": {"label": "CONTACT", "h2": ["久留米興業を、もっと知る。"],
              "lead": "事業のこと、採用のこと。知りたいことに合わせてお進みください。",
              "cta": [("事業内容を見る", "@P1@business/index.html"), ("採用情報を見る", "@P1@recruit/index.html")],
              "sub": ("工事・事業に関するお問い合わせ（公式フォーム）", OFFICIAL_CONTACT)},
}

P2 = {
    "hero": {"label": "KURUME KOGYO / SINCE 1974", "h1": ["この街とともに、50年以上。", "働き方も、未来も、変えていく。"],
             "lead": "道路を直し、水道を支える。その仕事をこれからも続けていくために、働く人のことも考え続ける。久留米興業が守ってきたものと、変えようとしていることをご紹介します。",
             "img": ("field-work-street.jpg", "歩道の舗装工事を進める久留米興業の現場"), "caption": "世田谷の道路と人を支える仕事",
             "cta": [("久留米興業の歩みを知る", "@P2@about/index.html#about-history"), ("この会社で働く", "@P2@recruit/index.html")]},
    "story": {"label": "OUR STORY", "ja": "会社の歩み", "h2": ["1974年から、", "街の日常と向き合ってきた。"],
              "body": "世田谷を拠点に、道路の舗装復旧や維持、水道工事に携わってきた久留米興業。半世紀以上の歩みの先にあるのは、これからも街の暮らしを支えていくという仕事です。",
              "img": ("entrance-sunny.jpg", "「(株)久留米興業」の看板が掲げられた現在の本社入口"), "caption": "現在の本社（東京都世田谷区北烏山）",
              "cta": ("会社の歩みと事業を見る", "@P2@about/index.html#about-history")},
    "leader": {"label": "THE PEOPLE BEHIND CHANGE", "ja": "代表の歩み", "h2": ["「何のために働くのか」を、", "考えたことがあるから。"],
               "body": "18歳で現場に入り、24歳で一度会社を離れた川島代表。現場・管理・経営を経験し、今は働く時間や人の負担にも目を向けながら、次の世代へつながる会社づくりを考えています。",
               "steps": [("18歳", "現場に入る"), ("24歳", "一度会社を離れる"), ("現在", "現場・管理・経営を経て、会社づくりへ")],
               "img": ("ceo-portrait.jpg", "代表取締役 川島 和範"), "caption": "代表取締役　川島 和範",
               "gate": "代表の経歴は代表インタビューの再構成原稿：本人確認待ち",
               "cta": [("川島代表の歩みと想い", "@P2@about/index.html#about-representative"), ("代表と働く人を知る", "@P2@people/index.html#people-president")]},
    "change": {"label": "CHANGES IN PRACTICE", "ja": "働き方の見直し", "h2": ["守るために、", "変えるという選択。"],
               "lead": "昔からのやり方を続けるだけでは、働く人も仕事も守り続けられない。久留米興業では、現場の経験を持つ代表が、働き方の見直しに向き合ってきました。",
               "items": [("勤務時間を見直す", "定時を意識し、残業時間を管理することから働き方を見直してきました。"),
                         ("現場の負担を分け合う", "一人だけに無理を集中させず、人員の配置にも目を向けています。"),
                         ("個性を同じ型にはめない", "得意なことや仕事の進め方が違っても、同じ目標へ進める関係を大切にしています。")],
               "honest": "課題もあります。現場には今も忙しい日や体力的な負担があり、その実際は採用情報の「仕事のリアル」でお伝えしています。",
               "cta": [("変化の理由と現在を知る", "@P2@about/index.html#about-change"), ("これからの課題を見る", "@P2@future/index.html#future-workstyle")]},
    "work": {"label": "OUR BUSINESS", "ja": "事業", "h2": ["目立たない仕事が、", "街の毎日を支えている。"],
             "lead": "道が通れること、水が届くこと。特別な出来事ではない日常を支えるために、現場で人が動き、工事が進みます。",
             "items": [("ガス管取替後の復旧舗装工事", "工事が終わった道路を元のように整え、毎日の通行を支える。", "paving-roller.jpg", "ローラーで舗装を転圧している現場"),
                       ("路面改良・維持工事", "傷みや変化が生じた道路を維持・改良し、安全な通行を支える。", "civil-road.jpg", "カラー舗装で仕上げた道路"),
                       ("水道管布設・布設替工事", "暮らしに欠かせない水道インフラを整える。", "water-pipe.jpg", "掘削した溝に水道管を布設している現場"),
                       ("自治体の緊急要請への対応", "雪かきや土嚢作成など、地域で必要とされる対応にも取り組む。", None, None)],
             "cta": ("久留米興業の仕事を知る", "@P2@about/index.html#about-business")},
    "voices": {"label": "REAL VOICES", "ja": "社員の声", "h2": ["どんな人が働いているのか。", "答えは、社員の言葉にある。"],
               "lead": "同じ会社でも、入社のきっかけや仕事の覚え方は人それぞれ。営業と現場、実際に働く人の経験から、久留米興業の姿を見てください。",
               "sales": [("根岸さん", "異業種から現場代理人へ", "お茶の営業から転職し、公共工事の現場調整と資格取得へ。", "member-n.jpg", BLOG_NEGISHI),
                         ("高畑さん", "新卒から営業を経験", "業界用語も分からない時期に先輩の支えを受け、仕事を覚えてきた。", "member-t2.jpg", BLOG_TAKAHATA),
                         ("今井さん", "広告業界から転職", "現場での衝突を経験し、職人との対話を通じて調整力を磨いた。", "member-i2.jpg", BLOG_IMAI)],
               "field": [("松野さん", "班長", "長年の現場経験から、役割分担と新人の成長について話しています。"),
                         ("奥居さん", "現場職", "建築から土木へ。先輩に聞きながら仕事を覚え、現場の大変さも率直に話しています。")],
               "cta": [("社員の実話から仕事を知る", "@P2@recruit/index.html#recruit-voices"), ("働くスタッフを知る", "@P2@people/index.html")],
               "blog": ("公開中の営業社員インタビュー", BLOG_LIST)},
    "next": {"label": "FOR THE NEXT 50 YEARS", "ja": "これから", "h2": ["仕事が続くために、", "人が育つ会社でありたい。"],
             "body": "これからも街のインフラを守っていくには、次の世代へ経験や技術を渡していく必要があります。未完成なところも見直しながら、人が長く働ける会社を目指しています。",
             "img": ("field-team-back.jpg", "歩道の工事で、それぞれの持ち場で作業する現場職"), "caption": "次の世代へ、仕事を渡していく",
             "cta": ("久留米興業の未来を見る", "@P2@future/index.html")},
    "recruit": {"label": "JOIN OUR TEAM", "ja": "採用情報", "h2": ["仕事の中身も、大変さも", "知ってから選んでほしい。"],
                "lead": "取引先と現場をつなぐ営業職。現場で手を動かし、街を整える現場職。仕事の種類も、最初に覚えることも違います。入社後を想像できるよう、実際の情報をご案内します。",
                "items": [("営業職｜人と現場をつなぐ仕事", "SALES", "相談・見積・段取り・現場との連携。", "office-pc.jpg", "事務所で資料を確認する社員", ("営業職の仕事を見る", "@P2@recruit/index.html#recruit-role-sales")),
                          ("現場職｜仲間とつくる仕事", "FIELD WORK", "現場の流れを学び、安全を守りながら施工に携わる。", "field-worker-helmet.jpg", "ヘルメットをかぶって作業する現場職", ("現場職の仕事を見る", "@P2@recruit/index.html#recruit-role-field"))],
                "cta": ("待遇・募集要項を確認する", "@P2@recruit/index.html#recruit-offerings")},
    "proof": {"label": "WORKS & NEWS", "ja": "実際の仕事", "h2": ["言葉の先にある、", "実際の仕事。"],
              "lead": "現場の写真や会社の活動にも、久留米興業の日常が表れています。施工の様子と、地域に関わる取り組みをご紹介します。",
              "photos": [("work-kamisoshigaya.jpg", "歩道の舗装を終えた現場と工事黒板"), ("work-chisaki.jpg", "新しく舗装した生活道路と工事黒板")],
              "news": ("2024-03-08", "2024.03.08", "会社の活動", "令和6年度能登半島地震に伴う災害救援隊について", DISASTER),
              "cta": [("実際の施工を見る", OFFICIAL_WORKS), ("企業の取り組みを見る", OFFICIAL_NEWS)]},
    "close": {"label": "NEXT STEP", "h2": ["久留米興業を、", "もう少し知ってみませんか。"],
              "lead": "仕事のこと、会社の歩み、実際に働く人のこと。気になるところから、詳しく見ていただけます。",
              "cta": [("会社の歩みと想いを知る", "@P2@about/index.html"), ("働く人の声を読む", "@P2@people/index.html"), ("募集・働き方を知る", "@P2@recruit/index.html")]},
}


def br(lines):
    return "<br>".join(lines)


def is_ext(href):
    return href.startswith("http")


def a(label, href, cls="", arrow=None):
    c = f' class="{cls}"' if cls else ""
    if is_ext(href):
        arr = arrow or "↗"
        return f'<a{c} href="{href}" target="_blank" rel="noopener noreferrer">{label} <span aria-hidden="true">{arr}</span><span class="sr-only">（外部サイトが開きます）</span></a>'
    arr = arrow or "→"
    return f'<a{c} href="{href}">{label} <span aria-hidden="true">{arr}</span></a>'

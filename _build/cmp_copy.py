# 比較用TOP（デザイン②・③）の共通文章・写真・リンク（2026-11-06 改訂：法人向け優先・01_REVISED_CONTENT_MASTER準拠）。
# 同じ構成のデザイン②・③は、このデータだけを使う（見出し・本文・リンクをそろえ、違いは画面の構造・写真の見せ方・文字組み・動きで出す）。
from common import OFFICIAL_CONTACT, OFFICIAL_WORKS, OFFICIAL_NEWS, DISASTER, BLOG_NEGISHI, BLOG_TAKAHATA, BLOG_IMAI, BLOG_LIST

PH = "@R@assets/photos/"
TEL = "03-3309-3786"
ADDRESS = "〒157-0061 東京都世田谷区北烏山6丁目26-28"

FIELDS = [  # 正式な4工種（構成①・②で共通）
    ("ガス管取替後の復旧舗装工事", "service-gas"),
    ("水道工事", "service-water"),
    ("一般土木工事", "service-civil"),
    ("下水道工事", "service-sewer"),
]

P1 = {
    "hero": {"label": "INFRASTRUCTURE / KURUME KOGYO", "h1": ["道路の復旧舗装から、", "水道・土木工事まで。"],
             "lead": "世田谷を拠点に、ガス管取替後の復旧舗装工事をはじめ、水道・一般土木・下水道工事に携わる株式会社久留米興業。道路と街のインフラに関わる施工領域をご紹介します。",
             "img": ("field-work-street.jpg", "重機とともに歩道の路盤をつくる施工中の現場"), "caption": "施工中の様子",
             "cta": [("事業内容を見る", "@P1@business/index.html"), ("会社情報を見る", "@P1@company/index.html")]},
    "about": {"label": "SINCE 1974", "ja": "会社概要", "h2": ["1974年から、", "現場と地域に向き合う。"],
              "body": "久留米興業は1974年設立。道路や水道に関わる工事を通じ、地域の暮らしを支えてきました。現在の会社の姿と、取り組んできた事業を知っていただけるページです。",
              "facts": [("設立", "1974年3月4日"), ("所在地", "東京都世田谷区北烏山6丁目26-28"), ("主な事業", "復旧舗装・水道・一般土木・下水道"), ("関連会社", "KRM株式会社")],
              "img": ("entrance.jpg", "「(株)久留米興業」の看板が掲げられた本社の敷地入口"), "caption": "現在の本社",
              "cta": ("会社の概要を見る", "@P1@company/index.html#company-overview")},
    "business": {"label": "OUR WORK", "ja": "事業内容", "h2": ["対応する工事を、明確に。"],
                 "lead": "ガス管取替後の道路復旧から、水道・土木・下水道工事まで。主な事業領域を整理しました。発注内容に近い分野から詳しい情報をご覧ください。",
                 "items": [("ガス管取替後の復旧舗装工事", "ガス管の取替後に行う道路の舗装復旧工事。", "paving-roller.jpg", "ローラーで舗装を転圧している現場", "@P1@business/index.html#service-gas"),
                           ("水道工事", "水道管の布設・布設替など、給水インフラに関わる工事。", "water-pipe.jpg", "掘削した溝に配水管を布設している現場", "@P1@business/index.html#service-water"),
                           ("一般土木工事", "道路の改良・維持など、公共空間の基盤に関わる土木工事。", "civil-road.jpg", "カラー舗装で仕上げた道路", "@P1@business/index.html#service-civil"),
                           ("下水道工事", "下水道の整備など、生活環境を支える工事。", None, None, "@P1@business/index.html#service-sewer")],
                 "cta": ("施工領域を詳しく見る", "@P1@business/index.html")},
    "approach": {"label": "COORDINATION", "ja": "仕事の進め方", "h2": ["施工の先にある、", "信頼まで。"],
                 "lead": "工事は、取引先・現場・協力会社・地域の方々との連携によって進みます。担当する仕事の内容だけでなく、現場を円滑に進めるための関係づくりも大切にしています。",
                 "steps": [("CLIENT", "取引先・発注者", "工事の内容や場所、時期などのご相談を受けて、仕事が始まります。"),
                           ("COORDINATION", "営業・調整", "現地の確認、見積、人や材料・日程の段取りを整え、現場とつなぎます。"),
                           ("CONSTRUCTION", "現場・施工", "安全を確かめながら班で役割を分け、近隣にも配慮して施工を進めます。")],
                 "note": "仕事の進め方を説明するための図です。工事ごとの詳しい流れは事業内容のページでご案内しています。",
                 "img": ("field-crew-hq.jpg", "歩道の路盤をつくる施工中のチーム"),
                 "cta": [("仕事内容を知る", "@P1@business/index.html#business-process"), ("会社の考え方を見る", "@P1@company/index.html#company-values")]},
    "works": {"label": "PROJECT SCENES", "ja": "施工の様子", "h2": ["現場を、写真で確かめる。"],
              "lead": "施工内容を検討する際には、言葉だけでなく実際の現場の様子も大切な判断材料です。久留米興業の仕事を、確認できた写真とともにご紹介します。",
              "items": [("work-kamisoshigaya.jpg", "歩道の舗装を終えた現場と工事黒板", "令和3年度 道路維持工事（世田谷区上祖師谷）"),
                        ("work-kyuden.jpg", "舗装を仕上げた車道", "世田谷区給田（表層改良）"),
                        ("work-chisaki.jpg", "新しく舗装した生活道路と工事黒板", "世田谷区上祖師谷（地先道路築造工事）")],
              "cta": [("対応工事を詳しく見る", "@P1@business/index.html"), ("施工実績を見る", OFFICIAL_WORKS)]},
    "workstyle": {"label": "OUR TEAMWORK", "ja": "働き方", "h2": ["施工を支えるのは、", "人と段取り。"],
                  "lead": "現場で施工する人、取引先と現場をつなぐ人。それぞれの役割や働き方を紹介しています。仕事の進め方を知ることは、会社を理解することにもつながります。",
                  "office": ("office.jpg", "社員がデスクで仕事をする事務所の様子", "事務所"),
                  "field": ("field-worker-helmet.jpg", "ヘルメットをかぶって作業する社員", "現場"),
                  "words": [("組織", "事務所と現場で役割を分ける"), ("段取り", "人・材料・日程を整える"), ("施工", "班で安全に仕上げる")],
                  "cta": ("労働環境を見る", "@P1@work-environment/index.html")},
    "people": {"label": "OUR MEMBERS", "ja": "働くメンバー", "h2": ["現場と事務所、", "役割は違っても。"],
               "lead": "工事は一人では完成しません。営業、現場、管理を担う人たちのそれぞれの視点から、久留米興業で働く実像をご紹介します。",
               "img": ("office-wide.jpg", "複数の社員がデスクで仕事をする事務所"),
               "links": [("PRESIDENT", "代表", "現場から経営まで、代表の歩み", "@P1@people/index.html#people-ceo"),
                         ("SALES", "営業職", "取引先と現場をつなぐ社員の経験", "@P1@people/index.html#people-sales"),
                         ("FIELD", "現場職", "班で施工を進める現場の仕事", "@P1@people/index.html#people-field")],
               "cta": ("働くメンバーを知る", "@P1@people/index.html")},
    "recruit": {"label": "CAREERS", "ja": "採用情報", "h2": ["次のインフラを支える仲間へ。"],
                "lead": "営業職と現場職、それぞれの仕事には異なる専門性があります。入社後の流れ、評価、働く環境、募集条件は採用情報ページで詳しく紹介しています。",
                "roles": [("営業職", "SALES", "取引先と現場をつなぐ、見積・調整・手配の仕事。", "office-pc.jpg", "事務所でパソコンに向かう社員", "@P1@recruit/index.html#career-sales"),
                          ("現場職", "FIELD WORK", "道路やインフラ工事の現場で、チームとともに施工する仕事。", "field-team-back.jpg", "歩道の工事でそれぞれの持ち場で作業する社員", "@P1@recruit/index.html#career-field")],
                "cta": ("採用情報・募集条件を見る", "@P1@recruit/index.html")},
    "news": {"label": "JOURNAL", "ja": "取り組み", "h2": ["久留米興業の取り組みを知る。"],
             "lead": "仕事の取り組みや社員へのインタビューなど、会社の実際の姿を伝える記事をご案内します。",
             "items": [("2024-03-08", "2024.03.08", "お知らせ", "令和6年度能登半島地震に伴う災害救援隊について", DISASTER),
                       ("", "", "社員インタビュー", "営業職・根岸さん：異業種から現場代理人へ", BLOG_NEGISHI),
                       ("", "", "社員インタビュー", "営業職・高畑さん：新卒・未経験から営業へ", BLOG_TAKAHATA),
                       ("", "", "社員インタビュー", "営業職・今井さん：広告業界から土木の調整役へ", BLOG_IMAI)],
             "cta": ("公開記事一覧を見る", BLOG_LIST)},
    "contact": {"label": "GET IN TOUCH", "ja": "お問い合わせ", "h2": ["工事のご相談から、", "会社のことまで。"],
                "lead": "事業内容や会社概要をご覧いただき、工事に関するお問い合わせは正式な窓口へ。久留米興業で働くことに関心のある方には、採用情報もご案内しています。",
                "client": [("お問い合わせフォーム", OFFICIAL_CONTACT), ("会社情報を見る", "@P1@company/index.html")],
                "recruit": ("採用情報を見る", "@P1@recruit/index.html"),
                "img": ("machine.jpg", "「久留米興業」の社名が入った重機")},
}

P2 = {
    "hero": {"label": "1974 / TODAY / NEXT", "h1": ["この街とともに、50年以上。", "信頼をつなぎ、次の時代へ。"],
             "lead": "ガス管取替後の復旧舗装工事や水道・土木工事。1974年から積み重ねた仕事と、人を大切にする会社づくり。久留米興業の歩みと、これからを紹介します。",
             "site": ("field-work-street.jpg", "重機とともに歩道の路盤をつくる施工中の現場", "施工中の様子"),
             "office": ("office.jpg", "社員がデスクで仕事をする事務所", "事務所"),
             "cta": [("久留米興業について", "@P2@about/index.html"), ("事業を知る", "@P2@about/index.html#about-business")]},
    "history": {"label": "SINCE 1974", "ja": "会社の歩み", "h2": ["守ってきた仕事が、", "今の街につながる。"],
                "lead": "世田谷で半世紀以上、道路や水道に関わる工事に取り組んできた久留米興業。長く続く仕事の背景には、地域・取引先・社員とのつながりがあります。",
                "img": ("entrance-sunny.jpg", "「(株)久留米興業」の看板が掲げられた現在の社屋", "現在の社屋"),
                "people_img": ("office-floor.jpg", "社員が働く現在の事務所", "現在の職場"),
                "cta": ("会社の歩みを知る", "@P2@about/index.html#about-history")},
    "leader": {"label": "A PERSONAL POINT OF VIEW", "ja": "代表の経験", "h2": ["経験したから、", "変えたいことがある。"],
               "lead": "18歳で現場に入り、24歳で一度会社を離れた川島代表。現場と管理、そして経営を経験してきたからこそ、仕事を続ける人の負担や働き方にも目を向けています。",
               "facts": [("18歳", "現場に入る"), ("24歳", "一度会社を離れる"), ("その後", "現場・管理・経営を経験")],
               "img": ("ceo-portrait.jpg", "代表取締役 川島 和範", "代表取締役　川島 和範"),
               "gate": "代表の経歴は代表インタビューの再構成：本人の掲載承認待ち",
               "cta": ("代表のストーリーを見る", "@P2@about/index.html#about-representative")},
    "change": {"label": "WORK IN PROGRESS", "ja": "守ること・変えること", "h2": ["仕事の価値は守る。", "働き方は、見直し続ける。"],
               "lead": "勤務時間の管理、負担を分ける人員配置、異なる個性の尊重。現場の厳しさも残るからこそ、会社づくりは完成形ではありません。",
               "keep": ["インフラを支える仕事", "取引先との信頼", "仲間との連携"],
               "change": ["時間の管理", "現場の負担", "経験を次へ渡す仕組み"],
               "points": [("時間の管理", "定時を意識し、残業時間を管理することから働き方を見直してきました。"),
                          ("人員の配置", "一人だけに無理を集中させず、人を増やして負担を分ける考え方に取り組んできました。"),
                          ("個性の尊重", "得意なことや仕事の進め方が違っても、同じ目標へ進める関係を大切にしています。")],
               "honest": "現場には今も忙しい日や、休憩に余裕を感じにくい日があります。取り組みは途中です。",
               "imgs": [("office-staff-closeup-03.jpg", "事務所のデスクで仕事をする社員", "職場"), ("process-remove.jpg", "重機で古い舗装を撤去する現場", "現場")],
               "cta": ("会社の未来を見る", "@P2@future/index.html")},
    "business": {"label": "4 BUSINESS FIELDS", "ja": "事業", "h2": ["社会に必要な工事を、", "毎日の現場で。"],
                 "lead": "道路を元の状態に戻し、地域の水道・下水道や土木の仕事に携わる。仕事の形は異なっても、その先には利用する人の生活があります。",
                 "items": [("ガス管取替後の復旧舗装工事", "ガス管取替後の道路を舗装復旧する工事。", "paving-roller.jpg", "ローラーで舗装を転圧している現場"),
                           ("水道工事", "水道管の布設・布設替など、供給基盤に関わる工事。", "water-pipe.jpg", "掘削した溝に水道管を布設している現場"),
                           ("一般土木工事", "道路の維持・改良など、地域の土木工事。", "civil-road.jpg", "カラー舗装で仕上げた道路"),
                           ("下水道工事", "下水道整備など、生活基盤に関わる工事。", None, None)],
                 "life": ("work-kyuden.jpg", "住宅地の中で舗装を仕上げた道路", "工事を終えた生活道路"),
                 "cta": ("事業内容を詳しく見る", "@P2@about/index.html#about-business")},
    "voices": {"label": "PEOPLE ARE THE STORY", "ja": "社員の声", "h2": ["会社を語るのは、", "そこで働く人たち。"],
               "lead": "異業種から営業に転職した人、長年現場を支えてきた人、建築から土木へ移った人。それぞれ違う経歴と視点から、久留米興業の実像が見えてきます。",
               "sales": [("根岸さん", "営業職", "お茶の営業から転職。公共工事の現場調整と資格取得を経て、現場代理人へ。", "member-n.jpg", BLOG_NEGISHI),
                         ("高畑さん", "営業職", "新卒・土木未経験で入社。先輩の仕事に同行しながら、現場の知識を増やしてきた。", "member-t2.jpg", BLOG_TAKAHATA),
                         ("今井さん", "営業職", "広告業界から転職。現場の職人との対話を重ねて、調整の進め方を身につけてきた。", "member-i2.jpg", BLOG_IMAI)],
               "talk": {"title": "現場職の二人の対談", "people": [("松野さん", "班長", "長年の現場経験から、役割分担と、新人に少しずつ覚えてほしいという考えを話しています。"),
                                                              ("奥居さん", "現場職", "建築から土木へ。先輩に聞きながら仕事を覚え、暑さや時間の厳しさも率直に話しています。")]},
               "cta": [("働くスタッフ紹介を見る", "@P2@people/index.html"), ("公開インタビューを読む", BLOG_LIST)]},
    "future": {"label": "NEXT 50 YEARS", "ja": "これから", "h2": ["続けていくために、", "変わっていく。"],
               "lead": "次の世代に仕事をつなぎ、経験や技術を伝え、働く人にとって続けられる会社へ。実施してきたことと、これから整えたいことの両方をお伝えします。",
               "keep": ("工事を、次の世代へ。", "現場で培った技術と経験を、新しく加わる人へ渡していくことを目指しています。"),
               "change": ("育成と環境を、整えていく。", "教える側の余裕や仕組みがまだ十分でないことも認識し、教え方と働き方を見直していく考えです。"),
               "imgs": [("field-team-back.jpg", "歩道の工事でそれぞれの持ち場で作業する社員", "現場"), ("office-wide.jpg", "複数の社員がデスクで仕事をする事務所", "事務所")],
               "cta": ("久留米興業の未来を見る", "@P2@future/index.html")},
    "recruit": {"label": "CAREER CHOICES", "ja": "採用情報", "h2": ["自分の役割を、", "ここから見つける。"],
                "lead": "会社の考え方に共感できたら、働く現実も確かめてください。営業職と現場職それぞれの仕事、経験の積み方、待遇や募集条件を採用ページで説明しています。",
                "roles": [("営業職", "SALES", "取引先と現場をつなぐ調整・見積・段取り。", "office-pc.jpg", "事務所でパソコンに向かう社員", "@P2@recruit/index.html#recruit-role-sales"),
                          ("現場職", "FIELD WORK", "道路工事の現場で、先輩や仲間から学びながら施工を担う。", "field-worker-helmet.jpg", "ヘルメットをかぶって作業する社員", "@P2@recruit/index.html#recruit-role-field")],
                "cta": ("採用情報・募集要項を見る", "@P2@recruit/index.html"),
                "conditions": ("給与・休日などの条件は募集要項で確認する", "@P2@recruit/index.html#recruit-offerings")},
    "proof": {"label": "WORK / PEOPLE / REALITY", "ja": "実際の仕事と人", "h2": ["言葉だけでなく、", "現場と人の実像を。"],
              "lead": "会社の歩みや考え方は、実際の仕事や社員の話に表れます。現場写真と公開インタビューを通して、久留米興業の日常をご覧ください。",
              "photos": [("work-kamisoshigaya.jpg", "歩道の舗装を終えた現場と工事黒板", "施工を終えた歩道"), ("work-chisaki.jpg", "新しく舗装した生活道路と工事黒板", "施工を終えた生活道路")],
              "reads": [("社員インタビュー", "根岸さん｜異業種から現場代理人へ", BLOG_NEGISHI),
                        ("社員インタビュー", "高畑さん｜新卒・未経験から営業へ", BLOG_TAKAHATA),
                        ("社員インタビュー", "今井さん｜広告業界から土木の調整役へ", BLOG_IMAI),
                        ("会社の活動", "令和6年度能登半島地震に伴う災害救援隊について", DISASTER)],
              "cta": [("事業を知る", "@P2@about/index.html#about-business"), ("社員の声を読む", "@P2@people/index.html")]},
    "close": {"label": "YOUR NEXT STEP", "h2": ["久留米興業の仕事と、", "これからを。"],
              "lead": "工事について知りたい方は事業紹介へ。会社の歩みや考え方に関心のある方は、会社紹介へ。働くことを検討される方には採用情報をご案内します。",
              "cta": [("事業内容を見る", "@P2@about/index.html#about-business", "工事を知る"),
                      ("会社情報を見る", "@P2@company/index.html", "会社を知る"),
                      ("採用情報を見る", "@P2@recruit/index.html", "働くことを知る")]},
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

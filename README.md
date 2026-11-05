# 久留米興業様 Webサイト｜構成パターン × デザインパターン比較

構成パターン（①会社理解重視／②ビジョン共感）とデザインパターン（①コーポレート／②シンプル／③表現重視）を比較するための静的プロトタイプです。CAREECONマーケティングCMSへ移植する前の確認用で、本番公開物ではありません（全ページ `noindex`）。

## 比較ページ（1画面で切り替え）

`compare/` を開くと、左で構成・デザイン・ページ・表示幅（PC／1024px／スマホ）・確認用／公開イメージを切り替え、右に選んだページを表示します。左の一覧は16画面すべてへのリンクで、上層ページを兼ねます。URLの `#p2-d3` や `#p1-d1-recruit` で表示中の組み合わせを共有できます。

## 画面一覧（16画面）

| 構成 × デザイン | パス | 範囲 |
|---|---|---|
| ① × ① | `index.html` ほか下表 | 6ページ（既存・URL変更なし） |
| ② × ① | `pattern2/`（`about/` `recruit/` `people/` `future/` `company/`） | 6ページ |
| ① × ② | `compare/pattern1/design-a/` | TOPのみ |
| ① × ③ | `compare/pattern1/design-b/` | TOPのみ |
| ② × ② | `compare/pattern2/design-a/` | TOPのみ |
| ② × ③ | `compare/pattern2/design-b/` | TOPのみ |

画面右下の「比較」から、構成とデザインを別々に選んで切り替えられます（`#compare` を付けたURLはパネルを開いた状態で表示）。デザイン②・③はTOPのみのため、下層ページから選んだ場合は同じ構成のTOPへ移動します。比較切替は `assets/compare/switcher.js / switcher.css` の独立部品で、各ページの読み込み2行を消せば外せます。

### パターン① × デザイン①

| ページ | パス |
|---|---|
| ① TOP | `index.html` |
| ② 事業内容 | `business/` |
| ③ 採用情報 | `recruit/` |
| ④ 労働環境 | `work-environment/` |
| ⑤ 働くメンバー | `people/` |
| ⑥ 会社情報 | `company/` |

- 共通CSS：`assets/site.css`／共通JS：`assets/site.js`（JSは独立管理）
- 各セクションの `data-cms-id`（CMS Section ID）と `data-implementation`（方式A/B/C）は開発用メモです。
- 画面左下の「確認用／公開イメージ」はデモ専用の表示切替です（承認前の項目の表示・非表示）。CMSには移植しません。

## 修正のしかた
HTMLは `_build/` のPythonから生成しています。外部リンク先は `_build/common.py` の先頭にまとめてあります。

```
python3 _build/build.py
```

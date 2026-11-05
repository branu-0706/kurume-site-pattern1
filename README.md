# 久留米興業様 Webサイト｜パターン① × デザイン①（①〜⑥）

構成パターン①「会社理解重視」× デザイン①「コーポレート」の静的プロトタイプです。CAREECONマーケティングCMSへ移植する前の確認用で、本番公開物ではありません（全ページ `noindex`）。

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

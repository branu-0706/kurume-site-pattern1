# -*- coding: utf-8 -*-
"""TOPのファーストビュー：CMS標準セクションの組み合わせ（CTAなし・画像と文字だけ）。
  721 Mainvisual Responsive Slider … 施工写真1枚の上に、ラベル・H1・リード・対応工事（テキスト）を重ねる（自動切替なし）
  文字の下には暗幕（ネイビーのグラデーション）を敷き、写真が明るくてもコントラスト4.5:1以上を保つ
独自HTMLは使わない。見た目の違いは各デザインのCSS（余白・文字サイズ・揃え・写真の高さ）だけで出す。"""

FIELDS4 = ["ガス管取替後の復旧舗装工事", "水道工事", "一般土木工事", "下水道工事"]


def top_hero(sid, tid, label, h1, lead, src, alt, cls="", fields=True, w=941, h=627):
    fl = ""
    if fields:
        fl = '\n      <ul class="fv-fields" aria-label="対応する工事">' + "".join(f"<li>{t}</li>" for t in FIELDS4) + "</ul>"
    return f'''<!-- 01 MAIN VISUAL｜方式B：CMS 721 Mainvisual Responsive Slider（写真1枚＋キャッチコピー・自動切替なし。H1はページで1つ）＋ CSS（文字位置・余白・文字サイズ・写真の高さ・暗幕の濃さのみ）。CTAなし -->
<section class="fv-mv {cls}" id="{sid}" aria-labelledby="{tid}" data-cms-id="721" data-implementation="B">
  <div class="fv-slide">
    <img src="{src}" alt="{alt}" width="{w}" height="{h}" fetchpriority="high">
    <div class="fv-copy">
      <p class="fv-label">{label}</p>
      <h1 id="{tid}">{h1}</h1>
      <p class="fv-lead">{lead}</p>{fl}
    </div>
  </div>
</section>'''

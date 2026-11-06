# -*- coding: utf-8 -*-
"""TOPのファーストビュー：CMS標準セクションの組み合わせ（CTAなし・画像と文字だけ）。
  734 H1 Center ……… ラベル・H1・リード・対応工事（テキスト）
  721 Mainvisual Responsive Slider … 施工写真1枚（自動切替なし）
独自HTMLは使わない。見た目の違いは各デザインのCSS（余白・文字サイズ・揃え・写真の高さ）だけで出す。"""

FIELDS4 = ["ガス管取替後の復旧舗装工事", "水道工事", "一般土木工事", "下水道工事"]


def top_hero(sid, tid, label, h1, lead, src, alt, cls="", fields=True, w=941, h=627):
    fl = ""
    if fields:
        fl = '\n    <ul class="fv-fields" aria-label="対応する工事">' + "".join(f"<li>{t}</li>" for t in FIELDS4) + "</ul>"
    return f'''<!-- 01 HERO｜方式B：CMS 734 H1 Center（文字）＋ 721 Mainvisual Responsive Slider（写真1枚・自動切替なし）＋ CSS（余白・文字サイズ・揃え・写真の高さのみ）。CTAなし・画像と文字のみ。写真に文字を重ねない -->
<section class="fv-h1 {cls}" id="{sid}" aria-labelledby="{tid}" data-cms-id="734" data-implementation="B">
  <div class="fv-inner">
    <p class="fv-label">{label}</p>
    <h1 id="{tid}">{h1}</h1>
    <p class="fv-lead">{lead}</p>{fl}
  </div>
</section>
<section class="fv-mv {cls}" aria-label="施工の様子" data-cms-id="721" data-implementation="B">
  <div class="fv-slide"><img src="{src}" alt="{alt}" width="{w}" height="{h}" fetchpriority="high"></div>
</section>'''

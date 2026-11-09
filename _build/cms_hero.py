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


def ink_hero(sid, tid, label, h1, lead, imgs, en, cls=""):
    """D1のTOP（2026-11-09〜）：白黒写真＋吹き付けの筆跡＋手書き文字。CMS 721 Mainvisual に1枚の画像として登録する想定。
    imgs: [(src, alt), ...]（2枚なら左右に並べる。合成ではなく2場面）。文字はネイビーの筆跡の面に置く（背景色を持つのでコントラストを保てる）。"""
    split = " is-split" if len(imgs) > 1 else ""
    pics = "".join(f'<img src="{s}" alt="{a}" width="1600" height="1066" fetchpriority="high">' for s, a in imgs)
    fl = '<ul class="fv-fields" aria-label="対応する工事">' + "".join(f"<li>{t}</li>" for t in FIELDS4) + "</ul>"
    return f'''<!-- 01 MAIN VISUAL｜方式B：CMS 721 Mainvisual Responsive Slider（写真・筆跡・手書き文字を1枚の画像に仕上げて登録。H1はテキストで別に持つ）＋ CSS（assets/ink.css）。CTAなし。人物の顔が主役にならない写真を使う -->
<section class="fv-mv fv-ink {cls}" id="{sid}" aria-labelledby="{tid}" data-cms-id="721" data-implementation="B">
  <div class="fv-slide{split}">
    <div class="fv-pics">{pics}</div>
    <span class="ink-deco ink-lime fv-d1" aria-hidden="true"></span>
    <p class="fv-en" aria-hidden="true">{en}</p>
    {fl}
    <div class="fv-copy ink ink-navy">
      <p class="fv-label">{label}</p>
      <h1 id="{tid}">{h1}</h1>
      <p class="fv-lead">{lead}</p>
    </div>
  </div>
</section>'''

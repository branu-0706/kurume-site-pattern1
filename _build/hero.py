# -*- coding: utf-8 -*-
"""ファーストビュー（KV）共通部品。CTA・リンクは置かず、画像と文字だけで構成する。
スタイルは assets/hero.css（--kk-* 変数のみ参照）。写真の上に文字は重ねない（文字は無地の面に置く）。"""

P = "@R@assets/photos/"


def _img(src, alt, pos="50% 50%", w=1200, h=800):
    return (f'<img src="{P}{src}" alt="{alt}" width="{w}" height="{h}" '
            f'style="object-position:{pos}" fetchpriority="high">')


def _fields(items):
    lis = "".join(f'<li><span>{i+1:02d}</span>{t}</li>' for i, t in enumerate(items))
    return f'<ul class="kv-fields" aria-label="対応する工事">{lis}</ul>'


FIELDS4 = ["ガス管取替後の復旧舗装工事", "水道工事", "一般土木工事", "下水道工事"]


def cover(sid, tid, en, h1, lead, img, alt, pos, side, cms="721,734", note=""):
    """P1 TOP：全幅に近い写真＋左下に重なる無地パネル。"""
    return f'''<!-- 01 HERO｜KV cover（方式C：独自HTML＋CSS assets/hero.css）。CMS ID参考：{cms}。CTAなし・画像と文字のみ{note} -->
<section class="kv kv--cover" id="{sid}" aria-labelledby="{tid}" data-cms-id="{cms}" data-implementation="C">
  <figure class="kv-media anim-enter">{_img(img, alt, pos)}</figure>
  <p class="kv-side" aria-hidden="true">{side}</p>
  <div class="kv-panel anim-enter" style="--delay:.12s">
    <p class="kv-index"><span class="kv-no">01</span><span>{en}</span></p>
    <h1 id="{tid}">{h1}</h1>
    <p class="kv-lead">{lead}</p>
    {_fields(FIELDS4)}
  </div>
  <p class="kv-scroll" aria-hidden="true"><span></span>SCROLL</p>
</section>'''


def frame(sid, tid, no, en, jp, h1, lead, img, alt, pos, word, flip=False, cms="734", extra=""):
    """下層ページ：ブルーグレーの面に、ずらした額縁写真と大きな英字。"""
    cls = "kv kv--frame" + (" is-flip" if flip else "")
    return f'''<!-- 01 HERO｜KV frame（方式B：CMS {cms} H1 ＋ CSS assets/hero.css）。CTAなし・画像と文字のみ -->
<section class="{cls}" id="{sid}" aria-labelledby="{tid}" data-cms-id="{cms}" data-implementation="B">
  <p class="kv-word" aria-hidden="true">{word}</p>
  <div class="kv-wrap">
    <div class="kv-copy anim-enter">
      <p class="kv-index"><span class="kv-no">{no}</span><span>{en}</span></p>
      <p class="kv-eyebrow">{jp}</p>
      <h1 id="{tid}">{h1}</h1>
      <p class="kv-lead">{lead}</p>{extra}
    </div>
    <figure class="kv-media anim-enter" style="--delay:.12s">{_img(img, alt, pos)}</figure>
  </div>
</section>'''


def strip(sid, tid, no, en, jp, h1, lead, img, alt, pos, caption, dark=False, cms="734,721", extra=""):
    """P2下層：大きな見出しの下に、斜めに切ったパノラマ写真。"""
    cls = "kv kv--strip" + (" is-dark" if dark else "")
    return f'''<!-- 01 HERO｜KV strip（方式B：CMS {cms} H1 ＋ CSS assets/hero.css）。CTAなし・画像と文字のみ -->
<section class="{cls}" id="{sid}" aria-labelledby="{tid}" data-cms-id="{cms}" data-implementation="B">
  <div class="kv-wrap kv-head anim-enter">
    <p class="kv-index"><span class="kv-no">{no}</span><span>{en}</span><span class="kv-rule" aria-hidden="true"></span><span>{jp}</span></p>
    <h1 id="{tid}">{h1}</h1>
    <div class="kv-aside"><p class="kv-lead">{lead}</p>{extra}</div>
  </div>
  <figure class="kv-media anim-enter" style="--delay:.14s">{_img(img, alt, pos, 1600, 700)}<figcaption>{caption}</figcaption></figure>
</section>'''


def chapter(sid, tid, h1, lead, img, alt, pos, cms="734,721"):
    """P2 TOP：大きな年号と斜めに切った写真、下に4つの事業（テキストのみ）。"""
    return f'''<!-- 01 HERO｜KV chapter（方式C：独自HTML＋CSS assets/hero.css）。CMS ID参考：{cms}。CTAなし・画像と文字のみ -->
<section class="kv kv--chapter" id="{sid}" aria-labelledby="{tid}" data-cms-id="{cms}" data-implementation="C">
  <div class="kv-wrap">
    <div class="kv-copy anim-enter">
      <p class="kv-years" aria-hidden="true"><span>1974</span><i></i><span>NEXT</span></p>
      <h1 id="{tid}">{h1}</h1>
      <p class="kv-lead">{lead}</p>
    </div>
    <figure class="kv-media anim-enter" style="--delay:.12s">{_img(img, alt, pos)}<figcaption>SINCE 1974 — SETAGAYA, TOKYO</figcaption></figure>
  </div>
  <div class="kv-base anim-enter" style="--delay:.24s"><div class="kv-wrap"><p>4 BUSINESS FIELDS</p>{_fields(FIELDS4)}</div></div>
</section>'''

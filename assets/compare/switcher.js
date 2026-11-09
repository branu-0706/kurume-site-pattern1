/* 構成パターン × デザインパターンの比較切替（デモ専用・独立部品）
   ・<html data-structure="p1|p2" data-design="d1|d2|d3" data-page="..."> を読み取って現在地を表示する
   ・構成とデザインを別々に選び、「表示する」で該当ページへ移動する（URLのパスが状態を表す）
   ・デザイン②・③はTOPのみ。下層ページで選んだ場合は、その旨を表示して同じ構成のTOPへ移動する
   ・自分の読み込みURLからサイトのルートを求めるので、GitHub Pagesのサブパスでも動く
   CMS移植時は、このJSと switcher.css の読み込み2行を消すだけで外せる。 */
(()=>{
  'use strict';
  /* 比較ページ（compare/index.html）の中に表示されている時は、外側の操作を使うので出さない */
  try{if(window.self!==window.top&&/\/compare\/(index\.html)?$/.test(window.top.location.pathname))return;}catch(e){}
  const script=document.currentScript;
  const root=new URL('../../',script.src); // assets/compare/switcher.js → サイトのルート
  const html=document.documentElement;
  const cur={s:html.dataset.structure||'p1',d:html.dataset.design||'d1',page:html.dataset.page||'top'};

  const ROUTES={
    'p1-d1':'index.html',
    'p1-d2':'compare/pattern1/design-a/index.html',
    'p1-d3':'compare/pattern1/design-b/index.html',
    'p2-d1':'pattern2/index.html',
    'p2-d2':'pattern2/design-b/index.html',
    'p2-d3':'pattern2/design-c/index.html'
  };
  const S_LABEL={p1:'構成① 会社理解',p2:'構成② ビジョン共感'};
  /* デザインの名前は構成ごとに違う（2026-11-06 改訂） */
  const D_NAMES={p1:{d1:'基準（会社理解）',d2:'オフィシャル',d3:'表現重視'},p2:{d1:'A NAVY CURVE',d2:'B EDITORIAL',d3:'C CINEMA'}};
  const DL=(s,d)=>'デザイン'+({d1:'①',d2:'②',d3:'③'}[d])+' '+D_NAMES[s][d];
  const S_SHORT={p1:'構成①',p2:'構成②'};
  const D_SHORT={d1:'デザイン①',d2:'デザイン②',d3:'デザイン③'};

  /* 同じ構成のデザイン①で、今見ている下層ページを開き直す（D1同士の切替のみ） */
  const samePage=()=>location.href;

  const target=(s,d)=>{
    if(s===cur.s&&d===cur.d) return {href:samePage(),note:''};
    if(cur.page!=='top'&&s===cur.s&&d!=='d1'){
      return {href:new URL(ROUTES[s+'-'+d],root).href,note:'デザイン②・③はTOPのみの比較案です。'+S_SHORT[s]+'の'+D_SHORT[d]+'のTOPへ移動します。'};
    }
    if(cur.page!=='top'&&s!==cur.s){
      return {href:new URL(ROUTES[s+'-'+d],root).href,note:'構成①と構成②は下層ページの構成が異なるため、'+S_SHORT[s]+'の'+D_SHORT[d]+'のTOPへ移動します。'};
    }
    return {href:new URL(ROUTES[s+'-'+d],root).href,note:''};
  };

  const box=document.createElement('div');
  box.className='cmp-switcher';
  box.innerHTML=
    (window.KKTheme?'<button type="button" class="cmp-theme" aria-controls="kkt-panel">配色を調整</button>':'')+
    '<button type="button" class="cmp-toggle" aria-expanded="false" aria-controls="cmp-panel">'+
      '<span class="cmp-toggle-title">比較</span><span class="cmp-toggle-now">'+S_SHORT[cur.s]+' × '+D_SHORT[cur.d]+'</span></button>'+
    '<div class="cmp-panel" id="cmp-panel" role="dialog" aria-modal="false" aria-labelledby="cmp-title" hidden>'+
      '<div class="cmp-head"><p id="cmp-title">表示するパターンを選ぶ</p><button type="button" class="cmp-close" aria-label="閉じる">×</button></div>'+
      '<p class="cmp-now">現在：'+S_LABEL[cur.s]+' × '+DL(cur.s,cur.d)+(cur.page==='top'?'（TOP）':'（下層ページ）')+'</p>'+
      '<fieldset class="cmp-group"><legend>構成パターン</legend>'+
        ['p1','p2'].map(s=>'<label><input type="radio" name="cmp-s" value="'+s+'"'+(s===cur.s?' checked':'')+'><span>'+S_LABEL[s]+'</span></label>').join('')+
      '</fieldset>'+
      '<fieldset class="cmp-group"><legend>デザインパターン</legend>'+
        ['d1','d2','d3'].map(d=>'<label><input type="radio" name="cmp-d" value="'+d+'"'+(d===cur.d?' checked':'')+'><span class="cmp-dname" data-d="'+d+'">'+DL(cur.s,d)+'</span>'+(d==='d1'?'':'<small>'+(cur.s==='p2'?'':'TOPのみ')+'</small>')+'</label>').join('')+
      '</fieldset>'+
      '<p class="cmp-note" aria-live="polite"></p>'+
      '<a class="cmp-go" href="#">表示する</a>'+
      '<a class="cmp-hub" href="'+new URL('compare/index.html#'+cur.s+'-'+cur.d+(cur.d==='d1'&&cur.page!=='top'?'-'+cur.page:''),root).href+'">1画面で切り替えて比較（パターン①②③・全画面の一覧）</a>'+
    '</div>';
  document.body.appendChild(box);

  const btn=box.querySelector('.cmp-toggle');
  const panel=box.querySelector('.cmp-panel');
  const close=box.querySelector('.cmp-close');
  const note=box.querySelector('.cmp-note');
  const go=box.querySelector('.cmp-go');

  const selected=()=>({s:box.querySelector('input[name="cmp-s"]:checked').value,d:box.querySelector('input[name="cmp-d"]:checked').value});
  const update=()=>{
    const {s,d}=selected();
    box.querySelectorAll('.cmp-dname').forEach(n=>{n.textContent=DL(s,n.dataset.d);});
    const t=target(s,d);
    go.href=t.href;
    const same=(s===cur.s&&d===cur.d);
    go.textContent=same?'このページを表示中':(S_SHORT[s]+' × '+D_SHORT[d]+' を表示する');
    go.setAttribute('aria-disabled',String(same));
    note.textContent=t.note;
  };
  const open=()=>{panel.hidden=false;btn.setAttribute('aria-expanded','true');update();(box.querySelector('input:checked')||close).focus();};
  const shut=(focus)=>{panel.hidden=true;btn.setAttribute('aria-expanded','false');if(focus)btn.focus();};

  btn.addEventListener('click',()=>{if(window.KKTheme&&window.KKTheme.isOpen())window.KKTheme.close();panel.hidden?open():shut(false);});
  const tb=box.querySelector('.cmp-theme');
  if(tb)tb.addEventListener('click',()=>{shut(false);window.KKTheme.isOpen()?window.KKTheme.close():window.KKTheme.open(tb);});
  close.addEventListener('click',()=>shut(true));
  box.addEventListener('change',update);
  go.addEventListener('click',e=>{if(go.getAttribute('aria-disabled')==='true'){e.preventDefault();shut(true);}});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!panel.hidden)shut(true);});
  document.addEventListener('click',e=>{if(!panel.hidden&&!box.contains(e.target))shut(false);});
  if(location.hash==='#theme'&&window.KKTheme)window.KKTheme.open(tb);

  /* URLの #compare で、比較パネルを開いた状態で表示できる（共有・確認用） */
  if(location.hash==='#compare') open();
})();

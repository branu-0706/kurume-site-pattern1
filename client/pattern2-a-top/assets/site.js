/* 久留米興業 パターン① 共通JS（独立管理）。CMS移植時は共通JS入力欄に置き、読み込み位置とCSPを本番で確認する。 */
(()=>{
  'use strict';
  const root=document.documentElement;
  root.classList.add('js');

  /* ヘッダーの縮小 */
  const header=document.getElementById('site-header');
  if(header){
    const setHeader=()=>header.classList.toggle('scrolled',window.scrollY>18);
    setHeader();window.addEventListener('scroll',setHeader,{passive:true});
  }

  /* スマホメニュー */
  const menuButton=document.getElementById('menu-toggle');
  const menu=document.getElementById('mobile-nav');
  if(menuButton&&menu){
    const closeMenu=()=>{menu.hidden=true;menuButton.setAttribute('aria-expanded','false');menuButton.setAttribute('aria-label','メニューを開く');};
    menuButton.addEventListener('click',()=>{
      const open=menuButton.getAttribute('aria-expanded')!=='true';
      menu.hidden=!open;menuButton.setAttribute('aria-expanded',String(open));menuButton.setAttribute('aria-label',open?'メニューを閉じる':'メニューを開く');
    });
    menu.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu();});
    window.addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu();});
    window.addEventListener('resize',()=>{if(window.innerWidth>920)closeMenu();});
  }

  /* スクロール表示（非対応環境では最初から表示） */
  const revealNodes=[...document.querySelectorAll('.reveal')];
  revealNodes.forEach(n=>n.style.setProperty('--reveal-delay',n.dataset.delay||'0'));
  const reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if('IntersectionObserver' in window&&!reduce){
    const observer=new IntersectionObserver(entries=>{
      entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');observer.unobserve(e.target);}});
    },{threshold:.08,rootMargin:'0px 0px -30px 0px'});
    revealNodes.forEach(n=>observer.observe(n));
    /* 1.5秒後も画面外にあるものは表示状態にしておく（印刷・サムネイル対策） */
    setTimeout(()=>revealNodes.forEach(n=>{const r=n.getBoundingClientRect();if(r.top<window.innerHeight)n.classList.add('is-visible');}),1500);
  }else{revealNodes.forEach(n=>n.classList.add('is-visible'));}

  /* レビュー用：確認用 / 公開想定 の表示切替（デモ専用。CMS本番には移植しない） */
  const KEY='krk-view-mode';
  const setMode=m=>{
    root.classList.toggle('mode-review',m==='review');
    root.classList.toggle('mode-public',m==='public');
    document.querySelectorAll('[data-mode]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.mode===m)));
    try{localStorage.setItem(KEY,m);}catch(e){}
  };
  let saved='review';
  try{saved=localStorage.getItem(KEY)||'review';}catch(e){}
  setMode('public'); /* 送付用：常に公開イメージ */
  document.querySelectorAll('[data-mode]').forEach(b=>b.addEventListener('click',()=>setMode(b.dataset.mode)));
})();

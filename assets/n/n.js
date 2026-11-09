/* パターン②③（新デザイン）の動き。CMSでは「JS追加」に入れる想定。
   ・[data-n-slider]：メインビジュアルの写真を自動で切り替える（番号・見出し・進み具合の線も連動）
   ・[data-n-track]：横に送るカルーセル（矢印・進み具合の線）
   ・.n-rv：画面に入ったら表示（動きを減らす設定では最初から表示）
   動きを減らす設定（prefers-reduced-motion）では自動切替をしない。 */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var root = document.documentElement;
  root.classList.add('n-js');

  document.querySelectorAll('[data-n-slider]').forEach(function (box) {
    var slides = box.querySelectorAll('.n-slide');
    if (!slides.length) return;
    var cur = box.querySelector('.n-cur'), lab = box.querySelector('.n-lab'), bar = box.querySelector('.n-bar');
    var i = 0, dur = 5600;
    function show(n) {
      slides[i].classList.remove('is-on');
      i = (n + slides.length) % slides.length;
      slides[i].classList.add('is-on');
      if (cur) cur.textContent = (i < 9 ? '0' : '') + (i + 1);
      if (lab) lab.textContent = slides[i].getAttribute('data-label') || '';
      if (bar) { bar.style.animation = 'none'; void bar.offsetWidth; bar.style.animation = ''; }
    }
    if (bar) bar.style.setProperty('--n-dur', dur + 'ms');
    if (!reduce && slides.length > 1) setInterval(function () { if (!document.hidden) show(i + 1); }, dur);
  });

  document.querySelectorAll('[data-n-track]').forEach(function (track) {
    var id = track.id, ctrl = document.querySelector('[data-n-ctrl="' + id + '"]'), prog = document.querySelector('[data-n-progress="' + id + '"]');
    function step() { var c = track.querySelector('li'); return c ? c.getBoundingClientRect().width + 24 : 320; }
    function upd() {
      var max = track.scrollWidth - track.clientWidth;
      if (prog) prog.style.width = (max > 0 ? Math.max(12, (track.scrollLeft + track.clientWidth) / track.scrollWidth * 100) : 100) + '%';
      if (ctrl) { ctrl.querySelector('.n-prev').disabled = track.scrollLeft <= 2; ctrl.querySelector('.n-next').disabled = track.scrollLeft >= max - 2; }
    }
    if (ctrl) {
      ctrl.querySelector('.n-prev').addEventListener('click', function () { track.scrollBy({ left: -step(), behavior: reduce ? 'auto' : 'smooth' }); });
      ctrl.querySelector('.n-next').addEventListener('click', function () { track.scrollBy({ left: step(), behavior: reduce ? 'auto' : 'smooth' }); });
    }
    track.addEventListener('scroll', upd, { passive: true });
    window.addEventListener('resize', upd);
    upd();
  });

  // 表示アニメーションの対象はJSで付ける（HTMLはCMSのまま）。位置だけを動かし、透明にはしない（文字が読めない瞬間を作らない）
  document.querySelectorAll('.n-head,.n-biz-item,.n-card,.n-tile,.n-flow-list li,.n-num-list>div,.n-pick-list li,.n-vision-photo,.n-biz-tall,.m-entry-list li,.m-people-list li,.m-change-list li,.m-card-panel,.m-split,.m-biz-list li,.m-wide').forEach(function (e) { e.classList.add('n-rv'); });
  var items = document.querySelectorAll('.n-rv');
  if (reduce || !('IntersectionObserver' in window)) { items.forEach(function (e) { e.classList.add('is-in'); }); return; }
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -8% 0px' });
  items.forEach(function (e) { io.observe(e); });
})();

// 久留米興業サイト 品質チェック（公開前に必ず実行）
// 使い方: サイトのフォルダで `python3 -m http.server 8765` を起動してから `node _build/qa.js`
// 1) 写真の使い回し  2) 文字のコントラスト  3) 出典・制作メモの表記  4) 横スクロール・画像切れ・JSエラー・ページ内リンク・H1
const {chromium}=require('playwright');
const BASE=process.env.QA_BASE||'http://localhost:8765/';
const PAGES=['index.html','business/index.html','recruit/index.html','work-environment/index.html','people/index.html','company/index.html'];
const BANNED=['求人票','出典','採用ブログより','公式サイト','掲載表記','インタビューより','ヒアリング','CAREECON求人','求人ボックス'];
(async()=>{
  const b=await chromium.launch();const problems=[];const photoUse={};
  for(const [w,tag] of [[1440,'PC'],[390,'SP']]){
    const ctx=await b.newContext({viewport:{width:w,height:900}});
    for(const p of PAGES){
      const pg=await ctx.newPage();const errs=[];
      pg.on('pageerror',e=>errs.push(e.message));
      pg.on('requestfailed',r=>{if(!/fonts\.(googleapis|gstatic)/.test(r.url()))errs.push('読み込み失敗 '+r.url())});
      await pg.goto(BASE+p,{waitUntil:'networkidle'});
      // 公開イメージで確認（確認用の注記は対象外）
      await pg.evaluate(()=>{document.documentElement.classList.remove('mode-review');document.documentElement.classList.add('mode-public');document.querySelectorAll('.reveal').forEach(n=>n.classList.add('is-visible'));document.querySelectorAll('img').forEach(i=>i.loading='eager')});
      await pg.evaluate(async()=>{await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})))});
      const r=await pg.evaluate(({BANNED})=>{
        const vis=e=>{const s=getComputedStyle(e);return s.display!=='none'&&s.visibility!=='hidden'&&e.getClientRects().length};
        // 写真
        const photos=[];
        document.querySelectorAll('img').forEach(i=>{if(vis(i)){const m=(i.currentSrc||i.src).match(/photos\/([\w-]+\.jpg)/);if(m)photos.push(m[1])}});
        document.querySelectorAll('*').forEach(e=>{const bg=getComputedStyle(e).backgroundImage;const m=bg&&bg.match(/photos\/([\w-]+\.jpg)/);if(m&&vis(e))photos.push(m[1])});
        // コントラスト
        const lum=c=>{const v=c.match(/[\d.]+/g).map(Number);const f=x=>{x/=255;return x<=.03928?x/12.92:Math.pow((x+.055)/1.055,2.4)};return [.2126*f(v[0])+.7152*f(v[1])+.0722*f(v[2]),v[3]===undefined?1:v[3]]};
        const bgOf=e=>{for(let n=e;n;n=n.parentElement){const s=getComputedStyle(n);if(s.backgroundImage&&s.backgroundImage!=='none'&&!/gradient/.test(s.backgroundImage))return null;const c=s.backgroundColor;const a=c.match(/[\d.]+/g);if(a&&(a[3]===undefined||+a[3]>0.85))return c;if(/gradient/.test(s.backgroundImage)){const m=s.backgroundImage.match(/rgba?\([^)]*\)/);if(m)return m[0]}}return 'rgb(255,255,255)'};
        const low=[];
        document.querySelectorAll('body *').forEach(e=>{
          if(!vis(e)||e.closest('.mode-bar,.page-hero,.hero,.photo-slot,.business-image,.about-media,.work-media,.person-art,.person-photo,.lc-media,.pattern-art'))return;
          const t=[...e.childNodes].filter(n=>n.nodeType===3&&n.textContent.trim()).map(n=>n.textContent.trim()).join('');
          if(!t)return;
          const s=getComputedStyle(e);const bg=bgOf(e);if(!bg)return;
          const [l1,a1]=lum(s.color);const [l2]=lum(bg);if(a1<.5)return;
          const ratio=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);
          const big=parseFloat(s.fontSize)>=24||(parseFloat(s.fontSize)>=18.6&&+s.fontWeight>=700);
          if(ratio<(big?3:4.5))low.push(ratio.toFixed(2)+' 「'+t.slice(0,24)+'」');
        });
        // 表記
        const text=document.body.innerText;const banned=BANNED.filter(w=>text.includes(w));
        const sw=document.documentElement.scrollWidth,cw=document.documentElement.clientWidth;
        const broken=[...document.images].filter(i=>vis(i)&&i.complete&&i.naturalWidth===0).map(i=>i.src);
        const ids=new Set([...document.querySelectorAll('[id]')].map(e=>e.id));
        const badA=[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href').slice(1)).filter(h=>h&&!ids.has(h));
        return {photos,low:[...new Set(low)],banned,overflow:sw>cw,broken,badA,h1:document.querySelectorAll('h1').length};
      },{BANNED});
      if(tag==='PC')r.photos.forEach(f=>(photoUse[f]=photoUse[f]||[]).push(p));
      const pre=`[${tag}] ${p}`;
      if(r.low.length)problems.push(`${pre} コントラスト不足: ${r.low.slice(0,6).join(' / ')}`);
      if(r.banned.length)problems.push(`${pre} 表記NG: ${r.banned.join('、')}`);
      if(r.overflow)problems.push(`${pre} 横スクロールあり`);
      if(r.broken.length)problems.push(`${pre} 画像切れ: ${r.broken.join(' ')}`);
      if(r.badA.length)problems.push(`${pre} ページ内リンク切れ: ${r.badA.join(' ')}`);
      if(r.h1!==1)problems.push(`${pre} H1が${r.h1}個`);
      errs.forEach(e=>problems.push(`${pre} ${e}`));
      await pg.close();
    }
    await ctx.close();
  }
  Object.entries(photoUse).forEach(([f,ps])=>{if(ps.length>1)problems.push(`写真の使い回し: ${f} → ${ps.join(', ')}`)});
  await b.close();
  console.log(problems.length?problems.join('\n'):'OK：問題は見つかりませんでした');
  process.exit(problems.length?1:0);
})();

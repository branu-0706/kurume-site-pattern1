// 久留米興業サイト 品質チェック（公開前に必ず実行）
// 使い方: サイトのフォルダで `python3 -m http.server 8765` を起動してから `node _build/qa.js`
// 1) 写真の使い回し（サイトごと＋ページ内）  2) 文字のコントラスト  3) 出典・制作メモの表記  4) 横スクロール・画像切れ・JSエラー・ページ内リンク・H1
const {chromium}=require('playwright');
const BASE=process.env.QA_BASE||'http://localhost:8765/';
// サイト（写真の使い回しを判定する単位）ごとのページ一覧
const SITES={
  'パターン①×デザイン①':['index.html','business/index.html','recruit/index.html','work-environment/index.html','people/index.html','company/index.html'],
  'パターン②×デザイン①':['pattern2/index.html','pattern2/about/index.html','pattern2/recruit/index.html','pattern2/people/index.html','pattern2/future/index.html','pattern2/company/index.html'],
  'パターン①×デザイン②':['compare/pattern1/design-a/index.html'],
  'パターン①×デザイン③':['compare/pattern1/design-b/index.html'],
  'パターン②×デザイン②':['compare/pattern2/design-a/index.html'],
  'パターン②×デザイン③':['compare/pattern2/design-b/index.html'],
  'パターン③×デザインA':['pattern3/design-a/index.html','pattern3/design-a/business/index.html','pattern3/design-a/recruit/index.html','pattern3/design-a/work-environment/index.html','pattern3/design-a/people/index.html','pattern3/design-a/company/index.html'],
  'パターン③×デザインB':['pattern3/design-b/index.html','pattern3/design-b/business/index.html','pattern3/design-b/recruit/index.html','pattern3/design-b/work-environment/index.html','pattern3/design-b/people/index.html','pattern3/design-b/company/index.html'],
  'パターン③×デザインC':['pattern3/design-c/index.html','pattern3/design-c/business/index.html','pattern3/design-c/recruit/index.html','pattern3/design-c/work-environment/index.html','pattern3/design-c/people/index.html','pattern3/design-c/company/index.html'],
  '比較ページ':['compare/index.html'],
};
const PAGES=Object.values(SITES).flat();
const SITE_OF=Object.fromEntries(Object.entries(SITES).flatMap(([k,ps])=>ps.map(p=>[p,k])));
// 同じ元写真のトリミング違い（別ファイルでも同じ写真として扱う）
const ALIAS={'office-staff-closeup-03.jpg':'member-i.jpg','ceo.jpg':'ceo-wide.jpg','field-sidewalk2.jpg':'field-team-back.jpg','office-pc-wide.jpg':'office-pc.jpg'};
const WIDTHS=(process.env.QA_WIDTHS||'1440,1024,768,390,320').split(',').map(Number);
const fs=require('fs'),path=require('path');
const ROOT=process.env.QA_ROOT||process.cwd();
const BANNED=['求人票','出典','採用ブログより','公式サイト','掲載表記','インタビューより','ヒアリング','CAREECON求人','求人ボックス'];
(async()=>{
  const b=await chromium.launch();const problems=[];const photoUse={};
  for(const w of WIDTHS){const tag=w+'px';const deep=(w===1440||w===390);
    const ctx=await b.newContext({viewport:{width:w,height:900}});
    for(const p of PAGES){
      const pg=await ctx.newPage();const errs=[];
      pg.on('pageerror',e=>errs.push(e.message));
      pg.on('requestfailed',r=>{if(!/fonts\.(googleapis|gstatic)/.test(r.url()))errs.push('読み込み失敗 '+r.url())});
      await pg.goto(BASE+p+(process.env.QA_QUERY||''),{waitUntil:'networkidle'});
      // 公開イメージで確認（確認用の注記は対象外）
      await pg.evaluate(()=>{document.documentElement.classList.remove('mode-review');document.documentElement.classList.add('mode-public');document.querySelectorAll('.reveal').forEach(n=>n.classList.add('is-visible'));document.querySelectorAll('img').forEach(i=>i.loading='eager')});
      await pg.evaluate(async()=>{await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})))});
      const r=await pg.evaluate(({BANNED,deep})=>{
        const vis=e=>{const s=getComputedStyle(e);return s.display!=='none'&&s.visibility!=='hidden'&&e.getClientRects().length};
        // 写真
        const photos=[];
        document.querySelectorAll('img').forEach(i=>{if(vis(i)){const m=(i.currentSrc||i.src).match(/photos\/([\w-]+\.jpg)/);if(m)photos.push(m[1])}});
        document.querySelectorAll('*').forEach(e=>{const bg=getComputedStyle(e).backgroundImage;const m=bg&&bg.match(/photos\/([\w-]+\.jpg)/);if(m&&vis(e))photos.push(m[1])});
        // コントラスト
        const norm=c=>{const m=c.match(/^color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: \/ ([\d.]+))?\)/);return m?`rgba(${m[1]*255},${m[2]*255},${m[3]*255},${m[4]===undefined?1:m[4]})`:c};
        const lum=c0=>{const c=norm(c0);const v=c.match(/[\d.]+/g).map(Number);const f=x=>{x/=255;return x<=.03928?x/12.92:Math.pow((x+.055)/1.055,2.4)};return [.2126*f(v[0])+.7152*f(v[1])+.0722*f(v[2]),v[3]===undefined?1:v[3]]};
        const bgOf=e=>{for(let n=e;n;n=n.parentElement){const s=getComputedStyle(n);if(s.backgroundImage&&s.backgroundImage!=='none'&&!/gradient/.test(s.backgroundImage))return null;const c=norm(s.backgroundColor);const a=c.match(/[\d.]+/g);if(a&&(a[3]===undefined||+a[3]>0.85))return c;if(/gradient/.test(s.backgroundImage)){const m=s.backgroundImage.match(/rgba?\([^)]*\)/);if(m)return m[0]}}return 'rgb(255,255,255)'};
        const low=[];
        if(deep)document.querySelectorAll('body *').forEach(e=>{
          if(!vis(e)||e.closest('.sr-only,.kkt,.cmp-switcher,[aria-hidden="true"],.mode-bar,.page-hero,.hero,.photo-slot,.business-image,.about-media,.work-media,.person-art,.person-photo,.lc-media,.pattern-art'))return;
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
        const links=[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href')).filter(h=>!/^(https?:|mailto:|tel:|#)/.test(h));
        return {photos,low:[...new Set(low)],banned,overflow:sw>cw,broken,badA,links,h1:document.querySelectorAll('h1').length};
      },{BANNED,deep});
      if(w===1440){
        const seen={};r.photos.map(f=>ALIAS[f]||f).forEach(f=>{seen[f]=(seen[f]||0)+1;});
        Object.entries(seen).forEach(([f,n])=>{const site=SITE_OF[p];photoUse[site]=photoUse[site]||{};(photoUse[site][f]=photoUse[site][f]||new Set()).add(p);if(n>1)problems.push(`[${p}] 同じページ内で写真が重複: ${f}`);});
        // サイト内リンク：ファイルの存在とページ間アンカー
        for(const h of r.links){const [file,hash]=h.split('#');const target=path.normalize(path.join(path.dirname(p),file||path.basename(p)));
          const fp=path.join(ROOT,target);if(!fs.existsSync(fp)){problems.push(`[${p}] リンク切れ: ${h}`);continue;}
          if(hash&&target.endsWith('.html')&&!new RegExp('id="'+hash+'"').test(fs.readFileSync(fp,'utf8')))problems.push(`[${p}] アンカー切れ: ${h}`);}
      }
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
  /* ファーストビュー：CMS標準セクション（734 H1 Center／721 Mainvisual）を使い、独自HTML（方式C）にしない。CTA・リンクを置かない */
  for(const p of PAGES.filter(x=>x!=='compare/index.html'&&!x.startsWith('pattern3/'))){
    const html=fs.readFileSync(path.join(ROOT,p),'utf8');
    const secs=html.match(/<section\b[^>]*>[\s\S]*?<\/section>/g)||[];
    const fv=secs.find(s=>/<h1\b/.test(s));
    if(!fv){problems.push(`[${p}] ファーストビュー: H1のあるセクションが見つからない`);continue;}
    const open=fv.match(/<section\b[^>]*>/)[0];
    const ids=(open.match(/data-cms-id="([^"]*)"/)||[,''])[1];
    if(!/\b(734|721)\b/.test(ids))problems.push(`[${p}] ファーストビュー: CMSセクション734／721を使っていない（data-cms-id="${ids}"）`);
    if(/data-implementation="[^"]*C/.test(open))problems.push(`[${p}] ファーストビュー: 独自HTML（方式C）になっている`);
    if(/<(a|button)\b/.test(fv))problems.push(`[${p}] ファーストビュー: ボタン・リンクが入っている`);
  }
  Object.entries(photoUse).forEach(([site,m])=>Object.entries(m).forEach(([f,ps])=>{if(ps.size>1)problems.push(`写真の使い回し（${site}）: ${f} → ${[...ps].join(', ')}`)}));
  await b.close();
  console.log(problems.length?problems.join('\n'):'OK：問題は見つかりませんでした');
  process.exit(problems.length?1:0);
})();

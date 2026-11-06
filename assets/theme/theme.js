/* 配色の適用と「配色を調整」パネル（デモ専用）。
   ・既定色は assets/theme.css（config/themes.json から生成）。ここでは閲覧者がブラウザ内で試した色だけを上書きする。
   ・保存先は localStorage「kurume-demo-theme-v1」。この閲覧者のブラウザだけに反映され、他の人の表示は変わらない。
   ・適用は <html> 1要素へのCSS変数のみ。ロゴ画像・写真の色は変えない。
   ・恒久的に変えるときは「JSONを書き出す」→ config/themes.json に反映 → 再ビルド・デプロイ。
   CMS移植時はこのファイルと presets.js / theme-editor.css を読み込まない（theme.css だけを使う）。 */
(function(){
  'use strict';
  var KEY='kurume-demo-theme-v1';
  var T=window.KK_THEMES||{defaultPreset:'office-blue-gray',presets:{},notes:{}};
  var html=document.documentElement;
  var ORDER=['pageBg','primary','primaryStrong','accent','brandNavy','text','buttonPrimaryBg','buttonPrimaryText','surface','surfaceSoft','accentSoft','brandBlue','mutedText','border','buttonSecondaryBg','buttonSecondaryText','focusRing'];
  var MAIN=['pageBg','primary','primaryStrong','accent','brandNavy','text','buttonPrimaryBg'];
  var LABEL={pageBg:'背景',primary:'メイン',primaryStrong:'サブメイン',accent:'ライム（補助）',brandNavy:'ネイビー（締め色）',text:'本文',buttonPrimaryBg:'主ボタン背景',buttonPrimaryText:'主ボタン文字',surface:'紙面',surfaceSoft:'薄い区切り面',accentSoft:'ライム淡色面',brandBlue:'ロゴ由来ブルー',mutedText:'補助本文',border:'罫線',buttonSecondaryBg:'副ボタン背景',buttonSecondaryText:'副ボタン文字',focusRing:'フォーカス輪郭'};
  var kebab=function(k){return '--kk-'+k.replace(/[A-Z]/g,function(m){return '-'+m.toLowerCase();});};
  var isHex=function(v){return /^#[0-9a-fA-F]{6}$/.test(v);};

  var load=function(){try{var s=JSON.parse(localStorage.getItem(KEY)||'null');if(s&&s.version===1)return s;}catch(e){}return {version:1,preset:T.defaultPreset,scopes:{}};};
  var save=function(s){try{localStorage.setItem(KEY,JSON.stringify(s));}catch(e){}try{window.dispatchEvent(new Event('kk-theme-change'));}catch(e){}};
  var ctx=function(){return {s:html.dataset.structure||'',d:html.dataset.design||''};};
  var scopeKeys=function(){var c=ctx();var k=['all'];if(c.s)k.push('structure:'+c.s);if(c.s&&c.d)k.push('design:'+c.s+'-'+c.d);return k;};

  /* URLの ?palette=office-neutral でプリセットだけを指定できる（共有用。カスタム色はURLに載せない） */
  var urlPreset=(function(){try{var p=new URLSearchParams(location.search).get('palette');return p&&T.presets[p]?p:null;}catch(e){return null;}})();

  var resolved=function(st){
    var base=(T.presets[urlPreset||st.preset]||T.presets[T.defaultPreset]||{tokens:{}}).tokens;
    var out={};Object.keys(base).forEach(function(k){out[k]=base[k];});
    scopeKeys().forEach(function(sk){var o=st.scopes[sk];if(o)Object.keys(o).forEach(function(k){if(isHex(o[k]))out[k]=o[k];});});
    return out;
  };
  var apply=function(){
    var st=load();var tok=resolved(st);
    var custom=urlPreset||st.preset!==T.defaultPreset||Object.keys(st.scopes).some(function(k){return st.scopes[k]&&Object.keys(st.scopes[k]).length;});
    ORDER.forEach(function(k){if(custom&&tok[k])html.style.setProperty(kebab(k),tok[k]);else html.style.removeProperty(kebab(k));});
    html.toggleAttribute('data-theme-custom',!!custom);
    return tok;
  };
  apply();
  window.addEventListener('storage',function(e){if(e.key===KEY){apply();if(panel&&!panel.hidden)render();}});

  /* ---------- コントラスト ---------- */
  var lum=function(hex){var c=[1,3,5].map(function(i){var v=parseInt(hex.substr(i,2),16)/255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4);});return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2];};
  var ratio=function(a,b){if(!isHex(a)||!isHex(b))return 0;var x=lum(a),y=lum(b);return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05);};
  var PAIRS=[['text','pageBg','本文／背景',4.5],['text','surface','本文／紙面',4.5],['mutedText','surface','補助本文／紙面',4.5],['brandNavy','primary','ネイビー文字／メイン面',4.5],['brandNavy','primaryStrong','ネイビー文字／サブメイン面',4.5],['text','surfaceSoft','本文／薄い区切り面',4.5],['buttonPrimaryText','buttonPrimaryBg','主ボタン',4.5],['buttonSecondaryText','buttonSecondaryBg','副ボタン',4.5],['brandBlue','surface','ブルーの英字ラベル／紙面',4.5],['accent','surface','ライムの線／紙面（装飾）',1.5]];

  /* ---------- パネル ---------- */
  var panel=null,scopeSel='all';
  var esc=function(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});};
  var scopeLabel=function(k){var c=ctx();if(k==='all')return '全案共通';if(k.indexOf('structure:')===0)return 'この構成だけ（構成'+(c.s==='p2'?'②':'①')+'）';return 'このデザインだけ（構成'+(c.s==='p2'?'②':'①')+'×デザイン'+({d1:'①',d2:'②',d3:'③'}[c.d]||'')+'）';};

  var build=function(){
    var css=document.createElement('link');css.rel='stylesheet';css.href=new URL('theme-editor.css',SRC||location.href).href;document.head.appendChild(css);
    panel=document.createElement('div');panel.className='kkt';panel.id='kkt-panel';panel.setAttribute('role','dialog');panel.setAttribute('aria-modal','false');panel.setAttribute('aria-labelledby','kkt-title');panel.hidden=true;
    document.body.appendChild(panel);
    panel.addEventListener('input',onInput);panel.addEventListener('change',onInput);panel.addEventListener('click',onClick);
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&panel&&!panel.hidden)close();});
  };
  var SRC=document.currentScript?document.currentScript.src:'';

  var render=function(){
    var st=load();var tok=resolved(st);var ov=st.scopes[scopeSel]||{};
    var presetOpts=Object.keys(T.presets).map(function(k){return '<option value="'+k+'"'+(k===st.preset?' selected':'')+'>'+esc(T.presets[k].label||k)+'</option>';}).join('');
    var scopes=scopeKeys().map(function(k){var n=st.scopes[k]?Object.keys(st.scopes[k]).length:0;return '<option value="'+k+'"'+(k===scopeSel?' selected':'')+'>'+esc(scopeLabel(k))+(n?'（'+n+'色を変更中）':'')+'</option>';}).join('');
    var row=function(k){var v=tok[k]||'#000000';var changed=ov[k]?' is-changed':'';return '<div class="kkt-row'+changed+'"><label for="kkt-h-'+k+'">'+esc(LABEL[k]||k)+(ov[k]?'<small>変更</small>':'')+'</label><input type="color" value="'+v+'" data-k="'+k+'" aria-label="'+esc(LABEL[k])+'の色を選ぶ"><input id="kkt-h-'+k+'" class="kkt-hex" type="text" value="'+v.toUpperCase()+'" data-k="'+k+'" maxlength="7" spellcheck="false" autocomplete="off" aria-describedby="kkt-err-'+k+'"><span class="kkt-err" id="kkt-err-'+k+'" aria-live="polite"></span></div>';};
    var checks=PAIRS.map(function(p){var r=ratio(tok[p[0]],tok[p[1]]);var ok=r>=p[3];return '<li class="'+(ok?'ok':'ng')+'"><span class="kkt-swatch" style="background:'+tok[p[1]]+';color:'+tok[p[0]]+'">Aa</span><span>'+esc(p[2])+'</span><b>'+r.toFixed(1)+':1 '+(ok?'OK':(p[3]>=4.5?'要確認（4.5未満）':'要確認'))+'</b></li>';}).join('');
    var limeWarn=(ratio(tok.buttonPrimaryText,tok.buttonPrimaryBg)<4.5)?'<p class="kkt-warn" role="alert">主ボタンの文字と背景のコントラストが不足しています。ライムなど明るい背景にする場合は、主ボタン文字を濃い色（例：ネイビー）にしてください。</p>':'';
    panel.innerHTML=
      '<div class="kkt-head"><p id="kkt-title">配色を調整</p><button type="button" class="kkt-x" data-act="close" aria-label="配色パネルを閉じる">×</button></div>'+
      '<p class="kkt-note">この変更は<b>あなたのブラウザだけ</b>に保存されるプレビューです。全員の表示を変えるには、書き出したJSONを config/themes.json に反映して再デプロイします。</p>'+
      '<div class="kkt-field"><label for="kkt-preset">プリセット</label><select id="kkt-preset" data-act="preset">'+presetOpts+'</select></div>'+
      '<div class="kkt-field"><label for="kkt-scope">適用先</label><select id="kkt-scope" data-act="scope">'+scopes+'</select></div>'+
      '<fieldset class="kkt-colors"><legend>主な色</legend>'+MAIN.map(row).join('')+'</fieldset>'+
      '<details class="kkt-more"><summary>その他の色（10色）</summary>'+ORDER.filter(function(k){return MAIN.indexOf(k)<0;}).map(row).join('')+'</details>'+
      limeWarn+
      '<div class="kkt-check"><p>コントラスト検査（WCAG AA：文字4.5:1以上）</p><ul>'+checks+'</ul></div>'+
      '<div class="kkt-actions"><button type="button" data-act="reset-scope">この適用先を元に戻す</button><button type="button" data-act="reset-all">すべて初期値に戻す</button><button type="button" data-act="copy">JSONをコピー</button><button type="button" data-act="download">JSONを保存</button></div>'+
      '<details class="kkt-more"><summary>JSONを読み込む</summary><label class="sr-only" for="kkt-import">書き出したJSONを貼り付け</label><textarea id="kkt-import" rows="4" placeholder="書き出したJSONを貼り付け"></textarea><button type="button" data-act="import">読み込んで適用</button></details>'+
      '<p class="kkt-status" role="status" aria-live="polite"></p>';
  };

  var status=function(msg){var s=panel.querySelector('.kkt-status');if(s)s.textContent=msg;};
  var setColor=function(k,v){
    var st=load();st.scopes[scopeSel]=st.scopes[scopeSel]||{};st.scopes[scopeSel][k]=v.toUpperCase();save(st);apply();
    var ae=document.activeElement;var id=ae&&ae.id;var sel=ae&&ae.dataset&&ae.dataset.k&&ae.type;render();
    if(id){var el=document.getElementById(id);if(el){el.focus();if(el.setSelectionRange)el.setSelectionRange(el.value.length,el.value.length);}}
    else if(sel){var c=panel.querySelector('input[type="color"][data-k="'+ae.dataset.k+'"]');if(c)c.focus();}
  };
  var onInput=function(e){
    var t=e.target;
    if(t.dataset.act==='preset'&&e.type==='change'){var st=load();st.preset=t.value;save(st);apply();render();status('プリセットを「'+(T.presets[t.value].label||t.value)+'」にしました');document.getElementById('kkt-preset').focus();return;}
    if(t.dataset.act==='scope'&&e.type==='change'){scopeSel=t.value;render();document.getElementById('kkt-scope').focus();return;}
    if(!t.dataset.k)return;
    if(t.type==='color'){if(e.type==='input'||e.type==='change')setColor(t.dataset.k,t.value);return;}
    var v=t.value.trim();if(v&&v[0]!=='#')v='#'+v;
    var err=document.getElementById('kkt-err-'+t.dataset.k);
    if(isHex(v)){if(err)err.textContent='';t.removeAttribute('aria-invalid');if(e.type==='change'||v.length===7)setColor(t.dataset.k,v);}
    else if(e.type==='change'||v.length>=7){t.setAttribute('aria-invalid','true');if(err)err.textContent='#から始まる6桁のHEX（例 #C9DCE8）で入力してください';}
  };
  var exportJson=function(){
    var st=load();var tok=resolved(st);
    return JSON.stringify({schemaVersion:1,exportedAt:new Date().toISOString(),basePreset:st.preset,
      note:'presets.custom.tokens を config/themes.json の既定プリセットの tokens に反映し、build.py を実行してデプロイしてください。scopeOverrides は案ごとに試した上書きです。',
      presets:{custom:{label:'カスタム（'+scopeLabel(scopeSel)+'で書き出し）',tokens:tok}},scopeOverrides:st.scopes},null,2);
  };
  var onClick=function(e){
    var a=e.target.closest('[data-act]');if(!a)return;var act=a.dataset.act;var st=load();
    if(act==='close')close();
    if(act==='reset-scope'){delete st.scopes[scopeSel];save(st);apply();render();status(scopeLabel(scopeSel)+'の変更を元に戻しました');}
    if(act==='reset-all'){save({version:1,preset:T.defaultPreset,scopes:{}});apply();render();status('すべて初期値（'+(T.presets[T.defaultPreset].label||'')+'）に戻しました');}
    if(act==='copy'){var j=exportJson();var done=function(){status('JSONをコピーしました');};var fail=function(){var ta=panel.querySelector('#kkt-import');ta.value=j;ta.closest('details').open=true;ta.select();status('自動コピーできないため、下の欄を選択しました。コピーしてください');};try{navigator.clipboard.writeText(j).then(done,fail);}catch(err){fail();}}
    if(act==='download'){try{var b=new Blob([exportJson()],{type:'application/json'});var u=URL.createObjectURL(b);var l=document.createElement('a');l.href=u;l.download='kurume-theme-'+new Date().toISOString().slice(0,10)+'.json';document.body.appendChild(l);l.click();l.remove();setTimeout(function(){URL.revokeObjectURL(u);},1000);status('JSONファイルを保存しました');}catch(err){status('保存できない環境です。「JSONをコピー」をお使いください');}}
    if(act==='import'){try{var j2=JSON.parse(panel.querySelector('#kkt-import').value);var ns={version:1,preset:T.presets[j2.basePreset]?j2.basePreset:T.defaultPreset,scopes:j2.scopeOverrides||{}};if(!j2.scopeOverrides&&j2.presets&&j2.presets.custom)ns.scopes={all:j2.presets.custom.tokens};save(ns);apply();render();status('JSONを読み込んで適用しました');}catch(err){status('JSONの形式が正しくありません');}}
  };
  var opener=null;
  var open=function(from){if(!panel)build();scopeSel='all';render();panel.hidden=false;opener=from||document.activeElement;var f=panel.querySelector('#kkt-preset');if(f)f.focus();};
  var close=function(){if(!panel)return;panel.hidden=true;if(opener&&opener.focus)opener.focus();};
  window.KKTheme={open:open,close:close,apply:apply,isOpen:function(){return !!panel&&!panel.hidden;}};
})();

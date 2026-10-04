const LEARN=CONTENT.lessons,STAGES=CONTENT.questions,TAGS=CONTENT.tags,CONCEPT_MAP=CONTENT.conceptMap;
const SECN={s1:"Ⅰ · 代謝與活化能",s2:"Ⅱ · 催化與專一性",s3:"Ⅲ · 競爭抑制",s4:"Ⅳ · 溫度與pH",s5:"Ⅴ · 輔因子與統整"};
const FLIPS={},SIM_CARD=-1;let SLOTG={};
const zoomImg=(k,alt)=>`<img src="${IMG[k]}" alt="${alt}" class="zoomable">`;
const tbImg=(k,cap)=>`<details class="tbx"><summary>課本原圖：${cap}</summary>${zoomImg(k,cap)}</details>`;
const flipBox=set=>`<div class="flip" id="flip" data-set="${set}"><img id="fimg" alt="原始簡報逐步畫面"><span class="fno" id="fno"></span><div class="fcap" id="fcap"></div></div><div class="fctl"><button data-a="first" aria-label="回到第一格">⏮</button><button data-a="prev">◀ 上一步</button><button data-a="play" id="fplay">▶ 自動播放</button><button data-a="next">下一步 ▶</button><button data-a="show">⛶ 完整簡報</button></div><div class="fdots" id="fdots"></div>`;
LEARN.forEach(L=>{const f=L.figSpec;if(f.flip){FLIPS[L.id]=DECK.filter(x=>f.flip.includes(x[1]));L.fig=()=>flipBox(L.id)+(L.tb||[]).map(t=>tbImg(...t)).join('');}else if(f.pair){L.fig=()=>`<div class="fig-pair">${f.pair.map((k,i)=>zoomImg(k,L.t+'子圖'+(i+1))).join('')}</div>`+(L.tb||[]).map(t=>tbImg(...t)).join('');}else L.fig=()=>zoomImg(f.image,L.t)+(L.tb||[]).map(t=>tbImg(...t)).join('');});
STAGES.filter(s=>s.kind==='drag').forEach(s=>s.check=place=>{const bad=s.slots.filter(x=>place[x.id]?.id!==s.sol[x.id]);return{ok:!bad.length,msg:`有${bad.length}個配對需要重新比對。比對物質轉換、催化步驟與分子的作用。`,tags:[s.tag]};});

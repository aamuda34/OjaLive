path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

anchor = "function drawDetailChart(changes) {"
if content.count(anchor) != 1:
    print("ABORT: anchor found " + str(content.count(anchor)) + " times, expected 1. No changes made.")
else:
    library = """var _EARTH_PALETTE = ['#C4612A','#2D7A4F','#B8894A','#8B5CF6','#C0392B','#3B82F6','#D4A017','#7A6A55'];
function renderEarthLineChart(canvasId, prices, dates, opts){
  opts = opts || {};
  var canvas = document.getElementById(canvasId);
  if(!canvas || !prices || prices.length < 2){ if(canvas) canvas.style.display='none'; return null; }
  canvas.style.display = 'block';
  var H = opts.height || 160;
  var W = canvas.offsetWidth || 320;
  canvas.width = W; canvas.height = H;
  canvas._chartPrices = prices;
  canvas._chartDates = dates || [];
  canvas._chartIsUp = prices[prices.length-1] >= prices[0];
  canvas._chartCrosshairIdx = null;
  _drawEarthLineChart(canvas);
  _bindEarthChartDrag(canvas);
  var last=prices[prices.length-1], first=prices[0];
  if(opts.summaryEl){
    var lc = canvas._chartIsUp ? '#2D7A4F' : '#C0392B';
    var pct = ((last-first)/first*100).toFixed(1);
    document.getElementById(opts.summaryEl).innerHTML = '<span style="font-weight:800;color:'+lc+';">\u20a6'+last.toLocaleString()+'</span><span style="color:'+lc+';">'+(last>=first?'+':'')+pct+'% overall</span>';
  }
  return { last:last, first:first, high:Math.max.apply(null,prices), low:Math.min.apply(null,prices), pctChange:((last-first)/first*100) };
}
function _drawEarthLineChart(canvas){
  var prices=canvas._chartPrices, isUp=canvas._chartIsUp;
  var W=canvas.width,H=canvas.height;
  var ctx=canvas.getContext('2d');
  var lc=isUp?'#2D7A4F':'#C0392B';
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle='#FEFCF8';ctx.fillRect(0,0,W,H);
  var mn=Math.min.apply(null,prices)*0.999,mx=Math.max.apply(null,prices)*1.001;
  var pL=52,pR=10,pT=16,pB=22,rng=mx-mn||1;
  function bpx(i){return pL+(i/(prices.length-1||1))*(W-pL-pR);}
  function bpy(v){return H-pB-((v-mn)/rng)*(H-pT-pB);}
  ctx.setLineDash([2,4]);ctx.lineWidth=1;
  [0,0.5,1].forEach(function(t){
    var yy=H-pB-t*(H-pT-pB);
    ctx.strokeStyle='#E8DFD0';ctx.beginPath();ctx.moveTo(pL,yy);ctx.lineTo(W-pR,yy);ctx.stroke();
    ctx.fillStyle='#7A6A55';ctx.font='9px sans-serif';ctx.textAlign='right';
    ctx.fillText('\u20a6'+(mn+t*rng).toLocaleString('en',{maximumFractionDigits:0}),pL-3,yy+3);
  });
  ctx.setLineDash([]);
  ctx.beginPath();ctx.moveTo(bpx(0),bpy(prices[0]));
  for(var i=1;i<prices.length;i++){var cpx=(bpx(i-1)+bpx(i))/2;ctx.bezierCurveTo(cpx,bpy(prices[i-1]),cpx,bpy(prices[i]),bpx(i),bpy(prices[i]));}
  var gr=ctx.createLinearGradient(0,pT,0,H-pB);
  gr.addColorStop(0,isUp?'rgba(45,122,79,0.16)':'rgba(192,57,43,0.16)');gr.addColorStop(1,'rgba(254,252,248,0)');
  ctx.lineTo(bpx(prices.length-1),H-pB);ctx.lineTo(bpx(0),H-pB);ctx.closePath();ctx.fillStyle=gr;ctx.fill();
  ctx.beginPath();ctx.moveTo(bpx(0),bpy(prices[0]));
  for(var i=1;i<prices.length;i++){var cpx=(bpx(i-1)+bpx(i))/2;ctx.bezierCurveTo(cpx,bpy(prices[i-1]),cpx,bpy(prices[i]),bpx(i),bpy(prices[i]));}
  ctx.strokeStyle=lc;ctx.lineWidth=2;ctx.stroke();
  prices.forEach(function(p,i){ctx.beginPath();ctx.arc(bpx(i),bpy(p),i===prices.length-1?4:2.5,0,Math.PI*2);ctx.fillStyle=lc;ctx.fill();});
  ctx.save();
  ctx.beginPath();ctx.rect(0,0,W,H);ctx.clip();
  ctx.globalAlpha=0.09;ctx.fillStyle='#C4612A';ctx.font='bold 12px sans-serif';ctx.textAlign='center';
  var stepX=80, stepY=44;
  for(var yy2=-stepY; yy2<H+stepY; yy2+=stepY){
    for(var xx2=-stepX; xx2<W+stepX; xx2+=stepX){
      ctx.save();ctx.translate(xx2,yy2);ctx.rotate(-20*Math.PI/180);ctx.fillText('OjaLive',0,0);ctx.restore();
    }
  }
  ctx.restore();ctx.globalAlpha=1;
  if(canvas._chartCrosshairIdx !== null){
    var idx=Math.max(0,Math.min(prices.length-1,canvas._chartCrosshairIdx));
    var cx=bpx(idx), cy=bpy(prices[idx]);
    ctx.save();
    ctx.strokeStyle='#C4612A';ctx.setLineDash([3,3]);ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(cx,pT);ctx.lineTo(cx,H-pB);ctx.stroke();
    ctx.setLineDash([]);
    ctx.beginPath();ctx.arc(cx,cy,4,0,Math.PI*2);ctx.fillStyle=lc;ctx.fill();ctx.strokeStyle='#FEFCF8';ctx.lineWidth=2;ctx.stroke();
    var dates=canvas._chartDates||[];
    var dLabel=dates[idx]||'';
    var pLabel='\u20a6'+Math.round(prices[idx]).toLocaleString();
    ctx.font='bold 10px sans-serif';
    var tw=Math.max(ctx.measureText(pLabel).width, dLabel?ctx.measureText(dLabel).width:0)+14;
    var th=dLabel?30:18;
    var tx=Math.min(Math.max(cx-tw/2,pL),W-pR-tw);
    var ty=cy>pT+th+6?cy-th-8:cy+10;
    ctx.fillStyle='#1A1208';ctx.fillRect(tx,ty,tw,th);
    ctx.fillStyle='#fff';ctx.textAlign='center';
    ctx.fillText(pLabel,tx+tw/2,ty+13);
    if(dLabel){ctx.font='9px sans-serif';ctx.fillStyle='#C4B8A3';ctx.fillText(dLabel,tx+tw/2,ty+25);}
    ctx.restore();
  }
}
function _bindEarthChartDrag(canvas){
  if(canvas._chartDragBound) return;
  canvas._chartDragBound = true;
  var dragging=false;
  function pos(e){var t=e.touches?e.touches[0]:e;var r=canvas.getBoundingClientRect();return {x:t.clientX-r.left};}
  function idxFromX(x){
    var W=canvas.width,pL=52,pR=10;
    var ratio=(x-pL)/(W-pL-pR);
    return Math.round(ratio*((canvas._chartPrices?canvas._chartPrices.length:1)-1));
  }
  function down(e){dragging=true;canvas._chartCrosshairIdx=idxFromX(pos(e).x);_drawEarthLineChart(canvas);}
  function move(e){if(!dragging)return;if(e.cancelable)e.preventDefault();canvas._chartCrosshairIdx=idxFromX(pos(e).x);_drawEarthLineChart(canvas);}
  function up(){dragging=false;canvas._chartCrosshairIdx=null;_drawEarthLineChart(canvas);}
  canvas.style.cursor='crosshair';
  canvas.addEventListener('mousedown',down);canvas.addEventListener('mousemove',move);window.addEventListener('mouseup',up);
  canvas.addEventListener('touchstart',down,{passive:true});canvas.addEventListener('touchmove',move,{passive:false});canvas.addEventListener('touchend',up);
}
function renderEarthPieChart(canvasId, dataMap, opts){
  opts=opts||{};
  var canvas=document.getElementById(canvasId);
  var keys=Object.keys(dataMap);
  if(!canvas||!keys.length){if(canvas)canvas.style.display='none';return;}
  canvas.style.display='block';
  var H=opts.height||200;
  var W=canvas.offsetWidth||320;
  canvas.width=W;canvas.height=H;
  var ctx=canvas.getContext('2d');
  ctx.fillStyle='#FEFCF8';ctx.fillRect(0,0,W,H);
  var total=keys.reduce(function(s,k){return s+dataMap[k];},0);
  var cx=W*0.36, cy=H/2, r=Math.min(cx,cy)*0.8;
  var start=-Math.PI/2;
  keys.forEach(function(k,i){
    var slice=(dataMap[k]/total)*Math.PI*2;
    ctx.beginPath();ctx.moveTo(cx,cy);ctx.arc(cx,cy,r,start,start+slice);ctx.closePath();
    ctx.fillStyle=_EARTH_PALETTE[i%_EARTH_PALETTE.length];ctx.fill();
    ctx.strokeStyle='#FEFCF8';ctx.lineWidth=2;ctx.stroke();
    start+=slice;
  });
  ctx.beginPath();ctx.arc(cx,cy,r*0.55,0,Math.PI*2);ctx.fillStyle='#FEFCF8';ctx.fill();
  var lx=W*0.66, ly=H*0.14;
  keys.forEach(function(k,i){
    if(i>5)return;
    ctx.fillStyle=_EARTH_PALETTE[i%_EARTH_PALETTE.length];
    ctx.fillRect(lx,ly+i*24,10,10);
    ctx.fillStyle='#1A1208';ctx.font='10px sans-serif';ctx.textAlign='left';
    var short=k.length>13?k.substring(0,13)+'\u2026':k;
    ctx.fillText(short+' '+Math.round(dataMap[k]/total*100)+'%',lx+14,ly+i*24+9);
  });
  ctx.save();
  ctx.beginPath();ctx.rect(0,0,W,H);ctx.clip();
  ctx.globalAlpha=0.08;ctx.fillStyle='#C4612A';ctx.font='bold 11px sans-serif';ctx.textAlign='center';
  [[W*0.2,H*0.25],[W*0.45,H*0.75],[W*0.15,H*0.7]].forEach(function(p){ctx.save();ctx.translate(p[0],p[1]);ctx.rotate(-20*Math.PI/180);ctx.fillText('OjaLive',0,0);ctx.restore();});
  ctx.restore();ctx.globalAlpha=1;
}
"""
    content = content.replace(anchor, library + anchor, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Step 1 done: shared chart library inserted.")

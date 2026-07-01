path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old1 = """var _bdChartPrices = null, _bdChartIsUp = true, _bdWmOffset = {x:0,y:0}, _bdChartDragBound = false;
function drawBdPriceChart(){
  var canvas = document.getElementById('bd-price-chart');
  if(!canvas || !_bdChartPrices) return;
  var prices = _bdChartPrices, isUp = _bdChartIsUp;
  var W = canvas.width, H = canvas.height;
  var ctx = canvas.getContext('2d');
  var lc = isUp ? '#2D7A4F' : '#C0392B';
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle='#FEFCF8';ctx.fillRect(0,0,W,H);
  var mn=Math.min.apply(null,prices)*0.999,mx=Math.max.apply(null,prices)*1.001;
  var pL=50,pR=10,pT=15,pB=20,rng=mx-mn||1;
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
  // Tiled, draggable watermark
  ctx.save();
  ctx.beginPath();ctx.rect(0,0,W,H);ctx.clip();
  ctx.globalAlpha=0.055;ctx.fillStyle='#C4612A';ctx.font='bold 12px sans-serif';ctx.textAlign='center';
  var stepX=95, stepY=52;
  var offX=((_bdWmOffset.x%stepX)+stepX)%stepX, offY=((_bdWmOffset.y%stepY)+stepY)%stepY;
  for(var yy2=-stepY+offY; yy2<H+stepY; yy2+=stepY){
    for(var xx2=-stepX+offX; xx2<W+stepX; xx2+=stepX){
      ctx.save();ctx.translate(xx2,yy2);ctx.rotate(-20*Math.PI/180);ctx.fillText('OjaLive',0,0);ctx.restore();
    }
  }
  ctx.restore();
  ctx.globalAlpha=1;
}
function bindBdChartDrag(canvas){
  if(_bdChartDragBound) return;
  _bdChartDragBound = true;
  var dragging=false, startX=0, startY=0, startOff={x:0,y:0};
  function pos(e){ var t=e.touches?e.touches[0]:e; var r=canvas.getBoundingClientRect(); return {x:t.clientX-r.left, y:t.clientY-r.top}; }
  function down(e){ dragging=true; var p=pos(e); startX=p.x; startY=p.y; startOff={x:_bdWmOffset.x,y:_bdWmOffset.y}; canvas.style.cursor='grabbing'; }
  function move(e){ if(!dragging) return; var p=pos(e); _bdWmOffset={x:startOff.x+(p.x-startX), y:startOff.y+(p.y-startY)}; drawBdPriceChart(); }
  function up(){ dragging=false; canvas.style.cursor='grab'; }
  canvas.style.cursor='grab';
  canvas.addEventListener('mousedown',down); canvas.addEventListener('mousemove',move); window.addEventListener('mouseup',up);
  canvas.addEventListener('touchstart',down,{passive:true}); canvas.addEventListener('touchmove',move,{passive:true}); canvas.addEventListener('touchend',up);
}"""

new1 = """var _bdChartPrices = null, _bdChartIsUp = true, _bdChartDates = null, _bdCrosshairIdx = null, _bdChartDragBound = false;
function drawBdPriceChart(){
  var canvas = document.getElementById('bd-price-chart');
  if(!canvas || !_bdChartPrices) return;
  var prices = _bdChartPrices, isUp = _bdChartIsUp;
  var W = canvas.width, H = canvas.height;
  var ctx = canvas.getContext('2d');
  var lc = isUp ? '#2D7A4F' : '#C0392B';
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle='#FEFCF8';ctx.fillRect(0,0,W,H);
  var mn=Math.min.apply(null,prices)*0.999,mx=Math.max.apply(null,prices)*1.001;
  var pL=50,pR=10,pT=15,pB=20,rng=mx-mn||1;
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
  // Tiled watermark (fixed pattern, always visible, resists screenshot cropping)
  ctx.save();
  ctx.beginPath();ctx.rect(0,0,W,H);ctx.clip();
  ctx.globalAlpha=0.055;ctx.fillStyle='#C4612A';ctx.font='bold 12px sans-serif';ctx.textAlign='center';
  var stepX=95, stepY=52;
  for(var yy2=-stepY; yy2<H+stepY; yy2+=stepY){
    for(var xx2=-stepX; xx2<W+stepX; xx2+=stepX){
      ctx.save();ctx.translate(xx2,yy2);ctx.rotate(-20*Math.PI/180);ctx.fillText('OjaLive',0,0);ctx.restore();
    }
  }
  ctx.restore();
  ctx.globalAlpha=1;
  // Draggable crosshair
  if(_bdCrosshairIdx !== null){
    var idx = Math.max(0, Math.min(prices.length-1, _bdCrosshairIdx));
    var cx = bpx(idx), cy = bpy(prices[idx]);
    ctx.save();
    ctx.strokeStyle='#C4612A';ctx.setLineDash([3,3]);ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(cx,pT);ctx.lineTo(cx,H-pB);ctx.stroke();
    ctx.setLineDash([]);
    ctx.beginPath();ctx.arc(cx,cy,4,0,Math.PI*2);ctx.fillStyle=lc;ctx.fill();ctx.strokeStyle='#FEFCF8';ctx.lineWidth=2;ctx.stroke();
    var dLabel = (_bdChartDates && _bdChartDates[idx]) ? _bdChartDates[idx] : '';
    var pLabel = '\u20a6'+Math.round(prices[idx]).toLocaleString();
    ctx.font='bold 10px sans-serif';
    var tw = Math.max(ctx.measureText(pLabel).width, dLabel?ctx.measureText(dLabel).width:0) + 14;
    var th = dLabel ? 30 : 18;
    var tx = Math.min(Math.max(cx-tw/2, pL), W-pR-tw);
    var ty = cy > pT+th+6 ? cy-th-8 : cy+10;
    ctx.fillStyle='#1A1208';ctx.fillRect(tx,ty,tw,th);
    ctx.fillStyle='#fff';ctx.textAlign='center';
    ctx.fillText(pLabel, tx+tw/2, ty+13);
    if(dLabel){ctx.font='9px sans-serif';ctx.fillStyle='#C4B8A3';ctx.fillText(dLabel, tx+tw/2, ty+25);}
    ctx.restore();
  }
}
function bindBdChartDrag(canvas){
  if(_bdChartDragBound) return;
  _bdChartDragBound = true;
  var dragging=false;
  function pos(e){ var t=e.touches?e.touches[0]:e; var r=canvas.getBoundingClientRect(); return {x:t.clientX-r.left, y:t.clientY-r.top}; }
  function idxFromX(x){
    var W=canvas.width, pL=50, pR=10;
    var ratio = (x-pL)/(W-pL-pR);
    return Math.round(ratio*((_bdChartPrices?_bdChartPrices.length:1)-1));
  }
  function down(e){ dragging=true; _bdCrosshairIdx=idxFromX(pos(e).x); drawBdPriceChart(); }
  function move(e){ if(!dragging) return; if(e.cancelable) e.preventDefault(); _bdCrosshairIdx=idxFromX(pos(e).x); drawBdPriceChart(); }
  function up(){ dragging=false; _bdCrosshairIdx=null; drawBdPriceChart(); }
  canvas.style.cursor='crosshair';
  canvas.addEventListener('mousedown',down); canvas.addEventListener('mousemove',move); window.addEventListener('mouseup',up);
  canvas.addEventListener('touchstart',down,{passive:true}); canvas.addEventListener('touchmove',move,{passive:false}); canvas.addEventListener('touchend',up);
}"""

old2 = """    var prices=[Number(changes[0].old_price)].concat(changes.map(function(h){return Number(h.new_price);}));
    var canvas=document.getElementById('bd-price-chart');
    var W=canvas.offsetWidth||320,H=140;
    canvas.width=W;canvas.height=H;
    _bdChartPrices = prices;
    _bdChartIsUp = prices[prices.length-1]>=prices[0];
    drawBdPriceChart();
    bindBdChartDrag(canvas);"""

new2 = """    var prices=[Number(changes[0].old_price)].concat(changes.map(function(h){return Number(h.new_price);}));
    var dates=[null].concat(changes.map(function(h){
      if(!h.created_at) return null;
      var d=Math.floor((Date.now()-new Date(h.created_at).getTime())/86400000);
      return d===0?'today':d===1?'yesterday':d+'d ago';
    }));
    var canvas=document.getElementById('bd-price-chart');
    var W=canvas.offsetWidth||320,H=140;
    canvas.width=W;canvas.height=H;
    _bdChartPrices = prices;
    _bdChartDates = dates;
    _bdChartIsUp = prices[prices.length-1]>=prices[0];
    _bdCrosshairIdx = null;
    drawBdPriceChart();
    bindBdChartDrag(canvas);"""

count = 0
for i, (old, new) in enumerate([(old1,new1),(old2,new2)], 1):
    if old in content:
        content = content.replace(old, new, 1)
        count += 1
    else:
        print("WARNING: pattern #" + str(i) + " not found, skipped")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. " + str(count) + "/2 replacements applied.")

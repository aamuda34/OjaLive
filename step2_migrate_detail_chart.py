path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = """function drawDetailChart(changes) {
  if (!changes || !changes.length) return;
  var canvas = document.getElementById('detail-price-chart');
  canvas.style.display = 'block';
  canvas.style.borderRadius = '12px';
  var W = canvas.offsetWidth || 320;
  var H = 200;
  canvas.width = W; canvas.height = H;
  var ctx = canvas.getContext('2d');
  var prices = [Number(changes[0].old_price)].concat(changes.map(function(h){return Number(h.new_price);}));
  var times = changes.map(function(h){return timeAgo2(h.created_at);});
  function timeAgo2(ts){
    if(!ts)return '';
    var diff=Math.floor((Date.now()-new Date(ts).getTime())/1000);
    if(diff<60)return diff+'s';
    if(diff<3600)return Math.floor(diff/60)+'m';
    if(diff<86400)return Math.floor(diff/3600)+'h';
    if(diff<604800)return Math.floor(diff/86400)+'d';
    return Math.floor(diff/604800)+'w';
  }
  var isUp = prices[prices.length-1] >= prices[0];
  var lineColor = isUp ? '#0ECB81' : '#F6465D';
  var gradTop = isUp ? 'rgba(14,203,129,0.3)' : 'rgba(246,70,93,0.3)';
  var isSellerView = true;
  ctx.fillStyle = '#1E2026';
  ctx.fillRect(0,0,W,H);
  var min = Math.min.apply(null,prices)*0.999;
  var max = Math.max.apply(null,prices)*1.001;
  var padL=58,padR=12,padT=20,padB=28;
  var range = max-min||1;
  function px(i){ return padL+(i/(prices.length-1||1))*(W-padL-padR); }
  function py(v){ return H-padB-((v-min)/range)*(H-padT-padB); }
  ctx.setLineDash([2,4]);
  ctx.lineWidth=1;
  [0,0.25,0.5,0.75,1].forEach(function(t){
    var yy=H-padB-t*(H-padT-padB);
    ctx.strokeStyle='#2B2F36';
    ctx.beginPath();ctx.moveTo(padL,yy);ctx.lineTo(W-padR,yy);ctx.stroke();
    ctx.fillStyle='#848E9C';ctx.font='9px sans-serif';ctx.textAlign='right';
    ctx.fillText('\u20a6'+(min+t*range).toLocaleString('en',{maximumFractionDigits:0}),padL-4,yy+3);
  });
  ctx.setLineDash([]);
  ctx.beginPath();
  ctx.moveTo(px(0),py(prices[0]));
  for(var i=1;i<prices.length;i++){
    var cpx=(px(i-1)+px(i))/2;
    ctx.bezierCurveTo(cpx,py(prices[i-1]),cpx,py(prices[i]),px(i),py(prices[i]));
  }
  var grad=ctx.createLinearGradient(0,padT,0,H-padB);
  grad.addColorStop(0,gradTop);
  grad.addColorStop(1,'rgba(30,32,38,0)');
  ctx.lineTo(px(prices.length-1),H-padB);
  ctx.lineTo(px(0),H-padB);
  ctx.closePath();
  ctx.fillStyle=grad;ctx.fill();
  ctx.beginPath();
  ctx.moveTo(px(0),py(prices[0]));
  for(var i=1;i<prices.length;i++){
    var cpx=(px(i-1)+px(i))/2;
    ctx.bezierCurveTo(cpx,py(prices[i-1]),cpx,py(prices[i]),px(i),py(prices[i]));
  }
  ctx.strokeStyle=lineColor;ctx.lineWidth=2;ctx.stroke();
  prices.forEach(function(p,i){
    ctx.beginPath();ctx.arc(px(i),py(p),i===prices.length-1?5:3,0,Math.PI*2);
    ctx.fillStyle=lineColor;ctx.fill();
  });
  var last=prices[prices.length-1];
  var first=prices[0];
  var pctChange=((last-first)/first*100).toFixed(2);
  var pctSign=last>=first?'+':'';
  var high=Math.max.apply(null,prices);
  var low2=Math.min.apply(null,prices);
  var summary=document.getElementById('chart-summary');
  if(summary){
    summary.style.display='block';
    document.getElementById('chart-current-price').textContent='\u20a6'+last.toLocaleString();
    document.getElementById('chart-current-price').style.color=lineColor;
    var chEl=document.getElementById('chart-change');
    chEl.textContent=pctSign+pctChange+'% overall';
    chEl.style.color=lineColor;
    document.getElementById('chart-high').textContent='\u20a6'+high.toLocaleString();
    document.getElementById('chart-low').textContent='\u20a6'+low2.toLocaleString();
  }
  times.forEach(function(t,i){
    if(i===0)return;
    ctx.fillStyle='#848E9C';ctx.font='9px sans-serif';ctx.textAlign='center';
    ctx.fillText(t,px(i),H-padB+12);
  });
  canvas.ontouchstart=function(e){
    e.preventDefault();
    var rect=canvas.getBoundingClientRect();
    var touchX=e.touches[0].clientX-rect.left;
    var scaleX=W/rect.width;
    var tx=touchX*scaleX;
    var idx=Math.round((tx-padL)/(W-padL-padR)*(prices.length-1));
    idx=Math.max(0,Math.min(prices.length-1,idx));
    var tp=prices[idx];
    ctx.clearRect(0,0,W,H);
    ctx.fillStyle='#1E2026';ctx.fillRect(0,0,W,H);
    ctx.setLineDash([2,4]);ctx.lineWidth=1;
    [0,0.25,0.5,0.75,1].forEach(function(t){
      var yy=H-padB-t*(H-padT-padB);
      ctx.strokeStyle='#2B2F36';
      ctx.beginPath();ctx.moveTo(padL,yy);ctx.lineTo(W-padR,yy);ctx.stroke();
      ctx.fillStyle='#848E9C';ctx.font='9px sans-serif';ctx.textAlign='right';
      ctx.fillText('\u20a6'+(min+t*range).toLocaleString('en',{maximumFractionDigits:0}),padL-4,yy+3);
    });
    ctx.setLineDash([]);
    ctx.beginPath();ctx.moveTo(px(0),py(prices[0]));
    for(var i=1;i<prices.length;i++){var cpx=(px(i-1)+px(i))/2;ctx.bezierCurveTo(cpx,py(prices[i-1]),cpx,py(prices[i]),px(i),py(prices[i]));}
    ctx.strokeStyle=lineColor;ctx.lineWidth=2;ctx.stroke();
    ctx.setLineDash([3,3]);
    ctx.strokeStyle='#fff';ctx.lineWidth=1;ctx.globalAlpha=0.5;
    ctx.beginPath();ctx.moveTo(px(idx),padT);ctx.lineTo(px(idx),H-padB);ctx.stroke();
    ctx.beginPath();ctx.moveTo(padL,py(tp));ctx.lineTo(W-padR,py(tp));ctx.stroke();
    ctx.setLineDash([]);ctx.globalAlpha=1;
    ctx.beginPath();ctx.arc(px(idx),py(tp),5,0,Math.PI*2);
    ctx.fillStyle=lineColor;ctx.fill();
    var tooltipTime = idx===0 ? 'now' : (times[idx-1]?times[idx-1]+' ago':'now');
    var tooltipText = '\u20a6'+tp.toLocaleString();
    var tooltipW = 120;
    var tooltipH = 38;
    var tooltipX = Math.min(Math.max(px(idx)-tooltipW/2, padL), W-padR-tooltipW);
    var tooltipY = py(tp) < padT+50 ? py(tp)+12 : py(tp)-tooltipH-8;
    ctx.fillStyle='rgba(15,15,20,0.97)';
    ctx.strokeStyle=lineColor;ctx.lineWidth=1.5;
    ctx.beginPath();
    if(ctx.roundRect){ctx.roundRect(tooltipX,tooltipY,tooltipW,tooltipH,6);}
    else{ctx.rect(tooltipX,tooltipY,tooltipW,tooltipH);}
    ctx.fill();ctx.stroke();
    ctx.fillStyle='#FFFFFF';ctx.font='bold 13px sans-serif';ctx.textAlign='center';
    ctx.fillText(tooltipText,tooltipX+tooltipW/2,tooltipY+16);
    ctx.fillStyle='#E0E0E0';ctx.font='bold 11px sans-serif';
    ctx.fillText(tooltipTime,tooltipX+tooltipW/2,tooltipY+30);
    ctx.globalAlpha=0.1;ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';
    wRows.forEach(function(wy){wCols.forEach(function(wx){ctx.save();ctx.translate(wx,wy);ctx.rotate(-20*Math.PI/180);ctx.fillText('OjaLive',0,0);ctx.restore();});});
    ctx.globalAlpha=1;
  };
  ctx.globalAlpha=0.1;
  ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';
  var wRows=[H*0.25,H*0.5,H*0.75];
  var wCols=[W*0.25,W*0.5,W*0.75];
  wRows.forEach(function(wy){
    wCols.forEach(function(wx){
      ctx.save();
      ctx.translate(wx,wy);
      ctx.rotate(-20*Math.PI/180);
      ctx.fillText('OjaLive',0,0);
      ctx.restore();
    });
  });
  ctx.globalAlpha=1;
}"""

new = """function drawDetailChart(changes) {
  if (!changes || !changes.length) return;
  var prices = [Number(changes[0].old_price)].concat(changes.map(function(h){return Number(h.new_price);}));
  var dates = [null].concat(changes.map(function(h){
    if(!h.created_at) return null;
    var diff=Math.floor((Date.now()-new Date(h.created_at).getTime())/1000);
    if(diff<60)return diff+'s ago';
    if(diff<3600)return Math.floor(diff/60)+'m ago';
    if(diff<86400)return Math.floor(diff/3600)+'h ago';
    if(diff<604800)return Math.floor(diff/86400)+'d ago';
    return Math.floor(diff/604800)+'w ago';
  }));
  var stats = renderEarthLineChart('detail-price-chart', prices, dates, {height:200});
  if(!stats) return;
  var lc = stats.last >= stats.first ? '#2D7A4F' : '#C0392B';
  var summary = document.getElementById('chart-summary');
  if(summary){
    summary.style.display = 'block';
    document.getElementById('chart-current-price').textContent = '\u20a6'+stats.last.toLocaleString();
    document.getElementById('chart-current-price').style.color = lc;
    var chEl = document.getElementById('chart-change');
    chEl.textContent = (stats.pctChange>=0?'+':'')+stats.pctChange.toFixed(2)+'% overall';
    chEl.style.color = lc;
    document.getElementById('chart-high').textContent = '\u20a6'+stats.high.toLocaleString();
    document.getElementById('chart-low').textContent = '\u20a6'+stats.low.toLocaleString();
  }
}"""

if content.count(old) == 1:
    content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Step 2 done: drawDetailChart migrated.")
else:
    print("ABORT: old drawDetailChart block found " + str(content.count(old)) + " times, expected 1. No changes made.")

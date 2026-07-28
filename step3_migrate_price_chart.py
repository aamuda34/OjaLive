path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = """  if(empty2) empty2.style.display='none';
  if(canvas2) {
    canvas2.style.display='block';
    canvas2.style.borderRadius='12px';
    var prices2=[Number(changes[0].old_price)].concat(changes.map(function(h){return Number(h.new_price);}));
    var times2=changes.map(function(h){if(!h.created_at)return'';var d=Math.floor((Date.now()-new Date(h.created_at).getTime())/1000);return d<60?d+'s':d<3600?Math.floor(d/60)+'m':d<86400?Math.floor(d/3600)+'h':Math.floor(d/86400)+'d';});
    var W2=canvas2.offsetWidth||320,H2=200;
    canvas2.width=W2;canvas2.height=H2;
    var ctx2=canvas2.getContext('2d');
    var isUp2=prices2[prices2.length-1]>=prices2[0];
    var lc2=isUp2?'#0ECB81':'#F6465D';
    ctx2.fillStyle='#1E2026';ctx2.fillRect(0,0,W2,H2);
    var mn2=Math.min.apply(null,prices2)*0.999,mx2=Math.max.apply(null,prices2)*1.001;
    var pL2=55,pR2=10,pT2=20,pB2=28,rng2=mx2-mn2||1;
    function px2(i){return pL2+(i/(prices2.length-1||1))*(W2-pL2-pR2);}
    function py2(v){return H2-pB2-((v-mn2)/rng2)*(H2-pT2-pB2);}
    ctx2.setLineDash([2,4]);ctx2.lineWidth=1;
    [0,0.25,0.5,0.75,1].forEach(function(t){
      var yy=H2-pB2-t*(H2-pT2-pB2);
      ctx2.strokeStyle='#2B2F36';ctx2.beginPath();ctx2.moveTo(pL2,yy);ctx2.lineTo(W2-pR2,yy);ctx2.stroke();
      ctx2.fillStyle='#848E9C';ctx2.font='9px sans-serif';ctx2.textAlign='right';
      ctx2.fillText('\u20a6'+(mn2+t*rng2).toLocaleString('en',{maximumFractionDigits:0}),pL2-3,yy+3);
    });
    ctx2.setLineDash([]);
    ctx2.beginPath();ctx2.moveTo(px2(0),py2(prices2[0]));
    for(var i=1;i<prices2.length;i++){var cpx2=(px2(i-1)+px2(i))/2;ctx2.bezierCurveTo(cpx2,py2(prices2[i-1]),cpx2,py2(prices2[i]),px2(i),py2(prices2[i]));}
    var gr2=ctx2.createLinearGradient(0,pT2,0,H2-pB2);
    gr2.addColorStop(0,isUp2?'rgba(14,203,129,0.3)':'rgba(246,70,93,0.3)');gr2.addColorStop(1,'rgba(30,32,38,0)');
    ctx2.lineTo(px2(prices2.length-1),H2-pB2);ctx2.lineTo(px2(0),H2-pB2);ctx2.closePath();ctx2.fillStyle=gr2;ctx2.fill();
    ctx2.beginPath();ctx2.moveTo(px2(0),py2(prices2[0]));
    for(var i=1;i<prices2.length;i++){var cpx2=(px2(i-1)+px2(i))/2;ctx2.bezierCurveTo(cpx2,py2(prices2[i-1]),cpx2,py2(prices2[i]),px2(i),py2(prices2[i]));}
    ctx2.strokeStyle=lc2;ctx2.lineWidth=2;ctx2.stroke();
    prices2.forEach(function(p,i){ctx2.beginPath();ctx2.arc(px2(i),py2(p),i===prices2.length-1?5:3,0,Math.PI*2);ctx2.fillStyle=lc2;ctx2.fill();});
    var last2=prices2[prices2.length-1];
    ctx2.fillStyle=lc2;ctx2.font='bold 12px sans-serif';ctx2.textAlign='left';
    ctx2.fillText('\u20a6'+last2.toLocaleString(),pL2,pT2-4);
    var pct2=((last2-prices2[0])/prices2[0]*100).toFixed(1);
    ctx2.fillStyle=lc2;ctx2.font='11px sans-serif';
    ctx2.fillText((last2>=prices2[0]?'+':'')+pct2+'%',pL2+80,pT2-4);
    var wRows2=[H2*0.25,H2*0.5,H2*0.75];
    var wCols2=[W2*0.2,W2*0.5,W2*0.8];
    ctx2.globalAlpha=0.08;ctx2.fillStyle='#fff';ctx2.font='bold 13px sans-serif';ctx2.textAlign='center';
    wRows2.forEach(function(wy){wCols2.forEach(function(wx){ctx2.save();ctx2.translate(wx,wy);ctx2.rotate(-20*Math.PI/180);ctx2.fillText('OjaLive',0,0);ctx2.restore();});});
    ctx2.globalAlpha=1;
    canvas2.ontouchstart=function(e){
      e.preventDefault();
      var rect=canvas2.getBoundingClientRect();
      var tx=(e.touches[0].clientX-rect.left)*(W2/rect.width);
      var idx=Math.round((tx-pL2)/(W2-pL2-pR2)*(prices2.length-1));
      idx=Math.max(0,Math.min(prices2.length-1,idx));
      var tp=prices2[idx];
      ctx2.clearRect(0,0,W2,H2);
      ctx2.fillStyle='#1E2026';ctx2.fillRect(0,0,W2,H2);
      ctx2.setLineDash([2,4]);ctx2.lineWidth=1;
      [0,0.25,0.5,0.75,1].forEach(function(t){
        var yy=H2-pB2-t*(H2-pT2-pB2);
        ctx2.strokeStyle='#2B2F36';ctx2.beginPath();ctx2.moveTo(pL2,yy);ctx2.lineTo(W2-pR2,yy);ctx2.stroke();
        ctx2.fillStyle='#848E9C';ctx2.font='9px sans-serif';ctx2.textAlign='right';
        ctx2.fillText('\u20a6'+(mn2+t*rng2).toLocaleString('en',{maximumFractionDigits:0}),pL2-3,yy+3);
      });
      ctx2.setLineDash([]);
      ctx2.beginPath();ctx2.moveTo(px2(0),py2(prices2[0]));
      for(var i=1;i<prices2.length;i++){var cpx2=(px2(i-1)+px2(i))/2;ctx2.bezierCurveTo(cpx2,py2(prices2[i-1]),cpx2,py2(prices2[i]),px2(i),py2(prices2[i]));}
      ctx2.strokeStyle=lc2;ctx2.lineWidth=2;ctx2.stroke();
      ctx2.setLineDash([3,3]);ctx2.strokeStyle='rgba(255,255,255,0.5)';ctx2.lineWidth=1;
      ctx2.beginPath();ctx2.moveTo(px2(idx),pT2);ctx2.lineTo(px2(idx),H2-pB2);ctx2.stroke();
      ctx2.beginPath();ctx2.moveTo(pL2,py2(tp));ctx2.lineTo(W2-pR2,py2(tp));ctx2.stroke();
      ctx2.setLineDash([]);
      ctx2.beginPath();ctx2.arc(px2(idx),py2(tp),5,0,Math.PI*2);ctx2.fillStyle=lc2;ctx2.fill();
      var tLabel=idx===0?'start':(times2[idx-1]||'');
      var ttW=115,ttH=36;
      var ttX=Math.min(Math.max(px2(idx)-ttW/2,pL2),W2-pR2-ttW);
      var ttY=py2(tp)<pT2+50?py2(tp)+10:py2(tp)-ttH-8;
      ctx2.fillStyle='rgba(15,15,20,0.97)';ctx2.strokeStyle=lc2;ctx2.lineWidth=1.5;
      ctx2.beginPath();if(ctx2.roundRect)ctx2.roundRect(ttX,ttY,ttW,ttH,6);else ctx2.rect(ttX,ttY,ttW,ttH);
      ctx2.fill();ctx2.stroke();
      ctx2.fillStyle='#fff';ctx2.font='bold 12px sans-serif';ctx2.textAlign='center';
      ctx2.fillText('\u20a6'+tp.toLocaleString(),ttX+ttW/2,ttY+14);
      ctx2.fillStyle='#E0E0E0';ctx2.font='bold 10px sans-serif';
      ctx2.fillText(tLabel?tLabel+' ago':'now',ttX+ttW/2,ttY+28);
      wRows2.forEach(function(wy){wCols2.forEach(function(wx){ctx2.save();ctx2.globalAlpha=0.08;ctx2.fillStyle='#fff';ctx2.font='bold 13px sans-serif';ctx2.translate(wx,wy);ctx2.rotate(-20*Math.PI/180);ctx2.fillText('OjaLive',0,0);ctx2.restore();});});
    };
  }
  return;
  var canvas = document.getElementById('price-chart');"""

new = """  if(empty2) empty2.style.display='none';
  if(canvas2) {
    var prices2=[Number(changes[0].old_price)].concat(changes.map(function(h){return Number(h.new_price);}));
    var dates2=[null].concat(changes.map(function(h){
      if(!h.created_at)return null;
      var d=Math.floor((Date.now()-new Date(h.created_at).getTime())/1000);
      return d<60?d+'s ago':d<3600?Math.floor(d/60)+'m ago':d<86400?Math.floor(d/3600)+'h ago':Math.floor(d/86400)+'d ago';
    }));
    renderEarthLineChart('price-chart', prices2, dates2, {height:200});
  }
  return;
  var canvas = document.getElementById('price-chart');"""

if content.count(old) == 1:
    content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Step 3 done: renderPriceChart migrated.")
else:
    print("ABORT: old renderPriceChart block found " + str(content.count(old)) + " times, expected 1. No changes made.")

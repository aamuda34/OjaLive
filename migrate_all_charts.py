path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

reps = []

reps.append((
".range-btn{padding:4px 10px;background:#2B2F36;color:#848E9C;border:none;border-radius:6px;font-size:11px;font-weight:600;cursor:pointer;}",
".range-btn{padding:4px 10px;background:var(--border);color:var(--muted);border:none;border-radius:6px;font-size:11px;font-weight:600;cursor:pointer;}"
))

reps.append((
'''      <div id="chart-summary" style="display:none;padding:8px 0 10px;border-bottom:1px solid #2B2F36;margin-bottom:10px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
          <div>
            <div id="chart-current-price" style="font-family:'Syne',sans-serif;font-size:22px;font-weight:800;color:#0ECB81;"></div>
            <div id="chart-change" style="font-size:12px;margin-top:2px;"></div>
          </div>
          <div style="text-align:right;">
            <div style="font-size:11px;color:#848E9C;">High: <span id="chart-high" style="color:#0ECB81;font-weight:600;"></span></div>
            <div style="font-size:11px;color:#848E9C;margin-top:3px;">Low: <span id="chart-low" style="color:#F6465D;font-weight:600;"></span></div>
          </div>
        </div>''',
'''      <div id="chart-summary" style="display:none;padding:8px 0 10px;border-bottom:1px solid var(--border);margin-bottom:10px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
          <div>
            <div id="chart-current-price" style="font-family:'Syne',sans-serif;font-size:22px;font-weight:800;color:var(--earth);"></div>
            <div id="chart-change" style="font-size:12px;margin-top:2px;"></div>
          </div>
          <div style="text-align:right;">
            <div style="font-size:11px;color:var(--muted);">High: <span id="chart-high" style="color:var(--green);font-weight:600;"></span></div>
            <div style="font-size:11px;color:var(--muted);margin-top:3px;">Low: <span id="chart-low" style="color:var(--red);font-weight:600;"></span></div>
          </div>
        </div>'''
))

reps.append((
"    var color = up ? '#0ECB81' : '#F6465D';\n    var ago = timeAgo(h.created_at);",
"    var color = up ? '#2D7A4F' : '#C0392B';\n    var ago = timeAgo(h.created_at);"
))

reps.append((
'''    var extraHtml = '<div style="display:flex;gap:12px;margin-top:8px;padding-top:8px;border-top:1px solid #2B2F36;">';
    extraHtml += '<div style="flex:1;text-align:center;"><div style="font-size:10px;color:#848E9C;">AVG</div><div style="font-size:12px;font-weight:700;color:#fff;">\u20a6'+Number(avg).toLocaleString()+'</div></div>';
    extraHtml += '<div style="flex:1;text-align:center;"><div style="font-size:10px;color:#848E9C;">ALL TIME HIGH</div><div style="font-size:13px;font-weight:700;color:#0ECB81;">\u20a6'+highEver.toLocaleString()+'</div></div>';
    extraHtml += '<div style="flex:1;text-align:center;"><div style="font-size:10px;color:#848E9C;">ALL TIME LOW</div><div style="font-size:13px;font-weight:700;color:#F6465D;">\u20a6'+lowEver.toLocaleString()+'</div></div>';
    extraHtml += '<div style="flex:1;text-align:center;"><div style="font-size:10px;color:#848E9C;">CHANGES</div><div style="font-size:13px;font-weight:700;color:#fff;">'+changes.length+'x</div></div>';''',
'''    var extraHtml = '<div style="display:flex;gap:12px;margin-top:8px;padding-top:8px;border-top:1px solid var(--border);">';
    extraHtml += '<div style="flex:1;text-align:center;"><div style="font-size:10px;color:var(--muted);">AVG</div><div style="font-size:12px;font-weight:700;color:var(--dark);">\u20a6'+Number(avg).toLocaleString()+'</div></div>';
    extraHtml += '<div style="flex:1;text-align:center;"><div style="font-size:10px;color:var(--muted);">ALL TIME HIGH</div><div style="font-size:13px;font-weight:700;color:var(--green);">\u20a6'+highEver.toLocaleString()+'</div></div>';
    extraHtml += '<div style="flex:1;text-align:center;"><div style="font-size:10px;color:var(--muted);">ALL TIME LOW</div><div style="font-size:13px;font-weight:700;color:var(--red);">\u20a6'+lowEver.toLocaleString()+'</div></div>';
    extraHtml += '<div style="flex:1;text-align:center;"><div style="font-size:10px;color:var(--muted);">CHANGES</div><div style="font-size:13px;font-weight:700;color:var(--dark);">'+changes.length+'x</div></div>';'''
))

reps.append((
"    var color = up ? '#0ECB81' : '#F6465D';\n    var pct = (up?'+':'')+((h.new_price-h.old_price)/h.old_price*100).toFixed(1)+'%';",
"    var color = up ? '#2D7A4F' : '#C0392B';\n    var pct = (up?'+':'')+((h.new_price-h.old_price)/h.old_price*100).toFixed(1)+'%';"
))

reps.append((
'''  var pieCanvas = document.getElementById('stats-pie-chart');
  var pieColors = ['#C55A11','#0ECB81','#F6465D','#3B82F6','#F59E0B','#8B5CF6','#EC4899','#14B8A6'];
  if (cats.length > 0 && pieCanvas) {
    pieCanvas.style.display = 'block';
    var PW = pieCanvas.offsetWidth||320, PH = 200;
    pieCanvas.width = PW; pieCanvas.height = PH;
    var pctx = pieCanvas.getContext('2d');
    pctx.fillStyle = '#1E2026'; pctx.fillRect(0,0,PW,PH);
    var cx = PW*0.38, cy = PH/2, pr = Math.min(cx,cy)*0.85;
    var total2 = listings.length;
    var startAngle = -Math.PI/2;
    cats.forEach(function(c,i){
      var slice = (catMap[c]/total2)*Math.PI*2;
      pctx.beginPath();
      pctx.moveTo(cx,cy);
      pctx.arc(cx,cy,pr,startAngle,startAngle+slice);
      pctx.closePath();
      pctx.fillStyle = pieColors[i%pieColors.length];
      pctx.fill();
      pctx.strokeStyle = '#1E2026'; pctx.lineWidth = 2; pctx.stroke();
      startAngle += slice;
    });
    pctx.beginPath(); pctx.arc(cx,cy,pr*0.5,0,Math.PI*2);
    pctx.fillStyle='#1E2026'; pctx.fill();
    var lx = PW*0.68, ly = PH*0.15;
    cats.forEach(function(c,i){
      if(i>5)return;
      pctx.fillStyle=pieColors[i%pieColors.length];
      pctx.fillRect(lx,ly+i*26,12,12);
      pctx.fillStyle='#fff'; pctx.font='10px sans-serif'; pctx.textAlign='left';
      var short = c.length>12?c.substring(0,12)+'..':c;
      pctx.fillText(short+' '+Math.round(catMap[c]/total2*100)+'%',lx+16,ly+i*26+10);
    });
    pctx.globalAlpha=0.08; pctx.fillStyle='#fff'; pctx.font='bold 13px sans-serif'; pctx.textAlign='center';
    [[PW*0.3,PH*0.3],[PW*0.6,PH*0.6],[PW*0.15,PH*0.65]].forEach(function(pos){
      pctx.save();pctx.translate(pos[0],pos[1]);pctx.rotate(-20*Math.PI/180);pctx.fillText('OjaLive',0,0);pctx.restore();
    });
    pctx.globalAlpha=1;
  }
  document.getElementById('stats-categories').innerHTML = cats.length ? cats.map(function(c,i){
    var pct = Math.round(catMap[c]/listings.length*100);
    return '<div style="margin-bottom:8px;"><div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:3px;"><span style="display:flex;align-items:center;gap:6px;"><span style="width:10px;height:10px;border-radius:50%;background:'+pieColors[i%pieColors.length]+';display:inline-block;"></span><b>'+c+'</b></span><span>'+catMap[c]+' items ('+pct+'%)</span></div><div style="background:#f0f0f0;border-radius:6px;height:8px;"><div style="background:'+pieColors[i%pieColors.length]+';border-radius:6px;height:8px;width:'+pct+'%;"></div></div></div>';
  }).join('') : '<div class="empty">No categories yet</div>';''',
'''  var pieCanvas = document.getElementById('stats-pie-chart');
  if (cats.length > 0 && pieCanvas) {
    renderEarthPieChart('stats-pie-chart', catMap, {height:200});
  } else if (pieCanvas) {
    pieCanvas.style.display = 'none';
  }
  document.getElementById('stats-categories').innerHTML = cats.length ? cats.map(function(c,i){
    var pct = Math.round(catMap[c]/listings.length*100);
    var col = _EARTH_PALETTE[i%_EARTH_PALETTE.length];
    return '<div style="margin-bottom:8px;"><div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:3px;"><span style="display:flex;align-items:center;gap:6px;"><span style="width:10px;height:10px;border-radius:50%;background:'+col+';display:inline-block;"></span><b>'+c+'</b></span><span>'+catMap[c]+' items ('+pct+'%)</span></div><div style="background:var(--border);border-radius:6px;height:8px;"><div style="background:'+col+';border-radius:6px;height:8px;width:'+pct+'%;"></div></div></div>';
  }).join('') : '<div class="empty">No categories yet</div>';'''
))

reps.append((
'''  if (history.length > 1) {
    var canvas = document.getElementById('stats-chart');
    var prices = history.map(function(h){return Number(h.new_price);}).reverse();
    var W = canvas.offsetWidth||320; var H = 180;
    canvas.width=W; canvas.height=H;
    var ctx = canvas.getContext('2d');
    var isUp = prices[prices.length-1]>=prices[0];
    var lc = isUp?'#0ECB81':'#F6465D';
    ctx.fillStyle='#1E2026'; ctx.fillRect(0,0,W,H);
    var mn=Math.min.apply(null,prices)*0.998,mx=Math.max.apply(null,prices)*1.002;
    var pL=50,pR=10,pT=20,pB=25,rng=mx-mn||1;
    function px(i){return pL+(i/(prices.length-1||1))*(W-pL-pR);}
    function py(v){return H-pB-((v-mn)/rng)*(H-pT-pB);}
    ctx.setLineDash([2,4]); ctx.lineWidth=1;
    [0,0.5,1].forEach(function(t){
      var yy=H-pB-t*(H-pT-pB);
      ctx.strokeStyle='#2B2F36'; ctx.beginPath(); ctx.moveTo(pL,yy); ctx.lineTo(W-pR,yy); ctx.stroke();
      ctx.fillStyle='#848E9C'; ctx.font='9px sans-serif'; ctx.textAlign='right';
      ctx.fillText('\u20a6'+(mn+t*rng).toLocaleString('en',{maximumFractionDigits:0}),pL-3,yy+3);
    });
    ctx.setLineDash([]);
    ctx.beginPath(); ctx.moveTo(px(0),py(prices[0]));
    for(var i=1;i<prices.length;i++){var cpx=(px(i-1)+px(i))/2;ctx.bezierCurveTo(cpx,py(prices[i-1]),cpx,py(prices[i]),px(i),py(prices[i]));}
    var gr=ctx.createLinearGradient(0,pT,0,H-pB);
    gr.addColorStop(0,isUp?'rgba(14,203,129,0.25)':'rgba(246,70,93,0.25)'); gr.addColorStop(1,'rgba(30,32,38,0)');
    ctx.lineTo(px(prices.length-1),H-pB); ctx.lineTo(px(0),H-pB); ctx.closePath(); ctx.fillStyle=gr; ctx.fill();
    ctx.beginPath(); ctx.moveTo(px(0),py(prices[0]));
    for(var i=1;i<prices.length;i++){var cpx=(px(i-1)+px(i))/2;ctx.bezierCurveTo(cpx,py(prices[i-1]),cpx,py(prices[i]),px(i),py(prices[i]));}
    ctx.strokeStyle=lc; ctx.lineWidth=2; ctx.stroke();
    var last=prices[prices.length-1],first=prices[0];
    var pct=((last-first)/first*100).toFixed(1);
    document.getElementById('stats-chart-summary').innerHTML='<span style="font-weight:800;color:'+lc+';">\u20a6'+last.toLocaleString()+'</span><span style="color:'+lc+';">'+(last>=first?'+':'')+pct+'% overall</span>';
    var wR=[H*0.25,H*0.5,H*0.75],wC=[W*0.2,W*0.5,W*0.8];
    ctx.globalAlpha=0.08;ctx.fillStyle='#fff';ctx.font='bold 13px sans-serif';ctx.textAlign='center';
    wR.forEach(function(wy){wC.forEach(function(wx){ctx.save();ctx.translate(wx,wy);ctx.rotate(-20*Math.PI/180);ctx.fillText('OjaLive',0,0);ctx.restore();});});
    ctx.globalAlpha=1;
    var sCanvas=document.getElementById('stats-chart');
    sCanvas.ontouchstart=function(e){
      e.preventDefault();
      var rect=sCanvas.getBoundingClientRect();
      var tx=(e.touches[0].clientX-rect.left)*(W/rect.width);
      var idx=Math.round((tx-pL)/(W-pL-pR)*(prices.length-1));
      idx=Math.max(0,Math.min(prices.length-1,idx));
      var tp=prices[idx];
      ctx.clearRect(0,0,W,H);
      ctx.fillStyle='#1E2026';ctx.fillRect(0,0,W,H);
      ctx.setLineDash([2,4]);ctx.lineWidth=1;
      [0,0.5,1].forEach(function(t){
        var yy=H-pB-t*(H-pT-pB);
        ctx.strokeStyle='#2B2F36';ctx.beginPath();ctx.moveTo(pL,yy);ctx.lineTo(W-pR,yy);ctx.stroke();
        ctx.fillStyle='#848E9C';ctx.font='9px sans-serif';ctx.textAlign='right';
        ctx.fillText('\u20a6'+(mn+t*rng).toLocaleString('en',{maximumFractionDigits:0}),pL-3,yy+3);
      });
      ctx.setLineDash([]);
      ctx.beginPath();ctx.moveTo(px(0),py(prices[0]));
      for(var i=1;i<prices.length;i++){var cpx=(px(i-1)+px(i))/2;ctx.bezierCurveTo(cpx,py(prices[i-1]),cpx,py(prices[i]),px(i),py(prices[i]));}
      ctx.strokeStyle=lc;ctx.lineWidth=2;ctx.stroke();
      ctx.setLineDash([3,3]);ctx.strokeStyle='rgba(255,255,255,0.4)';ctx.lineWidth=1;
      ctx.beginPath();ctx.moveTo(px(idx),pT);ctx.lineTo(px(idx),H-pB);ctx.stroke();
      ctx.beginPath();ctx.moveTo(pL,py(tp));ctx.lineTo(W-pR,py(tp));ctx.stroke();
      ctx.setLineDash([]);
      ctx.beginPath();ctx.arc(px(idx),py(tp),5,0,Math.PI*2);ctx.fillStyle=lc;ctx.fill();
      var ttW=110,ttH=34;
      var ttX=Math.min(Math.max(px(idx)-ttW/2,pL),W-pR-ttW);
      var ttY=py(tp)<pT+50?py(tp)+10:py(tp)-ttH-8;
      ctx.fillStyle='rgba(15,15,20,0.97)';ctx.strokeStyle=lc;ctx.lineWidth=1.5;
      ctx.beginPath();if(ctx.roundRect)ctx.roundRect(ttX,ttY,ttW,ttH,6);else ctx.rect(ttX,ttY,ttW,ttH);
      ctx.fill();ctx.stroke();
      ctx.fillStyle='#fff';ctx.font='bold 12px sans-serif';ctx.textAlign='center';
      ctx.fillText('\u20a6'+tp.toLocaleString(),ttX+ttW/2,ttY+14);
      ctx.fillStyle='#E0E0E0';ctx.font='10px sans-serif';
      ctx.fillText('change #'+(idx+1),ttX+ttW/2,ttY+27);
      wR.forEach(function(wy){wC.forEach(function(wx){ctx.save();ctx.globalAlpha=0.08;ctx.fillStyle='#fff';ctx.font='bold 13px sans-serif';ctx.translate(wx,wy);ctx.rotate(-20*Math.PI/180);ctx.fillText('OjaLive',0,0);ctx.restore();});});
    };
  } else {
    var canvas2 = document.getElementById('stats-chart');
    canvas2.style.display = history.length<=1?'none':'block';
    document.getElementById('stats-chart-summary').innerHTML = '<span style="color:var(--muted);font-size:12px;">Edit item prices to see activity chart</span>';
  }
}''',
'''  if (history.length > 1) {
    var prices = history.map(function(h){return Number(h.new_price);}).reverse();
    var dates = history.slice().reverse().map(function(h){
      if(!h.created_at) return null;
      var d=Math.floor((Date.now()-new Date(h.created_at).getTime())/1000);
      return d<60?d+'s ago':d<3600?Math.floor(d/60)+'m ago':d<86400?Math.floor(d/3600)+'h ago':Math.floor(d/86400)+'d ago';
    });
    document.getElementById('stats-chart').style.display='block';
    renderEarthLineChart('stats-chart', prices, dates, {height:180, summaryEl:'stats-chart-summary'});
  } else {
    var canvas2 = document.getElementById('stats-chart');
    canvas2.style.display = history.length<=1?'none':'block';
    document.getElementById('stats-chart-summary').innerHTML = '<span style="color:var(--muted);font-size:12px;">Edit item prices to see activity chart</span>';
  }
}'''
))

reps.append((
"var chgColor=chg==='up'?'#0ECB81':chg==='down'?'#F6465D':'var(--muted)';",
"var chgColor=chg==='up'?'#2D7A4F':chg==='down'?'#C0392B':'var(--muted)';"
))

count = 0
for i, (old, new) in enumerate(reps, 1):
    if old in content:
        content = content.replace(old, new, 1)
        count += 1
    else:
        print("WARNING: pattern #" + str(i) + " not found, skipped")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. " + str(count) + "/" + str(len(reps)) + " replacements applied.")

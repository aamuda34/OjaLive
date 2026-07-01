path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
# 1. Full-bleed hero image instead of letterboxed/padded image
("""    galleryImgs.forEach(function(url){
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:20px;box-sizing:border-box;">'
        + '<img src="'+url+'" style="max-width:100%;max-height:100%;object-fit:contain;border-radius:8px;" loading="lazy" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });""",
"""    galleryImgs.forEach(function(url){
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;flex-shrink:0;position:relative;">'
        + '<img src="'+url+'" style="width:100%;height:100%;object-fit:cover;display:block;" loading="lazy" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });"""),

# 2. Chart canvas border
('<canvas id="bd-price-chart" style="width:100%;height:140px;border-radius:8px;"></canvas>',
 '<canvas id="bd-price-chart" style="width:100%;height:140px;border-radius:8px;border:1px solid var(--border);"></canvas>'),

# 3. Restyle dark price chart to match light earthy theme
("""    var canvas=document.getElementById('bd-price-chart');
    var W=canvas.offsetWidth||320,H=140;
    canvas.width=W;canvas.height=H;
    var ctx=canvas.getContext('2d');
    var isUp=prices[prices.length-1]>=prices[0];
    var lc=isUp?'#0ECB81':'#F6465D';
    ctx.fillStyle='#1E2026';ctx.fillRect(0,0,W,H);
    var mn=Math.min.apply(null,prices)*0.999,mx=Math.max.apply(null,prices)*1.001;
    var pL=50,pR=10,pT=15,pB=20,rng=mx-mn||1;
    function bpx(i){return pL+(i/(prices.length-1||1))*(W-pL-pR);}
    function bpy(v){return H-pB-((v-mn)/rng)*(H-pT-pB);}
    ctx.setLineDash([2,4]);ctx.lineWidth=1;
    [0,0.5,1].forEach(function(t){
      var yy=H-pB-t*(H-pT-pB);
      ctx.strokeStyle='#2B2F36';ctx.beginPath();ctx.moveTo(pL,yy);ctx.lineTo(W-pR,yy);ctx.stroke();
      ctx.fillStyle='#848E9C';ctx.font='9px sans-serif';ctx.textAlign='right';
      ctx.fillText('\u20a6'+(mn+t*rng).toLocaleString('en',{maximumFractionDigits:0}),pL-3,yy+3);
    });
    ctx.setLineDash([]);
    ctx.beginPath();ctx.moveTo(bpx(0),bpy(prices[0]));
    for(var i=1;i<prices.length;i++){var cpx=(bpx(i-1)+bpx(i))/2;ctx.bezierCurveTo(cpx,bpy(prices[i-1]),cpx,bpy(prices[i]),bpx(i),bpy(prices[i]));}
    var gr=ctx.createLinearGradient(0,pT,0,H-pB);
    gr.addColorStop(0,isUp?'rgba(14,203,129,0.25)':'rgba(246,70,93,0.25)');gr.addColorStop(1,'rgba(30,32,38,0)');
    ctx.lineTo(bpx(prices.length-1),H-pB);ctx.lineTo(bpx(0),H-pB);ctx.closePath();ctx.fillStyle=gr;ctx.fill();
    ctx.beginPath();ctx.moveTo(bpx(0),bpy(prices[0]));
    for(var i=1;i<prices.length;i++){var cpx=(bpx(i-1)+bpx(i))/2;ctx.bezierCurveTo(cpx,bpy(prices[i-1]),cpx,bpy(prices[i]),bpx(i),bpy(prices[i]));}
    ctx.strokeStyle=lc;ctx.lineWidth=2;ctx.stroke();
    ctx.globalAlpha=0.1;ctx.fillStyle='#fff';ctx.font='bold 13px sans-serif';ctx.textAlign='center';
    ctx.save();ctx.translate(W/2,H/2);ctx.rotate(-20*Math.PI/180);ctx.fillText('OjaLive',0,0);ctx.restore();
    ctx.globalAlpha=1;""",
"""    var canvas=document.getElementById('bd-price-chart');
    var W=canvas.offsetWidth||320,H=140;
    canvas.width=W;canvas.height=H;
    var ctx=canvas.getContext('2d');
    var isUp=prices[prices.length-1]>=prices[0];
    var lc=isUp?'#2D7A4F':'#C0392B';
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
    ctx.globalAlpha=0.06;ctx.fillStyle='#C4612A';ctx.font='bold 13px sans-serif';ctx.textAlign='center';
    ctx.save();ctx.translate(W/2,H/2);ctx.rotate(-20*Math.PI/180);ctx.fillText('OjaLive',0,0);ctx.restore();
    ctx.globalAlpha=1;"""),
]

count = 0
for i, (old, new) in enumerate(replacements, 1):
    if old in content:
        content = content.replace(old, new, 1)
        count += 1
    else:
        print("WARNING: pattern #" + str(i) + " not found, skipped")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. " + str(count) + "/" + str(len(replacements)) + " replacements applied.")

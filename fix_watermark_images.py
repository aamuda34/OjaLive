path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
("""  // Tiled watermark
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
  ctx.globalAlpha=1;""",
"""  // Tiled watermark
  ctx.save();
  ctx.beginPath();ctx.rect(0,0,W,H);ctx.clip();
  ctx.globalAlpha=0.09;ctx.fillStyle='#C4612A';ctx.font='bold 12px sans-serif';ctx.textAlign='center';
  var stepX=80, stepY=44;
  for(var yy2=-stepY; yy2<H+stepY; yy2+=stepY){
    for(var xx2=-stepX; xx2<W+stepX; xx2+=stepX){
      ctx.save();ctx.translate(xx2,yy2);ctx.rotate(-20*Math.PI/180);ctx.fillText('OjaLive',0,0);ctx.restore();
    }
  }
  ctx.restore();
  ctx.globalAlpha=1;"""),

("""  if(galleryImgs.length > 0){
    galleryImgs.forEach(function(url){
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:20px;box-sizing:border-box;">'
        + '<img src="'+url+'" style="max-width:100%;max-height:100%;object-fit:contain;border-radius:8px;" loading="lazy" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });
    if(galleryImgs.length > 1){""",
"""  if(galleryImgs.length > 0){
    galleryImgs.forEach(function(url,idx){
      var isFirst = idx===0;
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:20px;box-sizing:border-box;background:#F7F2EA;">'
        + '<img src="'+url+'" style="max-width:100%;max-height:100%;object-fit:contain;border-radius:8px;opacity:0;transition:opacity 0.25s;" '
        + (isFirst ? 'loading="eager" fetchpriority="high"' : 'loading="lazy"')
        + ' decoding="async" onload="this.style.opacity=1" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });
    if(galleryImgs.length > 1){"""),
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

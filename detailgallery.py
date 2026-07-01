f = open('index.html', 'r')
html = f.read()
f.close()
changes = 0

# 1. Increase image container height
old1 = '<div id="bd-images" style="background:#fff;height:300px;padding-top:env(safe-area-inset-top,0px);display:flex;overflow-x:auto;scrollbar-width:none;scroll-snap-type:x mandatory;border-bottom:1px solid #F0F0F0;"></div>'
new1 = '<div id="bd-images" style="background:#fff;height:360px;padding-top:env(safe-area-inset-top,0px);display:flex;overflow-x:auto;scrollbar-width:none;scroll-snap-type:x mandatory;border-bottom:1px solid #F0F0F0;position:relative;"></div>'

if old1 in html:
    html = html.replace(old1, new1)
    changes += 1
    print('1. Image height increased to 360px')
else:
    print('1. SKIP')

# 2. Add dots indicator and image counter badge when multiple images exist
old2 = """  if(galleryImgs.length > 0){
    galleryImgs.forEach(function(url){
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:20px;box-sizing:border-box;">'
        + '<img src="'+url+'" style="max-width:100%;max-height:100%;object-fit:contain;border-radius:8px;" loading="lazy" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });
  } else {
    imgEl.innerHTML='<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:64px;">🏪</div>';
  }"""

new2 = """  var oldDots = document.getElementById('bd-img-dots');
  if(oldDots) oldDots.remove();
  var oldCounter = document.getElementById('bd-img-counter');
  if(oldCounter) oldCounter.remove();
  if(galleryImgs.length > 0){
    galleryImgs.forEach(function(url){
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:20px;box-sizing:border-box;">'
        + '<img src="'+url+'" style="max-width:100%;max-height:100%;object-fit:contain;border-radius:8px;" loading="lazy" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });
    if(galleryImgs.length > 1){
      var dotsHtml = '<div id="bd-img-dots" style="position:absolute;bottom:14px;left:0;right:0;display:flex;justify-content:center;gap:5px;z-index:5;pointer-events:none;">';
      for(var di=0; di<galleryImgs.length; di++){ dotsHtml += '<div style="width:6px;height:6px;border-radius:50%;background:rgba(0,0,0,0.25);"></div>'; }
      dotsHtml += '</div>';
      imgEl.insertAdjacentHTML('afterend', dotsHtml);
      var counterHtml = '<div id="bd-img-counter" style="position:absolute;top:16px;right:16px;background:rgba(0,0,0,0.55);backdrop-filter:blur(4px);color:#fff;font-size:11px;font-weight:700;padding:4px 10px;border-radius:20px;z-index:5;">1/'+galleryImgs.length+'</div>';
      imgEl.insertAdjacentHTML('afterend', counterHtml);
      imgEl.onscroll = function(){
        var idx = Math.round(imgEl.scrollLeft / imgEl.offsetWidth);
        var cEl = document.getElementById('bd-img-counter');
        if(cEl) cEl.textContent = (idx+1)+'/'+galleryImgs.length;
      };
    }
  } else {
    imgEl.innerHTML='<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:64px;">🏪</div>';
  }"""

if old2 in html:
    html = html.replace(old2, new2)
    changes += 1
    print('2. Dots and image counter added')
else:
    print('2. SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()
print('TOTAL:', changes, '/2')

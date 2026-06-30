f = open('index.html', 'r')
html = f.read()
f.close()

old2 = """  var imgEl = document.getElementById('bd-images');
  imgEl.innerHTML = '';
  if(item.image_url){
    try{
      var imgs=JSON.parse(item.image_url);
      if(imgs.length>0){
        imgs.forEach(function(url){
          imgEl.innerHTML+='<img src="'+url+'" style="height:220px;min-width:100%;object-fit:cover;flex-shrink:0;" onclick="showFullImage(this.src)">';
        });
      } else {
        imgEl.innerHTML='<div style="width:100%;height:180px;display:flex;align-items:center;justify-content:center;font-size:60px;background:#f0ebe3;">🏪</div>';
      }
    }catch(e){imgEl.innerHTML='<div style="width:100%;height:180px;display:flex;align-items:center;justify-content:center;font-size:60px;background:#f0ebe3;">🏪</div>';}
  } else {
    imgEl.innerHTML='<div style="width:100%;height:180px;display:flex;align-items:center;justify-content:center;font-size:60px;background:#f0ebe3;">🏪</div>';
  }"""

new2 = """  var imgEl = document.getElementById('bd-images');
  imgEl.innerHTML = '';
  var galleryImgs = [];
  if(item.image_url){
    try{
      var imgs=JSON.parse(item.image_url);
      if(Array.isArray(imgs)) galleryImgs = imgs.filter(function(u){return u && typeof u==='string' && u.indexOf('http')===0;});
    }catch(e){}
  }
  if(galleryImgs.length > 0){
    galleryImgs.forEach(function(url){
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;display:flex;align-items:center;justify-content:center;flex-shrink:0;">'
        + '<img src="'+url+'" style="max-width:100%;max-height:100%;object-fit:contain;" loading="lazy" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });
  } else {
    imgEl.innerHTML='<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:64px;">🏪</div>';
  }"""

if old2 in html:
    html = html.replace(old2, new2)
    print('2. Image gallery fixed')
else:
    print('2. SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

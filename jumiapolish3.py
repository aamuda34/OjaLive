f = open('index.html', 'r')
html = f.read()
f.close()

old = """  if(galleryImgs.length > 0){
    galleryImgs.forEach(function(url){
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;display:flex;align-items:center;justify-content:center;flex-shrink:0;">'
        + '<img src="'+url+'" style="max-width:100%;max-height:100%;object-fit:contain;" loading="lazy" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });"""

new = """  if(galleryImgs.length > 0){
    galleryImgs.forEach(function(url){
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:20px;box-sizing:border-box;">'
        + '<img src="'+url+'" style="max-width:100%;max-height:100%;object-fit:contain;border-radius:8px;" loading="lazy" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });"""

if old in html:
    html = html.replace(old, new)
    print('Image padding added')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

f = open('index.html', 'r')
html = f.read()
f.close()

old = """  var inlineSellerEl = document.getElementById('bd-seller-inline-rating');
  if(inlineSellerEl){
    if(avgRating){
      inlineSellerEl.style.display='inline';
      inlineSellerEl.innerHTML = '★ '+avgRating;
    } else {
      inlineSellerEl.style.display='none';
    }
  }"""

new = """  var inlineSellerEl = document.getElementById('bd-seller-inline-rating');
  if(inlineSellerEl){
    if(avgRating){
      inlineSellerEl.style.display='inline';
      inlineSellerEl.innerHTML = '★ '+avgRating+' <span style="color:var(--muted);font-weight:500;">('+reviews.length+')</span>';
    } else {
      inlineSellerEl.style.display='none';
    }
  }"""

if old in html:
    html = html.replace(old, new)
    print('Rating count added inline')
else:
    print('ERROR: pattern not found')

f = open('index.html', 'w')
f.write(html)
f.close()

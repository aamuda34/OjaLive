f = open('index.html', 'r')
html = f.read()
f.close()

old2 = """async function loadSellerReviews(trader) {
  var result = await db.from('seller_ratings').select('*').eq('trader_name',trader).order('id',{ascending:false}).limit(10);
  var reviews = result.data||[];
  var avgRating = reviews.length ? (reviews.reduce(function(s,r){return s+r.rating;},0)/reviews.length).toFixed(1) : null;
  var avgEl = document.getElementById('bd-seller-avg-rating');
  if(avgEl) avgEl.textContent = avgRating ? '⭐ '+avgRating+' ('+reviews.length+')' : '';"""

new2 = """async function loadSellerReviews(trader) {
  var result = await db.from('seller_ratings').select('*').eq('trader_name',trader).order('id',{ascending:false}).limit(10);
  var reviews = result.data||[];
  var avgRating = reviews.length ? (reviews.reduce(function(s,r){return s+r.rating;},0)/reviews.length).toFixed(1) : null;
  var avgEl = document.getElementById('bd-seller-avg-rating');
  if(avgEl) avgEl.textContent = avgRating ? '⭐ '+avgRating+' ('+reviews.length+')' : '';
  var inlineSellerEl = document.getElementById('bd-seller-inline-rating');
  if(inlineSellerEl){
    if(avgRating){
      inlineSellerEl.style.display='inline';
      inlineSellerEl.innerHTML = '★ '+avgRating;
    } else {
      inlineSellerEl.style.display='none';
    }
  }"""

if old2 in html:
    html = html.replace(old2, new2)
    print('Seller rating populated inline')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

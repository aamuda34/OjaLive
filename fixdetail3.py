f = open('index.html', 'r')
html = f.read()
f.close()

old = """      <div id="bd-category" style="font-size:11px;color:var(--earth);font-weight:700;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:6px;"></div>
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:10px;margin-bottom:10px;">
        <div id="bd-name" style="font-family:'Syne',sans-serif;font-size:19px;font-weight:800;color:var(--dark);line-height:1.25;flex:1;"></div>
        <div id="bd-badge" style="flex-shrink:0;margin-top:2px;"></div>
      </div>"""

new = """      <div id="bd-category" style="font-size:11px;color:var(--earth);font-weight:700;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:6px;"></div>
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:10px;margin-bottom:6px;">
        <div id="bd-name" style="font-family:'Syne',sans-serif;font-size:19px;font-weight:800;color:var(--dark);line-height:1.25;flex:1;"></div>
        <div id="bd-badge" style="flex-shrink:0;margin-top:2px;"></div>
      </div>
      <div id="bd-inline-rating" style="font-size:12px;color:var(--muted);margin-bottom:10px;display:none;"></div>"""

if old in html:
    html = html.replace(old, new)
    print('1. Inline rating slot added')
else:
    print('1. SKIP')

old2 = """async function loadItemReviews(id) {
  var result = await db.from('reviews').select('*').eq('listing_id',id).order('id',{ascending:false}).limit(10);
  var reviews = result.data||[];
  var avgRating = reviews.length ? (reviews.reduce(function(s,r){return s+r.rating;},0)/reviews.length).toFixed(1) : null;
  var avgEl = document.getElementById('bd-avg-rating');
  if(avgEl) avgEl.textContent = avgRating ? '⭐ '+avgRating+' ('+reviews.length+')' : '';"""

new2 = """async function loadItemReviews(id) {
  var result = await db.from('reviews').select('*').eq('listing_id',id).order('id',{ascending:false}).limit(10);
  var reviews = result.data||[];
  var avgRating = reviews.length ? (reviews.reduce(function(s,r){return s+r.rating;},0)/reviews.length).toFixed(1) : null;
  var avgEl = document.getElementById('bd-avg-rating');
  if(avgEl) avgEl.textContent = avgRating ? '⭐ '+avgRating+' ('+reviews.length+')' : '';
  var inlineEl = document.getElementById('bd-inline-rating');
  if(inlineEl){
    if(avgRating){
      inlineEl.style.display='block';
      inlineEl.innerHTML = '<span style="color:#F59E0B;">★</span> <span style="font-weight:700;color:var(--dark);">'+avgRating+'</span> <span style="color:var(--muted);">('+reviews.length+' review'+(reviews.length!==1?'s':'')+')</span>';
    } else {
      inlineEl.style.display='none';
    }
  }"""

if old2 in html:
    html = html.replace(old2, new2)
    print('2. Inline rating populated from reviews')
else:
    print('2. SKIP')

f = open('index.html', 'w')
f.write(html)
f.close()

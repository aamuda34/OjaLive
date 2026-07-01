path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = """async function loadItemReviews(id) {
  var result = await db.from('reviews').select('*').eq('listing_id',id).order('id',{ascending:false}).limit(10);
  var reviews = result.data||[];
  var avgRating = reviews.length ? (reviews.reduce(function(s,r){return s+r.rating;},0)/reviews.length).toFixed(1) : null;
  var avgEl = document.getElementById('bd-avg-rating');
  if(avgEl) avgEl.textContent = avgRating ? '\u2b50 '+avgRating+' ('+reviews.length+')' : '';
  var inlineEl = document.getElementById('bd-inline-rating');
  if(inlineEl){
    if(avgRating){
      inlineEl.style.display='block';
      inlineEl.innerHTML = '<span style="color:#F59E0B;">\u2605</span> <span style="font-weight:700;color:var(--dark);">'+avgRating+'</span> <span style="color:var(--muted);">('+reviews.length+' review'+(reviews.length!==1?'s':'')+')</span>';
    } else {
      inlineEl.style.display='none';
    }
  }
  var listEl = document.getElementById('bd-reviews-list');
  if(!listEl) return;
  if(!reviews.length){listEl.innerHTML='<div style="font-size:13px;color:var(--muted);text-align:center;padding:10px;">No reviews yet. Be the first!</div>';return;}
  listEl.innerHTML = reviews.map(function(r){
    var stars='';for(var i=1;i<=5;i++)stars+='<span style="color:'+(i<=r.rating?'#F59E0B':'#ddd')+';">\u2605</span>';
    var ago='';if(r.created_at){var d=Math.floor((Date.now()-new Date(r.created_at).getTime())/86400000);ago=d===0?'today':d===1?'yesterday':d+'d ago';}
    return '<div style="padding:10px 0;border-bottom:1px solid var(--border);"><div style="display:flex;justify-content:space-between;align-items:center;"><div style="font-size:13px;font-weight:600;">'+r.reviewer+'</div><div style="font-size:11px;color:var(--muted);">'+ago+'</div></div><div style="font-size:14px;margin:2px 0;">'+stars+'</div>'+(r.comment?'<div style="font-size:13px;color:var(--dark);margin-top:4px;">'+r.comment+'</div>':'')+'</div>';
  }).join('');
}
async function loadSellerReviews(trader) {"""

new = """var _itemReviewsData = [];
function renderItemReviewsList(expanded){
  var listEl = document.getElementById('bd-reviews-list');
  if(!listEl) return;
  var reviews = _itemReviewsData;
  if(!reviews.length){listEl.innerHTML='<div style="font-size:13px;color:var(--muted);text-align:center;padding:10px;">No reviews yet. Be the first!</div>';return;}
  var shown = expanded ? reviews : reviews.slice(0,3);
  var html = shown.map(function(r){
    var stars='';for(var i=1;i<=5;i++)stars+='<span style="color:'+(i<=r.rating?'#F59E0B':'#ddd')+';">\u2605</span>';
    var ago='';if(r.created_at){var d=Math.floor((Date.now()-new Date(r.created_at).getTime())/86400000);ago=d===0?'today':d===1?'yesterday':d+'d ago';}
    return '<div style="padding:10px 0;border-bottom:1px solid var(--border);"><div style="display:flex;justify-content:space-between;align-items:center;"><div style="font-size:13px;font-weight:600;">'+r.reviewer+'</div><div style="font-size:11px;color:var(--muted);">'+ago+'</div></div><div style="font-size:14px;margin:2px 0;">'+stars+'</div>'+(r.comment?'<div style="font-size:13px;color:var(--dark);margin-top:4px;">'+r.comment+'</div>':'')+'</div>';
  }).join('');
  if(reviews.length > 3){
    html += '<div onclick="renderItemReviewsList('+(!expanded)+')" style="text-align:center;padding:10px 0 2px;font-size:12px;font-weight:700;color:var(--earth);cursor:pointer;">'+(expanded?'Show less':'Show all '+reviews.length+' reviews')+'</div>';
  }
  listEl.innerHTML = html;
}
async function loadItemReviews(id) {
  var result = await db.from('reviews').select('*').eq('listing_id',id).order('id',{ascending:false}).limit(10);
  var reviews = result.data||[];
  _itemReviewsData = reviews;
  var avgRating = reviews.length ? (reviews.reduce(function(s,r){return s+r.rating;},0)/reviews.length).toFixed(1) : null;
  var avgEl = document.getElementById('bd-avg-rating');
  if(avgEl) avgEl.innerHTML = avgRating ? '<span style="color:#F59E0B;">\u2605</span> '+avgRating+' ('+reviews.length+')' : '';
  var inlineEl = document.getElementById('bd-inline-rating');
  if(inlineEl){
    if(avgRating){
      inlineEl.style.display='block';
      inlineEl.innerHTML = '<span style="color:#F59E0B;">\u2605</span> <span style="font-weight:700;color:var(--dark);">'+avgRating+'</span> <span style="color:var(--muted);">('+reviews.length+' review'+(reviews.length!==1?'s':'')+')</span>';
    } else {
      inlineEl.style.display='none';
    }
  }
  renderItemReviewsList(false);
}
async function loadSellerReviews(trader) {"""

if old in content:
    content = content.replace(old, new, 1)
    print("Done. Reviews section collapsed to 3-preview with toggle.")
else:
    print("WARNING: pattern not found — file may already differ from expected.")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

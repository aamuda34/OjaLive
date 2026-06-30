f = open('index.html', 'r')
html = f.read()
f.close()

# 1. Fix image rendering — fixed height, handle broken/multiple images safely
old_img = """    var imgHtml = '';
    if(item.image_url){try{var imgs=JSON.parse(item.image_url);if(imgs[0])imgHtml='<img src="'+imgs[0]+'" style="width:100%;height:140px;object-fit:cover;" loading="lazy">';}catch(e){}}
    if(!imgHtml){
      var catEmoji={'Foodstuff':'🌾','Building Materials':'🏗️','Hardware':'🔧','Electronics':'📱','Phones & Accessories':'📲','Roofing Supplies':'🏠','Timber & Plywood':'🪵','Fabric & Clothing':'👗','Beverages':'🥤','Cosmetics & Beauty':'💄','Furniture':'🛋️','Automobile Parts':'🚗','Agricultural Produce':'🌱','Livestock & Poultry':'🐓'};
      var emoji = catEmoji[item.category]||'🏪';
      imgHtml='<div style="width:100%;height:150px;display:flex;align-items:center;justify-content:center;font-size:52px;background:linear-gradient(135deg,#F0EAE0,#E5D9C8);">'+emoji+'</div>';
    }"""

new_img = """    var imgHtml = '';
    var IMG_H = 130;
    if(item.image_url){
      try{
        var imgs=JSON.parse(item.image_url);
        if(Array.isArray(imgs) && imgs[0] && typeof imgs[0]==='string' && imgs[0].indexOf('http')===0){
          imgHtml='<img src="'+imgs[0]+'" style="width:100%;height:'+IMG_H+'px;object-fit:cover;display:block;" loading="lazy" onerror="this.parentElement.innerHTML=\\'<div style=&quot;width:100%;height:'+IMG_H+'px;display:flex;align-items:center;justify-content:center;font-size:44px;background:linear-gradient(135deg,#F0EAE0,#E5D9C8);&quot;>🏪</div>\\'">';
        }
      }catch(e){}
    }
    if(!imgHtml){
      var catEmoji={'Foodstuff':'🌾','Building Materials':'🏗️','Hardware':'🔧','Electronics':'📱','Phones & Accessories':'📲','Roofing Supplies':'🏠','Timber & Plywood':'🪵','Fabric & Clothing':'👗','Beverages':'🥤','Cosmetics & Beauty':'💄','Furniture':'🛋️','Automobile Parts':'🚗','Agricultural Produce':'🌱','Livestock & Poultry':'🐓'};
      var emoji = catEmoji[item.category]||'🏪';
      imgHtml='<div style="width:100%;height:'+IMG_H+'px;display:flex;align-items:center;justify-content:center;font-size:44px;background:linear-gradient(135deg,#F0EAE0,#E5D9C8);">'+emoji+'</div>';
    }"""

if old_img in html:
    html = html.replace(old_img, new_img)
    print('1. Image rendering fixed')
else:
    print('1. SKIP - image code not found')

# 2. Add trader name back + fix card layout with consistent structure
old_card = """    listingMap[item.id] = item;
    var likeCount = item.likes||0;
    var chgBadge = (chg==='up'||chg==='down') ? '<div style="position:absolute;top:8px;right:8px;background:'+(chg==='up'?'#0ECB81':'#F6465D')+';color:#fff;font-size:9px;font-weight:800;padding:3px 8px;border-radius:6px;">'+chgArrow+' '+chgLabel+'</div>' : '';
    var stockBadge = item.stock ? '<div style="position:absolute;top:8px;left:8px;background:#0ECB81;color:#fff;font-size:9px;font-weight:700;padding:3px 8px;border-radius:6px;">'+item.stock+' left</div>' : '';
    var unitClean = (item.unit||'').toLowerCase().startsWith('per ') ? item.unit.slice(4) : item.unit;
    var distText = (buyerLat && buyerLng && item.latitude && item.longitude) ? getDistance(buyerLat,buyerLng,item.latitude,item.longitude)+' km away' : item.location;
    return '<div onclick="openBuyerDetail('+item.id+')" style="background:#fff;border:1px solid #EBEBEB;border-radius:8px;overflow:hidden;cursor:pointer;">'
      +'<div style="position:relative;background:#F5F5F5;">'
      +imgHtml
      +chgBadge
      +stockBadge
      +'</div>'
      +'<div style="padding:8px 10px 12px;">'
      +'<div style="font-size:12px;color:#333;line-height:1.4;margin-bottom:6px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;">'+item.name+'</div>'
      +'<div style="font-family:Syne,sans-serif;font-size:17px;font-weight:800;color:#C4612A;">₦'+Number(item.price).toLocaleString()+'</div>'
      +'<div style="font-size:10px;color:#999;margin-bottom:6px;">per '+unitClean+'</div>'
      +'<div style="font-size:10px;color:#888;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">📍 '+distText+'</div>'
      +'</div>'
      +'</div>';"""

new_card = """    listingMap[item.id] = item;
    var likeCount = item.likes||0;
    var chgBadge = (chg==='up'||chg==='down') ? '<div style="position:absolute;top:8px;right:8px;background:'+(chg==='up'?'#0ECB81':'#F6465D')+';color:#fff;font-size:9px;font-weight:800;padding:3px 8px;border-radius:6px;">'+chgArrow+' '+chgLabel+'</div>' : '';
    var stockBadge = item.stock ? '<div style="position:absolute;top:8px;left:8px;background:#0ECB81;color:#fff;font-size:9px;font-weight:700;padding:3px 8px;border-radius:6px;">'+item.stock+' left</div>' : '';
    var unitClean = (item.unit||'').toLowerCase().startsWith('per ') ? item.unit.slice(4) : item.unit;
    var hasGPS = buyerLat && buyerLng && item.latitude && item.longitude;
    var distText = hasGPS ? getDistance(buyerLat,buyerLng,item.latitude,item.longitude)+' km away' : item.location;
    var distColor = hasGPS ? '#2D7A4F' : '#888';
    return '<div onclick="openBuyerDetail('+item.id+')" style="background:#fff;border:1px solid #EBEBEB;border-radius:10px;overflow:hidden;cursor:pointer;display:flex;flex-direction:column;height:100%;">'
      +'<div style="position:relative;background:#F5F5F5;flex-shrink:0;">'
      +imgHtml
      +chgBadge
      +stockBadge
      +'</div>'
      +'<div style="padding:9px 10px 11px;display:flex;flex-direction:column;flex:1;">'
      +'<div style="font-size:12px;color:#222;line-height:1.35;margin-bottom:3px;font-weight:500;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;min-height:32px;">'+item.name+'</div>'
      +'<div style="font-size:10px;color:#C4612A;font-weight:600;margin-bottom:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">🏪 '+item.trader+'</div>'
      +'<div style="margin-top:auto;">'
      +'<div style="font-family:Syne,sans-serif;font-size:17px;font-weight:800;color:#1A1208;">₦'+Number(item.price).toLocaleString()+'</div>'
      +'<div style="font-size:10px;color:#999;margin-bottom:5px;">per '+unitClean+'</div>'
      +'<div style="font-size:10px;color:'+distColor+';font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">📍 '+distText+'</div>'
      +'</div>'
      +'</div>'
      +'</div>';"""

if old_card in html:
    html = html.replace(old_card, new_card)
    print('2. Card layout upgraded with trader name')
else:
    print('2. SKIP - card code not found')

# 3. Make grid items equal height
old_grid = """document.getElementById('board').innerHTML = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding-bottom:20px;">'+html+'</div>';"""
new_grid = """document.getElementById('board').innerHTML = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding-bottom:20px;align-items:stretch;">'+html+'</div>';"""

if old_grid in html:
    html = html.replace(old_grid, new_grid)
    print('3. Grid alignment fixed')
else:
    print('3. SKIP - grid code not found')

# 4. Fix "Getting location..." stuck label with timeout fallback
old_loc = """function requestBuyerLocation() {
  var lbl = document.getElementById('loc-label');
  if (!lbl) return;
  if (!navigator.geolocation) { lbl.textContent = 'GPS not available'; return; }
  lbl.textContent = 'Getting location...';
  navigator.geolocation.getCurrentPosition(
    function(pos) {
      buyerLat = pos.coords.latitude;
      buyerLng = pos.coords.longitude;
      lbl.textContent = '✅ Location found';
      document.getElementById('filter-sort').value = 'nearest';
      renderBoard();
    },
    function(err) {
      lbl.textContent = 'Tap to use location';
    },
    { enableHighAccuracy: true, timeout: 10000, maximumAge: 30000 }
  );
}"""

new_loc = """function requestBuyerLocation() {
  var lbl = document.getElementById('loc-label');
  if (!lbl) return;
  if (!navigator.geolocation) { lbl.textContent = 'GPS not available on this device'; return; }
  lbl.textContent = 'Getting location...';
  var timedOut = false;
  var safetyTimer = setTimeout(function() {
    timedOut = true;
    lbl.textContent = 'Tap to use location';
  }, 11000);
  navigator.geolocation.getCurrentPosition(
    function(pos) {
      if (timedOut) return;
      clearTimeout(safetyTimer);
      buyerLat = pos.coords.latitude;
      buyerLng = pos.coords.longitude;
      lbl.textContent = '✅ Location found';
      document.getElementById('filter-sort').value = 'nearest';
      renderBoard();
    },
    function(err) {
      clearTimeout(safetyTimer);
      lbl.textContent = 'Tap to use location';
    },
    { enableHighAccuracy: true, timeout: 10000, maximumAge: 30000 }
  );
}"""

if old_loc in html:
    html = html.replace(old_loc, new_loc)
    print('4. Location label fixed with safety timeout')
else:
    print('4. SKIP - location code not found')

f = open('index.html', 'w')
f.write(html)
f.close()
print('ALL DONE')

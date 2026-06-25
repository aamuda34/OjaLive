f = open('index.html', 'r')
html = f.read()
f.close()

# 1. Add distance calculation function and buyer location to loadListings
old_load = '''var allListings = [];
async function loadListings() {
  try {
    var result = await db.from('Listing').select('*').eq('verified', true);
    if (result.error) { showToast('Error: '+result.error.message); return; }
    allListings = result.data || [];
    document.getElementById('filter-city').addEventListener('change', renderBoard);
    document.getElementById('filter-category').addEventListener('change', renderBoard);
    renderBoard();
  } catch(e) {
    showToast('Fatal error: '+e.message);
  }
}'''

new_load = '''var allListings = [];
var buyerLat = null;
var buyerLng = null;

function getDistance(lat1, lng1, lat2, lng2) {
  var R = 6371;
  var dLat = (lat2-lat1) * Math.PI/180;
  var dLng = (lng2-lng1) * Math.PI/180;
  var a = Math.sin(dLat/2)*Math.sin(dLat/2) + Math.cos(lat1*Math.PI/180)*Math.cos(lat2*Math.PI/180)*Math.sin(dLng/2)*Math.sin(dLng/2);
  var c = 2*Math.atan2(Math.sqrt(a),Math.sqrt(1-a));
  return Math.round(R*c);
}

async function loadListings() {
  try {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(pos) {
        buyerLat = pos.coords.latitude;
        buyerLng = pos.coords.longitude;
        renderBoard();
      });
    }
    var result = await db.from('Listing').select('*').eq('verified', true);
    if (result.error) { showToast('Error: '+result.error.message); return; }
    allListings = result.data || [];
    document.getElementById('filter-city').addEventListener('change', renderBoard);
    document.getElementById('filter-category').addEventListener('change', renderBoard);
    renderBoard();
  } catch(e) {
    showToast('Fatal error: '+e.message);
  }
}'''

html = html.replace(old_load, new_load)

# 2. Update renderBoard to show distance and sort by proximity
old_render = '''function renderBoard() {
  var city = document.getElementById('filter-city').value;
  var cat = document.getElementById('filter-category').value;
  var data = allListings.filter(function(item) {
    var cm = !city || (item.location||'').toLowerCase().includes(city.toLowerCase());
    var km = !cat || item.category === cat;
    return cm && km;
  });
  document.getElementById('count').textContent = data.length + ' Listings';
  if (!data.length) { document.getElementById('board').innerHTML = '<div class="empty">No listings found</div>'; return; }
  document.getElementById('board').innerHTML = data.map(function(item) {
    return '<div class="price-item"><div><div class="mname">'+item.name+'</div><div class="munit">'+item.unit+' · <span class="vdot"></span>'+item.trader+' · '+item.location+'</div></div><div class="pright"><div class="pval">&#8358;'+Number(item.price).toLocaleString()+'</div><span class="pbadge stable">Stable</span></div></div>';
  }).join('');
}'''

new_render = '''function renderBoard() {
  var city = document.getElementById('filter-city').value;
  var cat = document.getElementById('filter-category').value;
  var data = allListings.filter(function(item) {
    var cm = !city || (item.location||'').toLowerCase().includes(city.toLowerCase());
    var km = !cat || item.category === cat;
    return cm && km;
  });
  if (buyerLat && buyerLng) {
    data.sort(function(a,b) {
      var da = (a.latitude && a.longitude) ? getDistance(buyerLat,buyerLng,a.latitude,a.longitude) : 99999;
      var db2 = (b.latitude && b.longitude) ? getDistance(buyerLat,buyerLng,b.latitude,b.longitude) : 99999;
      return da - db2;
    });
  }
  document.getElementById('count').textContent = data.length + ' Listings';
  if (!data.length) { document.getElementById('board').innerHTML = '<div class="empty">No listings found</div>'; return; }
  document.getElementById('board').innerHTML = data.map(function(item) {
    var distBadge = '';
    if (buyerLat && buyerLng && item.latitude && item.longitude) {
      var d = getDistance(buyerLat,buyerLng,item.latitude,item.longitude);
      distBadge = '<span style="font-size:10px;color:var(--green);font-weight:600;margin-left:4px;">📍 '+d+' km away</span>';
    }
    return '<div class="price-item"><div><div class="mname">'+item.name+'</div><div class="munit">'+item.unit+' · <span class="vdot"></span>'+item.trader+' · '+item.location+distBadge+'</div></div><div class="pright"><div class="pval">&#8358;'+Number(item.price).toLocaleString()+'</div><span class="pbadge stable">Stable</span></div></div>';
  }).join('');
}'''

html = html.replace(old_render, new_render)

# 3. Update sellerSaveNewListing to capture GPS
old_save = '''async function sellerSaveNewListing() {
  var name = document.getElementById('add-item-name').value.trim();
  var price = parseFloat(document.getElementById('add-item-price').value);
  var unit = document.getElementById('add-item-unit').value.trim();
  var category = document.getElementById('add-item-category').value;
  var city = document.getElementById('add-item-city').value.trim();
  var address = document.getElementById('add-item-location').value.trim();
  if (!name||!price||!unit||!city) { showToast('Fill all required fields'); return; }
  var location = address ? address+', '+city : city;
  var result = await db.from('Listing').insert([{name:name,price:price,unit:unit,category:category,location:location,trader:currentSeller.full_name,verified:true,change:'stable'}]);
  if (result.error) { showToast('Error: '+result.error.message); return; }
  showToast('Item posted!');
  loadSellerDashboard();
  loadListings();
  sellerShowScreen('seller-dashboard');
}'''

new_save = '''async function sellerSaveNewListing() {
  var name = document.getElementById('add-item-name').value.trim();
  var price = parseFloat(document.getElementById('add-item-price').value);
  var unit = document.getElementById('add-item-unit').value.trim();
  var category = document.getElementById('add-item-category').value;
  var city = document.getElementById('add-item-city').value.trim();
  var address = document.getElementById('add-item-location').value.trim();
  if (!name||!price||!unit||!city) { showToast('Fill all required fields'); return; }
  var location = address ? address+', '+city : city;
  var lat = null; var lng = null;
  if (navigator.geolocation) {
    try {
      var pos = await new Promise(function(res,rej){ navigator.geolocation.getCurrentPosition(res,rej,{timeout:5000}); });
      lat = pos.coords.latitude;
      lng = pos.coords.longitude;
    } catch(e) {}
  }
  var result = await db.from('Listing').insert([{name:name,price:price,unit:unit,category:category,location:location,trader:currentSeller.full_name,verified:true,change:'stable',latitude:lat,longitude:lng}]);
  if (result.error) { showToast('Error: '+result.error.message); return; }
  showToast('Item posted!');
  loadSellerDashboard();
  loadListings();
  sellerShowScreen('seller-dashboard');
}'''

html = html.replace(old_save, new_save)

f = open('index.html', 'w')
f.write(html)
f.close()

print('Done! Distance feature added successfully.')

import re

f = open('index.html', 'r')
html = f.read()
f.close()

# 1. Replace registration location with structured dropdowns
html = html.replace(
'        <label>Market Location</label>\n        <input type="text" id="reg-location" placeholder="e.g. Shop 12, Oja Oba, Iwo">',
'        <label>Country</label>\n        <select id="reg-country"><option value="Nigeria">Nigeria</option><option value="Ghana">Ghana</option></select>\n        <label>State</label>\n        <select id="reg-state"><option value="Osun">Osun</option><option value="Lagos">Lagos</option><option value="Oyo">Oyo</option><option value="Kano">Kano</option></select>\n        <label>City / Market</label>\n        <input type="text" id="reg-location" placeholder="e.g. Iwo, Osogbo">'
)

# 2. Add filter bar to buy tab
html = html.replace(
'    <div id="board"><div class="empty">Loading prices...</div></div>',
'    <div style="display:flex;gap:8px;margin-bottom:12px;"><select id="filter-city" style="flex:1;padding:10px 12px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;background:#fff;"><option value="">All Cities</option><option value="Iwo">Iwo</option><option value="Osogbo">Osogbo</option><option value="Ile-Ife">Ile-Ife</option><option value="Lagos">Lagos</option><option value="Ibadan">Ibadan</option></select><select id="filter-category" style="flex:1;padding:10px 12px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;background:#fff;"><option value="">All Categories</option><option value="Building Materials">Building</option><option value="Foodstuff">Foodstuff</option><option value="Hardware">Hardware</option><option value="Roofing Supplies">Roofing</option><option value="Electronics">Electronics</option></select></div>\n    <div id="board"><div class="empty">Loading prices...</div></div>'
)

# 3. Update loadListings to support filtering
old_load = '''async function loadListings() {
  try {
    var result = await db.from('Listing').select('*').eq('verified', true);
    if (result.error) { showToast('Error: '+result.error.message); return; }
    var data = result.data || [];
    document.getElementById('count').textContent = data.length + ' Listings';
    if (!data.length) { document.getElementById('board').innerHTML = '<div class="empty">No listings</div>'; return; }
    document.getElementById('board').innerHTML = data.map(function(item) {
      return '<div class="price-item"><div><div class="mname">'+item.name+'</div><div class="munit">'+item.unit+' · <span class="vdot"></span>'+item.trader+' · '+item.location+'</div></div><div class="pright"><div class="pval">₦'+Number(item.price).toLocaleString()+'</div><span class="pbadge stable">Stable</span></div></div>';
    }).join('');
  } catch(e) {
    showToast('Fatal error: '+e.message);
  }
}'''

new_load = '''var allListings = [];
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
}
function renderBoard() {
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

html = html.replace(old_load, new_load)

# 4. Update sellerRegister to save country and state
html = html.replace(
"  var location = document.getElementById('reg-location').value.trim();\n  var trade = document.getElementById('reg-trade').value;\n  var password = document.getElementById('reg-password').value.trim();\n  if (!name||!phone||!location||!password) { showToast('Fill all fields'); return; }\n  if (password.length < 6) { showToast('Password must be 6+ characters'); return; }\n  var result = await db.from('traders').insert([{full_name:name,phone:phone,location:location,trade:trade,password:password,status:'approved'}]);",
"  var country = document.getElementById('reg-country').value;\n  var state = document.getElementById('reg-state').value;\n  var location = document.getElementById('reg-location').value.trim();\n  var trade = document.getElementById('reg-trade').value;\n  var password = document.getElementById('reg-password').value.trim();\n  if (!name||!phone||!location||!password) { showToast('Fill all fields'); return; }\n  if (password.length < 6) { showToast('Password must be 6+ characters'); return; }\n  var fullLocation = location+', '+state+', '+country;\n  var result = await db.from('traders').insert([{full_name:name,phone:phone,location:fullLocation,trade:trade,password:password,status:'approved'}]);"
)

f = open('index.html', 'w')
f.write(html)
f.close()

print('Done! All changes applied successfully.')

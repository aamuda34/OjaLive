f = open('index.html', 'r')
html = f.read()
f.close()
changes = 0

old1 = '''.cat-pill{padding:6px 14px;background:var(--card);color:var(--muted);border:1.5px solid var(--border);border-radius:20px;font-size:12px;font-weight:600;cursor:pointer;white-space:nowrap;flex-shrink:0;}
.cat-pill.active-pill{background:var(--earth);color:#fff;border-color:var(--earth);}'''
new1 = '''.cat-pill{padding:8px 14px;background:transparent;color:var(--muted);border:none;border-bottom:2px solid transparent;font-size:12px;font-weight:600;cursor:pointer;white-space:nowrap;flex-shrink:0;letter-spacing:0.2px;}
.cat-pill.active-pill{color:var(--earth);border-bottom:2px solid var(--earth);}'''
if old1 in html:
    html = html.replace(old1, new1); changes += 1; print('1. Tab style done')
else: print('1. SKIP')

old2 = '''  <div style="display:flex;gap:8px;overflow-x:auto;padding:10px 14px;scrollbar-width:none;background:#fff;border-bottom:1px solid var(--border);-webkit-overflow-scrolling:touch;">
    <button class="cat-pill active-pill" onclick="filterCat(this,'')">All</button>
    <button class="cat-pill" onclick="filterCat(this,'Foodstuff')">🌾 Food</button>
    <button class="cat-pill" onclick="filterCat(this,'Building Materials')">🏗️ Building</button>
    <button class="cat-pill" onclick="filterCat(this,'Hardware')">🔧 Hardware</button>
    <button class="cat-pill" onclick="filterCat(this,'Electronics')">📱 Electronics</button>
    <button class="cat-pill" onclick="filterCat(this,'Phones & Accessories')">📲 Phones</button>
    <button class="cat-pill" onclick="filterCat(this,'Roofing Supplies')">🏠 Roofing</button>
    <button class="cat-pill" onclick="filterCat(this,'Timber & Plywood')">🪵 Timber</button>
    <button class="cat-pill" onclick="filterCat(this,'Fabric & Clothing')">👗 Fashion</button>
    <button class="cat-pill" onclick="filterCat(this,'Beverages')">🥤 Drinks</button>
    <button class="cat-pill" onclick="filterCat(this,'Cosmetics & Beauty')">💄 Beauty</button>
    <button class="cat-pill" onclick="filterCat(this,'Furniture')">🛋️ Furniture</button>
    <button class="cat-pill" onclick="filterCat(this,'Automobile Parts')">🚗 Auto</button>
    <button class="cat-pill" onclick="filterCat(this,'Agricultural Produce')">🌱 Farm</button>
    <button class="cat-pill" onclick="filterCat(this,'Livestock & Poultry')">🐓 Livestock</button>
    <button class="cat-pill" onclick="filterCat(this,'Other')">📦 Other</button>
  </div>'''
new2 = '''  <div style="display:flex;gap:0;overflow-x:auto;padding:0 14px;scrollbar-width:none;background:#fff;border-bottom:1px solid var(--border);-webkit-overflow-scrolling:touch;">
    <button class="cat-pill active-pill" onclick="filterCat(this,'')">All</button>
    <button class="cat-pill" onclick="filterCat(this,'Foodstuff')">Foodstuff</button>
    <button class="cat-pill" onclick="filterCat(this,'Building Materials')">Building</button>
    <button class="cat-pill" onclick="filterCat(this,'Hardware')">Hardware</button>
    <button class="cat-pill" onclick="filterCat(this,'Electronics')">Electronics</button>
    <button class="cat-pill" onclick="filterCat(this,'Phones & Accessories')">Phones</button>
    <button class="cat-pill" onclick="filterCat(this,'Roofing Supplies')">Roofing</button>
    <button class="cat-pill" onclick="filterCat(this,'Timber & Plywood')">Timber</button>
    <button class="cat-pill" onclick="filterCat(this,'Fabric & Clothing')">Fashion</button>
    <button class="cat-pill" onclick="filterCat(this,'Beverages')">Beverages</button>
    <button class="cat-pill" onclick="filterCat(this,'Cosmetics & Beauty')">Beauty</button>
    <button class="cat-pill" onclick="filterCat(this,'Furniture')">Furniture</button>
    <button class="cat-pill" onclick="filterCat(this,'Automobile Parts')">Auto Parts</button>
    <button class="cat-pill" onclick="filterCat(this,'Agricultural Produce')">Farm</button>
    <button class="cat-pill" onclick="filterCat(this,'Livestock & Poultry')">Livestock</button>
    <button class="cat-pill" onclick="filterCat(this,'Other')">Other</button>
  </div>'''
if old2 in html:
    html = html.replace(old2, new2); changes += 1; print('2. Emojis removed done')
else: print('2. SKIP')

old3 = '''  <!-- STATS BAR -->
  <div style="background:linear-gradient(135deg,#1A1208,#3D2810);padding:14px 16px;display:flex;justify-content:space-between;align-items:center;cursor:pointer;border-bottom:1px solid rgba(255,255,255,0.06);" onclick="loadListings()">
    <div style="display:flex;align-items:center;gap:10px;">
      <div style="width:8px;height:8px;background:#0ECB81;border-radius:50%;box-shadow:0 0 6px #0ECB81;flex-shrink:0;"></div>
      <div>
        <div style="font-size:9px;color:var(--earth-lt);font-weight:700;letter-spacing:1.5px;text-transform:uppercase;">Live Market</div>
        <div style="font-family:'Syne',sans-serif;font-size:22px;font-weight:800;color:#fff;line-height:1.1;" id="count">0 Listings</div>
      </div>
    </div>
    <div style="text-align:right;">
      <div style="font-size:10px;color:#A0C878;font-weight:600;" id="hero-sub">↻ Tap to refresh</div>
      <div style="font-size:10px;color:rgba(255,255,255,0.4);margin-top:3px;" id="results-count"></div>
    </div>
  </div>'''
new3 = '''  <!-- STATS BAR -->
  <div style="background:#fff;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;cursor:pointer;border-bottom:1px solid var(--border);" onclick="loadListings()">
    <div style="display:flex;align-items:center;gap:8px;">
      <div style="width:7px;height:7px;background:#0ECB81;border-radius:50%;box-shadow:0 0 5px #0ECB81;flex-shrink:0;"></div>
      <div style="font-family:'Syne',sans-serif;font-size:15px;font-weight:800;color:var(--dark);" id="count">0 Listings</div>
    </div>
    <div style="display:flex;align-items:center;gap:10px;">
      <div style="font-size:10px;color:var(--muted);" id="results-count"></div>
      <div style="font-size:11px;color:var(--earth);font-weight:600;" id="hero-sub">↻ Refresh</div>
    </div>
  </div>'''
if old3 in html:
    html = html.replace(old3, new3); changes += 1; print('3. Stats bar done')
else: print('3. SKIP')

f = open('index.html', 'w')
f.write(html)
f.close()
print('TOTAL:', changes, '/3')

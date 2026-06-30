f = open('index.html', 'r')
html = f.read()
f.close()

old2 = '''  <div style="position:sticky;top:0;z-index:200;background:var(--dark);padding:10px 14px 8px;">
    <div style="position:relative;">
      <input type="text" id="search-bar" placeholder="🔍 Search items, sellers..." oninput="renderBoard()" style="background:#fff;padding:10px 36px 10px 14px;border:none;border-radius:10px;font-size:14px;margin:0;width:100%;">
      <span onclick="document.getElementById('search-bar').value='';renderBoard();" style="position:absolute;right:12px;top:50%;transform:translateY(-50%);color:var(--muted);cursor:pointer;font-size:18px;">✕</span>
    </div>
    <div style="display:flex;align-items:center;justify-content:space-between;margin-top:8px;">
      <button id="btn-use-location" onclick="requestBuyerLocation()" style="background:none;border:none;color:#A0C878;font-size:12px;font-weight:600;cursor:pointer;padding:0;">📍 <span id="loc-label">Tap to use location</span></button>
      <div style="display:flex;gap:6px;">
        <select id="filter-sort" onchange="renderBoard()" style="padding:5px 8px;border:none;border-radius:8px;font-size:11px;background:#2E2415;color:#A08060;">
          <option value="default">Sort</option>
          <option value="nearest">📍 Nearest</option>
          <option value="price-low">⬇ Price</option>
          <option value="price-high">⬆ Price</option>
          <option value="rising">▲ Rising</option>
          <option value="falling">▼ Falling</option>
        </select>
        <select id="filter-city" onchange="renderBoard()" style="padding:5px 8px;border:none;border-radius:8px;font-size:11px;background:#2E2415;color:#A08060;">
          <option value="">All Cities</option>
          <option value="Iwo">Iwo</option><option value="Osogbo">Osogbo</option>
          <option value="Ile-Ife">Ile-Ife</option><option value="Lagos">Lagos</option>
          <option value="Ibadan">Ibadan</option><option value="Abuja">Abuja</option>
          <option value="Kano">Kano</option><option value="Port Harcourt">Port Harcourt</option>
        </select>
      </div>
    </div>
  </div>'''

new2 = '''  <div style="position:sticky;top:0;z-index:200;background:var(--dark);padding:4px 14px 12px;">
    <div style="position:relative;margin-bottom:10px;">
      <input type="text" id="search-bar" placeholder="🔍 Search items, sellers..." oninput="renderBoard()" style="background:#fff;padding:11px 38px 11px 14px;border:none;border-radius:10px;font-size:14px;margin:0;width:100%;box-shadow:0 1px 3px rgba(0,0,0,0.15);">
      <span onclick="document.getElementById('search-bar').value='';renderBoard();" style="position:absolute;right:12px;top:50%;transform:translateY(-50%);color:var(--muted);cursor:pointer;font-size:18px;">✕</span>
    </div>
    <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;">
      <button id="btn-use-location" onclick="requestBuyerLocation()" style="background:none;border:none;color:#A0C878;font-size:12px;font-weight:600;cursor:pointer;padding:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex-shrink:1;min-width:0;">📍 <span id="loc-label">Tap to use location</span></button>
      <div style="display:flex;gap:6px;flex-shrink:0;">
        <select id="filter-sort" onchange="renderBoard()" style="padding:6px 8px;border:none;border-radius:8px;font-size:11px;background:rgba(255,255,255,0.08);color:#D4C5AC;">
          <option value="default">Sort</option>
          <option value="nearest">📍 Nearest</option>
          <option value="price-low">⬇ Price</option>
          <option value="price-high">⬆ Price</option>
          <option value="rising">▲ Rising</option>
          <option value="falling">▼ Falling</option>
        </select>
        <select id="filter-city" onchange="renderBoard()" style="padding:6px 8px;border:none;border-radius:8px;font-size:11px;background:rgba(255,255,255,0.08);color:#D4C5AC;">
          <option value="">All Cities</option>
          <option value="Iwo">Iwo</option><option value="Osogbo">Osogbo</option>
          <option value="Ile-Ife">Ile-Ife</option><option value="Lagos">Lagos</option>
          <option value="Ibadan">Ibadan</option><option value="Abuja">Abuja</option>
          <option value="Kano">Kano</option><option value="Port Harcourt">Port Harcourt</option>
        </select>
      </div>
    </div>
  </div>'''

if old2 in html:
    html = html.replace(old2, new2)
    print('Search bar tightened')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

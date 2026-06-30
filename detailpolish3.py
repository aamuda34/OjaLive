f = open('index.html', 'r')
html = f.read()
f.close()

old3 = '''      <!-- SELLER INFO -->
      <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px;margin-bottom:12px;">
        <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;margin-bottom:10px;">Seller Info</div>
        <div style="display:flex;align-items:flex-start;gap:12px;">
          <div id="bd-seller-photo" style="width:54px;height:54px;border-radius:50%;background:var(--earth);color:#fff;font-size:22px;display:flex;align-items:center;justify-content:center;flex-shrink:0;"></div>
          <div style="flex:1;">
            <div style="display:flex;align-items:center;justify-content:space-between;">
              <div id="bd-trader" style="font-size:15px;font-weight:700;color:var(--dark);"></div>
              <button id="bd-follow-btn2" onclick="toggleFollow()" style="padding:7px 14px;background:var(--earth);color:#fff;border:none;border-radius:20px;font-size:12px;font-weight:700;cursor:pointer;">+ Follow</button>
            </div>
            <div id="bd-followers-count" style="font-size:11px;color:var(--muted);margin-top:2px;"></div>
            <div id="bd-location" style="font-size:12px;color:var(--muted);margin-top:2px;"></div>
            <div id="bd-hours" style="font-size:11px;color:var(--green);margin-top:2px;"></div>
            <div id="bd-dist" style="font-size:11px;color:var(--green);font-weight:600;margin-top:2px;"></div>
          </div>
        </div>
      </div>'''

new3 = '''      <!-- SELLER INFO -->
      <div style="background:#FAF7F2;border:1px solid var(--border);border-radius:14px;padding:14px;margin:14px 0;">
        <div style="display:flex;align-items:center;gap:12px;">
          <div id="bd-seller-photo" style="width:48px;height:48px;border-radius:50%;background:var(--earth);color:#fff;font-size:19px;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-weight:700;"></div>
          <div style="flex:1;min-width:0;">
            <div id="bd-trader" style="font-size:14px;font-weight:700;color:var(--dark);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"></div>
            <div id="bd-followers-count" style="font-size:11px;color:var(--muted);"></div>
          </div>
          <button id="bd-follow-btn2" onclick="toggleFollow()" style="padding:7px 14px;background:var(--earth);color:#fff;border:none;border-radius:20px;font-size:11px;font-weight:700;cursor:pointer;flex-shrink:0;">+ Follow</button>
        </div>
        <div style="margin-top:10px;padding-top:10px;border-top:1px solid var(--border);display:flex;flex-direction:column;gap:4px;">
          <div id="bd-location" style="font-size:12px;color:var(--muted);"></div>
          <div id="bd-hours" style="font-size:11px;color:var(--green);"></div>
          <div id="bd-dist" style="font-size:11px;color:var(--green);font-weight:600;"></div>
        </div>
      </div>'''

if old3 in html:
    html = html.replace(old3, new3)
    print('3. Seller info card upgraded')
else:
    print('3. SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()
print('Saved part 3')

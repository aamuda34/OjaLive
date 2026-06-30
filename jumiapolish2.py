f = open('index.html', 'r')
html = f.read()
f.close()
changes = 0

old2 = '''    <div style="position:absolute;top:env(safe-area-inset-top,0px);left:0;right:0;padding:16px 16px 0;display:flex;align-items:center;justify-content:space-between;z-index:10;">
      <button onclick="closeBuyerDetail()" style="background:rgba(0,0,0,0.45);backdrop-filter:blur(6px);border:none;color:#fff;width:38px;height:38px;border-radius:50%;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.2);">←</button>
      <div style="display:none;color:#fff;font-family:'Syne',sans-serif;font-size:16px;font-weight:700;" id="bd-title">Item Detail</div>
    </div>
    <div id="bd-images" style="background:#F5F0E8;height:300px;padding-top:env(safe-area-inset-top,0px);display:flex;overflow-x:auto;scrollbar-width:none;scroll-snap-type:x mandatory;"></div>'''

new2 = '''    <div style="position:absolute;top:env(safe-area-inset-top,0px);left:0;right:0;padding:16px 16px 0;display:flex;align-items:center;justify-content:space-between;z-index:10;">
      <button onclick="closeBuyerDetail()" style="background:rgba(0,0,0,0.4);backdrop-filter:blur(6px);border:none;color:#fff;width:38px;height:38px;border-radius:50%;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.15);">←</button>
      <button onclick="shareItem()" style="background:rgba(0,0,0,0.4);backdrop-filter:blur(6px);border:none;color:#fff;width:38px;height:38px;border-radius:50%;font-size:15px;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.15);">⤴</button>
      <div style="display:none;color:#fff;font-family:'Syne',sans-serif;font-size:16px;font-weight:700;" id="bd-title">Item Detail</div>
    </div>
    <div id="bd-images" style="background:#fff;height:300px;padding-top:env(safe-area-inset-top,0px);display:flex;overflow-x:auto;scrollbar-width:none;scroll-snap-type:x mandatory;border-bottom:1px solid #F0F0F0;"></div>'''

if old2 in html:
    html = html.replace(old2, new2)
    changes += 1
    print('White background + share button added')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

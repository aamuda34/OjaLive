f = open('index.html', 'r')
html = f.read()
f.close()

changes = 0

old1 = '''  <div id="buyer-item-detail" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:var(--bg);z-index:500;overflow-y:auto;">
    <div style="position:sticky;top:0;background:var(--dark);padding:14px 16px;display:flex;align-items:center;gap:12px;z-index:10;">
      <button onclick="closeBuyerDetail()" style="background:none;border:none;color:#fff;font-size:22px;cursor:pointer;">←</button>
      <div style="color:#fff;font-family:'Syne',sans-serif;font-size:16px;font-weight:700;" id="bd-title">Item Detail</div>
    </div>
    <div id="bd-images" style="background:#000;min-height:200px;display:flex;overflow-x:auto;scrollbar-width:none;"></div>'''

new1 = '''  <div id="buyer-item-detail" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:#fff;z-index:500;overflow-y:auto;">
    <div style="position:absolute;top:0;left:0;right:0;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;z-index:10;">
      <button onclick="closeBuyerDetail()" style="background:rgba(0,0,0,0.45);backdrop-filter:blur(6px);border:none;color:#fff;width:36px;height:36px;border-radius:50%;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;">←</button>
      <div style="display:none;color:#fff;font-family:'Syne',sans-serif;font-size:16px;font-weight:700;" id="bd-title">Item Detail</div>
    </div>
    <div id="bd-images" style="background:#F0EAE0;height:280px;display:flex;overflow-x:auto;scrollbar-width:none;scroll-snap-type:x mandatory;"></div>'''

if old1 in html:
    html = html.replace(old1, new1)
    changes += 1
    print('1. Header/image area upgraded')
else:
    print('1. SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()
print('Saved part 1')

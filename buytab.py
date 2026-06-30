f = open('index.html', 'r')
html = f.read()
f.close()

# 1. Upgrade stats bar
old1 = '  <div style="background:linear-gradient(135deg,var(--dark),#3D2810);padding:10px 14px;display:flex;justify-content:space-between;align-items:center;cursor:pointer;" onclick="loadListings()">\n    <div>\n      <div style="font-size:10px;color:var(--earth-lt);font-weight:700;letter-spacing:1px;text-transform:uppercase;">Live Market</div>\n      <div style="font-family:\'Syne\',sans-serif;font-size:20px;font-weight:800;color:#fff;" id="count">0 Listings</div>\n    </div>\n    <div style="text-align:right;">\n      <div style="font-size:11px;color:#A0C878;" id="hero-sub">Tap to refresh</div>\n      <div style="font-size:11px;color:var(--earth-lt);margin-top:2px;" id="results-count"></div>\n    </div>\n  </div>'
new1 = '  <div style="background:linear-gradient(135deg,#1A1208,#3D2810);padding:14px 16px;display:flex;justify-content:space-between;align-items:center;cursor:pointer;border-bottom:1px solid rgba(255,255,255,0.06);" onclick="loadListings()">\n    <div style="display:flex;align-items:center;gap:10px;">\n      <div style="width:8px;height:8px;background:#0ECB81;border-radius:50%;box-shadow:0 0 6px #0ECB81;flex-shrink:0;"></div>\n      <div>\n        <div style="font-size:9px;color:var(--earth-lt);font-weight:700;letter-spacing:1.5px;text-transform:uppercase;">Live Market</div>\n        <div style="font-family:\'Syne\',sans-serif;font-size:22px;font-weight:800;color:#fff;line-height:1.1;" id="count">0 Listings</div>\n      </div>\n    </div>\n    <div style="text-align:right;">\n      <div style="font-size:10px;color:#A0C878;font-weight:600;" id="hero-sub">↻ Tap to refresh</div>\n      <div style="font-size:10px;color:rgba(255,255,255,0.4);margin-top:3px;" id="results-count"></div>\n    </div>\n  </div>'

if old1 in html:
    html = html.replace(old1, new1)
    print('Stats bar upgraded')
else:
    print('SKIP: Stats bar not found')

# 2. Upgrade image placeholder
old2 = "imgHtml='<div style=\"width:100%;height:140px;display:flex;align-items:center;justify-content:center;font-size:48px;background:linear-gradient(135deg,#F7F2EA,#EDE5D8);\">'+emoji+'</div>';"
new2 = "imgHtml='<div style=\"width:100%;height:150px;display:flex;align-items:center;justify-content:center;font-size:52px;background:linear-gradient(135deg,#F0EAE0,#E5D9C8);\">'+emoji+'</div>';"

if old2 in html:
    html = html.replace(old2, new2)
    print('Image placeholder upgraded')
else:
    print('SKIP: Image placeholder not found')

f = open('index.html', 'w')
f.write(html)
f.close()
print('Done!')

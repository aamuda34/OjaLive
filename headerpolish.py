f = open('index.html', 'r')
html = f.read()
f.close()

old1 = '''<div class="topbar">
  <div class="logo">Oja<span>Live</span></div>
  <div style="background:var(--earth);color:#fff;font-size:11px;font-weight:600;padding:4px 12px;border-radius:20px;">OjaLive v2.0</div>
</div>'''

new1 = '''<div class="topbar">
  <div class="logo">Oja<span>Live</span></div>
  <div style="display:flex;align-items:center;gap:6px;background:rgba(14,203,129,0.12);padding:5px 12px 5px 10px;border-radius:20px;">
    <span style="width:6px;height:6px;background:#0ECB81;border-radius:50%;box-shadow:0 0 5px #0ECB81;"></span>
    <span style="color:#0ECB81;font-size:11px;font-weight:700;letter-spacing:0.3px;">LIVE</span>
  </div>
</div>'''

if old1 in html:
    html = html.replace(old1, new1)
    print('Header badge softened')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

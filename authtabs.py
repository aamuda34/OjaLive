f = open('index.html', 'r')
html = f.read()
f.close()

old = """      <div style="text-align:center;margin-bottom:32px;">
        <div style="font-family:'Syne',sans-serif;font-size:40px;font-weight:800;">Oja<span style="color:var(--earth);">Live</span></div>
        <div style="font-size:14px;color:var(--muted);margin-top:6px;letter-spacing:1px;text-transform:uppercase;font-weight:600;">Seller Portal</div>
      </div>
      <div class="card" style="margin-bottom:16px;">
        <div class="card-title" style="margin-bottom:18px;">New Seller</div>"""

new = """      <div style="text-align:center;margin-bottom:28px;">
        <div style="font-family:'Syne',sans-serif;font-size:40px;font-weight:800;">Oja<span style="color:var(--earth);">Live</span></div>
        <div style="font-size:14px;color:var(--muted);margin-top:6px;letter-spacing:1px;text-transform:uppercase;font-weight:600;">Seller Portal</div>
      </div>
      <div style="display:flex;background:#F0EAE0;border-radius:12px;padding:4px;margin-bottom:20px;">
        <button type="button" id="auth-tab-login" onclick="switchAuthTab('login')" style="flex:1;padding:11px;border:none;border-radius:9px;font-size:13px;font-weight:700;cursor:pointer;background:var(--dark);color:#fff;">Login</button>
        <button type="button" id="auth-tab-register" onclick="switchAuthTab('register')" style="flex:1;padding:11px;border:none;border-radius:9px;font-size:13px;font-weight:700;cursor:pointer;background:transparent;color:var(--muted);">New Seller</button>
      </div>
      <div class="card hidden" id="auth-panel-register" style="margin-bottom:16px;">
        <div class="card-title" style="margin-bottom:18px;">Create Your Seller Account</div>"""

count = 0
if old in html:
    html = html.replace(old, new)
    count += 1
    print('1. Tab toggle added')
else:
    print('1. SKIP')

f = open('index.html', 'w')
f.write(html)
f.close()

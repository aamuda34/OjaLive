f = open('index.html', 'r')
html = f.read()
f.close()

old = '      <div class="card" id="auth-panel-login">'

new = """      <div class=\"card hidden\" id=\"auth-panel-success\" style=\"text-align:center;padding:36px 20px;\">
        <div style=\"width:64px;height:64px;border-radius:50%;background:#E8F5EE;display:flex;align-items:center;justify-content:center;margin:0 auto 18px;font-size:32px;color:#2D7A4F;\">✓</div>
        <div style=\"font-family:'Syne',sans-serif;font-size:19px;font-weight:800;color:var(--dark);margin-bottom:8px;\">Account Created!</div>
        <div style=\"font-size:13px;color:var(--muted);line-height:1.5;margin-bottom:22px;\">Welcome to OjaLive. Your seller account is ready. Please login to start posting your items.</div>
        <button type=\"button\" class=\"btn btn-p\" onclick=\"switchAuthTab('login')\" style=\"margin:0;\">Continue to Login</button>
      </div>
      <div class=\"card\" id=\"auth-panel-login\">"""

if old in html:
    html = html.replace(old, new, 1)
    print('Success screen HTML added')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

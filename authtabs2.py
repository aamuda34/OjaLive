f = open('index.html', 'r')
html = f.read()
f.close()

old = """      <div style="text-align:center;color:var(--muted);font-size:12px;margin:20px 0;letter-spacing:1px;text-transform:uppercase;font-weight:600;">or login</div>
      <div class="card">
        <div class="card-title" style="margin-bottom:18px;">Existing Seller</div>"""

new = """      <div class="card" id="auth-panel-login">
        <div class="card-title" style="margin-bottom:18px;">Login to Your Account</div>"""

if old in html:
    html = html.replace(old, new)
    print('Login panel wrapped')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

f = open('index.html', 'r')
html = f.read()
f.close()

old = """      <div class="card hidden" id="auth-panel-register" style="margin-bottom:16px;">
        <div class="card-title" style="margin-bottom:18px;">Create Your Seller Account</div>
        <label>Shop Name</label>"""

new = """      <div class="card hidden" id="auth-panel-register" style="margin-bottom:16px;">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;">
          <div class="card-title" style="margin-bottom:0;">Create Your Seller Account</div>
          <div style="font-size:11px;color:var(--earth);font-weight:700;" id="reg-step-label">Step 1 of 3</div>
        </div>
        <div style="display:flex;gap:4px;margin-bottom:20px;">
          <div id="reg-progress-1" style="flex:1;height:3px;border-radius:2px;background:var(--earth);"></div>
          <div id="reg-progress-2" style="flex:1;height:3px;border-radius:2px;background:var(--border);"></div>
          <div id="reg-progress-3" style="flex:1;height:3px;border-radius:2px;background:var(--border);"></div>
        </div>
        <div id="reg-step-1">
        <label>Shop Name</label>"""

if old in html:
    html = html.replace(old, new)
    print('1. Progress bar and step-1 wrapper opened')
else:
    print('1. SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

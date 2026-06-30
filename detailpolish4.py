f = open('index.html', 'r')
html = f.read()
f.close()

old4 = '''      <!-- ACTION BUTTONS -->
      <button id="bd-chat-btn" style="width:100%;padding:14px;background:var(--earth);color:#fff;border:none;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;margin-bottom:8px;">💬 Chat Now — Recommended</button>
      <div style="display:flex;gap:8px;margin-bottom:8px;">
        <a id="bd-wa-btn" href="#" target="_blank" style="flex:1;padding:12px;background:#25D366;color:#fff;border-radius:10px;font-size:13px;font-weight:600;text-decoration:none;text-align:center;display:block;">💬 WhatsApp</a>
        <a id="bd-call-btn" href="#" style="flex:1;padding:12px;background:#E8F5EE;color:var(--green);border-radius:10px;font-size:13px;font-weight:600;text-decoration:none;text-align:center;display:block;">📞 Call</a>
        <button id="bd-dir-btn" style="flex:1;padding:12px;background:var(--dark);color:#fff;border:none;border-radius:10px;font-size:13px;font-weight:600;cursor:pointer;">📍 Directions</button>
      </div>'''

new4 = '''      <!-- ACTION BUTTONS -->
      <div style="display:flex;gap:8px;margin-bottom:14px;">
        <a id="bd-wa-btn" href="#" target="_blank" style="flex:1.3;padding:13px;background:#25D366;color:#fff;border-radius:11px;font-size:13px;font-weight:700;text-decoration:none;text-align:center;display:flex;align-items:center;justify-content:center;gap:5px;">💬 WhatsApp</a>
        <a id="bd-call-btn" href="#" style="flex:1;padding:13px;background:var(--dark);color:#fff;border-radius:11px;font-size:13px;font-weight:700;text-decoration:none;text-align:center;display:flex;align-items:center;justify-content:center;gap:5px;">📞 Call</a>
        <button id="bd-dir-btn" style="width:46px;flex-shrink:0;padding:13px 0;background:#fff;border:1.5px solid var(--border);color:var(--dark);border-radius:11px;font-size:16px;cursor:pointer;">📍</button>
      </div>
      <button id="bd-chat-btn" style="display:none;width:100%;padding:14px;background:var(--earth);color:#fff;border:none;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;margin-bottom:8px;">💬 Chat Now</button>'''

if old4 in html:
    html = html.replace(old4, new4)
    print('4. Action buttons upgraded')
else:
    print('4. SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()
print('Saved part 4 - ALL DONE')

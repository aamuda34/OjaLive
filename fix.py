with open('/storage/emulated/0/OjaLive/index.html', 'r') as f:
    content = f.read()

old = """    var chatBtn = '<button onclick="showToast('In-app chat coming soon!')" style="display:block;width:100%;margin-top:6px;padding:10px;background:var(--earth);color:#fff;border:none;border-radius:8px;font-size:13px;font-weight:700;cursor:pointer;">💬 Chat Now — Recommended</button>';"""

new = """    var chatBtn = '<button onclick="showToast(&quot;In-app chat coming soon!&quot;)" style="display:block;width:100%;margin-top:6px;padding:10px;background:var(--earth);color:#fff;border:none;border-radius:8px;font-size:13px;font-weight:700;cursor:pointer;">\U0001f4ac Chat Now \u2014 Recommended</button>';"""

if old in content:
    content = content.replace(old, new)
    print("Fixed: chatBtn quotes corrected")
else:
    print("FAILED")

with open('/storage/emulated/0/OjaLive/index.html', 'w') as f:
    f.write(content)

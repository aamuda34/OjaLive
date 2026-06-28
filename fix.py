with open('/storage/emulated/0/OjaLive/index.html', 'r') as f:
    content = f.read()

old = '      <label>Business Description</label>\n      <textarea id="edit-profile-description" placeholder="Tell buyers about your business..." style="width:100%;padding:12px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;resize:none;height:80px;font-family:inherit;"></textarea>'

new = '      <label>Opening Hours</label>\n      <div style="display:flex;gap:8px;margin-bottom:8px;">\n        <input type="time" id="edit-open-from" style="flex:1;padding:10px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;">\n        <span style="align-self:center;color:var(--muted);">to</span>\n        <input type="time" id="edit-open-to" style="flex:1;padding:10px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;">\n      </div>\n      <select id="edit-open-days" style="width:100%;padding:10px 12px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;background:#fff;margin-bottom:10px;">\n        <option value="Mon-Fri">Monday - Friday</option>\n        <option value="Mon-Sat">Monday - Saturday</option>\n        <option value="Mon-Sun">Monday - Sunday (All week)</option>\n        <option value="Tue-Sun">Tuesday - Sunday</option>\n        <option value="Weekends">Weekends Only</option>\n      </select>\n      <label>Business Description</label>\n      <textarea id="edit-profile-description" placeholder="Tell buyers about your business..." style="width:100%;padding:12px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;resize:none;height:80px;font-family:inherit;"></textarea>'

if old in content:
    content = content.replace(old, new)
    print("Done: opening hours added to edit profile")
else:
    print("FAILED")

with open('/storage/emulated/0/OjaLive/index.html', 'w') as f:
    f.write(content)

path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

reps = []

reps.append((
'<div style="margin-top:6px;" id="profile-status-badge"><span class="spill">\u2714 Verified Seller</span></div>',
'<div style="margin-top:6px;" id="profile-status-badge"><span class="spill">\u2714 Active Seller</span></div>'
))

reps.append((
'''    if (currentSeller.status === 'approved') {
      statusBadge.innerHTML = '<span class="spill">\u2714 Verified Seller</span>';''',
'''    if (currentSeller.status === 'approved') {
      statusBadge.innerHTML = '<span class="spill">\u2714 Active Seller</span>';'''
))

reps.append((
'''      <div style="display:flex;gap:8px;margin-top:14px;">
        <button class="btn btn-p" id="btn-detail-edit" style="flex:1;margin:0;">\u270f\ufe0f Edit</button>
        <button class="btn btn-o" id="btn-detail-pause" style="flex:1;margin:0;border-color:var(--amber);color:var(--amber);">\u23f8\ufe0f Pause</button>
        <button class="btn btn-o" id="btn-detail-delete" style="flex:1;margin:0;border-color:var(--red);color:var(--red);">\U0001F5D1\ufe0f Delete</button>
      </div>
      <div style="display:flex;gap:8px;margin-top:8px;">
        <button class="btn btn-o" id="btn-detail-duplicate" style="flex:1;margin:0;border-color:var(--green);color:var(--green);">\U0001F4CB Duplicate</button>
        <button class="btn btn-o" id="btn-detail-share" style="flex:1;margin:0;border-color:var(--dark);color:var(--dark);">\U0001F4E4 Share</button>
        <button class="btn btn-o" id="btn-detail-export" style="flex:1;margin:0;">\U0001F4CA Export</button>
      </div>
    </div>
    <div class="card">
      <div class="card-title">\U0001F4C8 Price History</div>''',
'''      <button class="btn btn-p" id="btn-detail-edit" style="width:100%;margin:14px 0 0;display:flex;align-items:center;justify-content:center;gap:7px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 013 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>Edit Listing</button>
      <div style="display:flex;gap:6px;margin-top:8px;">
        <button id="btn-detail-pause" style="flex:1;padding:9px 2px;background:var(--card);border:1px solid var(--border);color:var(--amber);border-radius:9px;font-size:10px;font-weight:600;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:4px;"></button>
        <button id="btn-detail-duplicate" style="flex:1;padding:9px 2px;background:var(--card);border:1px solid var(--border);color:var(--dark);border-radius:9px;font-size:10px;font-weight:600;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:4px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>Duplicate</button>
        <button id="btn-detail-share" style="flex:1;padding:9px 2px;background:var(--card);border:1px solid var(--border);color:var(--dark);border-radius:9px;font-size:10px;font-weight:600;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:4px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.6" y1="10.5" x2="15.4" y2="6.5"/><line x1="8.6" y1="13.5" x2="15.4" y2="17.5"/></svg>Share</button>
        <button id="btn-detail-export" style="flex:1;padding:9px 2px;background:var(--card);border:1px solid var(--border);color:var(--dark);border-radius:9px;font-size:10px;font-weight:600;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:4px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>Export</button>
      </div>
      <div style="text-align:center;margin-top:10px;">
        <button id="btn-detail-delete" style="background:none;border:none;color:var(--red);font-size:12px;font-weight:600;cursor:pointer;padding:6px;display:inline-flex;align-items:center;gap:5px;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"/></svg>Delete this listing</button>
      </div>
    </div>
    <div class="card">
      <div class="card-title" style="display:flex;align-items:center;gap:6px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>Price History</div>'''
))

reps.append((
'''  var isPaused = item.verified === false;
  var pauseBtn = document.getElementById('btn-detail-pause');
  pauseBtn.textContent = isPaused ? '\u25b6\ufe0f Activate' : '\u23f8\ufe0f Pause';
  pauseBtn.style.color = isPaused ? 'var(--green)' : 'var(--amber)';
  pauseBtn.style.borderColor = isPaused ? 'var(--green)' : 'var(--amber)';''',
'''  var isPaused = item.verified === false;
  var pauseBtn = document.getElementById('btn-detail-pause');
  var pauseIcon = isPaused
    ? '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="5,3 19,12 5,21"/></svg>'
    : '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>';
  pauseBtn.innerHTML = pauseIcon + (isPaused ? 'Activate' : 'Pause');
  pauseBtn.style.color = isPaused ? 'var(--green)' : 'var(--amber)';'''
))

reps.append((
'      <div class="card-title">\U0001F4C8 Price History</div>',
'      <div class="card-title" style="display:flex;align-items:center;gap:6px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>Price History</div>'
))

count = 0
for i, (old, new) in enumerate(reps, 1):
    n = content.count(old)
    if n == 1:
        content = content.replace(old, new, 1)
        count += 1
    else:
        print("WARNING: pattern #" + str(i) + " found " + str(n) + " times (expected 1), skipped")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. " + str(count) + "/" + str(len(reps)) + " replacements applied.")

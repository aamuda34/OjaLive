import urllib.request, json, re

with open('/storage/emulated/0/OjaLive/index.html', 'r') as f:
    content = f.read()

# Fix 1: Harden Supabase init
old = "  var createClient = window.supabase.createClient || (window.supabase && window.supabase.default && window.supabase.default.createClient);\n  if (!createClient) { setTimeout(function(){initDB();}, 200); return; }\n  db = createClient(SUPABASE_URL, SUPABASE_KEY);\n\n  try {"
new = "  var sc = window.supabase;\n  var createClient = sc && (sc.createClient || (sc.default && sc.default.createClient));\n  if (typeof createClient !== 'function') { setTimeout(initDB, 200); return; }\n  try { db = createClient(SUPABASE_URL, SUPABASE_KEY); } catch(e) { setTimeout(initDB, 200); return; }\n  if (!db || typeof db.from !== 'function') { db = null; setTimeout(initDB, 200); return; }\n  try {"
if old in content: content = content.replace(old, new); print("Fix 1 done")
else: print("Fix 1 FAILED")

# Fix 2: Remove debug-msg
content = content.replace('    <div id="debug-msg" style="font-size:10px;color:#ff9;margin-top:4px;"></div>\n', '')
print("Fix 2 done")

# Fix 3: Clean loadListings
old3 = "async function loadListings() {\n  var dbg = document.getElementById('debug-msg');\n  if (!db) { if(dbg) dbg.textContent = 'DB not ready yet'; return; }\n  try {\n    if(dbg) dbg.textContent = 'Connecting to DB...';\n    var result = await db.from('Listing').select('*').eq('verified', true);\n    if(dbg) dbg.textContent = 'Got result. Error: '+(result.error?result.error.message:'none')+' Data: '+(result.data?result.data.length:0)+' items';\n    if (result.error) { showToast('Error: '+result.error.message); return; }\n    allListings = result.data || [];\n    var now = new Date();\n    var timeStr = now.toLocaleTimeString('en-NG',{hour:'2-digit',minute:'2-digit'});\n    var sub = document.getElementById('hero-sub');\n    if(sub) sub.textContent = 'Updated '+timeStr+' \xb7 Tap to refresh';\n    renderBoard();\n  } catch(e) {\n    if(dbg) dbg.textContent = 'CATCH ERROR: '+e.message;\n    showToast('Fatal error: '+e.message);\n  }\n}"
new3 = "async function loadListings() {\n  if (!db) return;\n  try {\n    var result = await db.from('Listing').select('*').eq('verified', true);\n    if (result.error) { showToast('Error loading prices'); return; }\n    allListings = result.data || [];\n    var now = new Date();\n    var timeStr = now.toLocaleTimeString('en-NG',{hour:'2-digit',minute:'2-digit'});\n    var sub = document.getElementById('hero-sub');\n    if(sub) sub.textContent = 'Updated '+timeStr+' \xb7 Tap to refresh';\n    renderBoard();\n  } catch(e) {\n    showToast('Connection error. Check internet.');\n  }\n}"
if old3 in content: content = content.replace(old3, new3); print("Fix 3 done")
else: print("Fix 3 FAILED")

# Fix 4: Hero onclick
content = content.replace("onclick=\"if(db)loadListings();else showToast('Still loading...')\"", 'onclick="loadListings()"')
print("Fix 4 done")

# Fix 5: Remove console.log from register
content = content.replace("  console.log('Registering:', {name,phone,fullLocation,regLat,regLng});\n", '')
content = content.replace("  console.log('Register result:', result);\n", '')
print("Fix 5 done")

# Fix 6: Fix showFullImage broken quotes
old6 = "          detailImgEl.innerHTML = dimgs.map(function(url,i) {\n            return '<div style=\"flex:none;width:'+(dimgs.length===1?'100%':'48%')+';aspect-ratio:4/3;border-radius:10px;overflow:hidden;\"><img src=\"'+url+'\" style=\"width:100%;height:100%;object-fit:cover;\" onclick=\"showFullImage('+\"''\"+'+url+'+\"''\"+')\">'+'</div>';\n          }).join('');"
new6 = "          detailImgEl.innerHTML = dimgs.map(function(url,i) {\n            var safeUrl = url.replace(/\"/g,'&quot;');\n            return '<div style=\"flex:none;width:'+(dimgs.length===1?'100%':'48%')+';aspect-ratio:4/3;border-radius:10px;overflow:hidden;cursor:pointer;\" onclick=\"showFullImage(this.firstChild.src)\"><img src=\"'+safeUrl+'\" style=\"width:100%;height:100%;object-fit:cover;pointer-events:none;\"></div>';\n          }).join('');"

# Try a regex replace for this one
import re
pattern = r"detailImgEl\.innerHTML = dimgs\.map\(function\(url,i\) \{.*?\.join\(''\);"
replacement = "detailImgEl.innerHTML = dimgs.map(function(url,i) {\n            var safeUrl = url.replace(/\"/g,'&quot;');\n            return '<div style=\"flex:none;width:'+(dimgs.length===1?'100%':'48%')+';aspect-ratio:4/3;border-radius:10px;overflow:hidden;cursor:pointer;\" onclick=\"showFullImage(this.firstChild.src)\"><img src=\"'+safeUrl+'\" style=\"width:100%;height:100%;object-fit:cover;pointer-events:none;\"></div>';\n          }).join('');"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
if new_content != content:
    content = new_content
    print("Fix 6 done: showFullImage fixed")
else:
    print("Fix 6 FAILED")

# Fix 7: Remove duplicate timeAgo2
old7 = "  var times=changes.map(function(h){return timeAgo2(h.created_at);});\n  function timeAgo2(ts){\n    if(!ts)return '';\n    var diff=Math.floor((Date.now()-new Date(ts).getTime())/1000);\n    if(diff<60)return diff+'s';\n    if(diff<3600)return Math.floor(diff/60)+'m';\n    if(diff<86400)return Math.floor(diff/3600)+'h';\n    if(diff<604800)return Math.floor(diff/86400)+'d';\n    return Math.floor(diff/604800)+'w';\n  }\n  times.forEach(function(t,i){"
new7 = "  times.forEach(function(t,i){"
if old7 in content: content = content.replace(old7, new7); print("Fix 7 done: duplicate timeAgo2 removed")
else: print("Fix 7 FAILED")

with open('/storage/emulated/0/OjaLive/index.html', 'w') as f:
    f.write(content)
print("\nAll done!")

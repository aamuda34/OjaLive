with open('/storage/emulated/0/OjaLive/index.html', 'r') as f:
    content = f.read()

fixes = 0

# 1. Add image counter overlay
old = '''    <div id="bd-images" style="background:#fff;height:300px;padding-top:env(safe-area-inset-top,0px);display:flex;overflow-x:auto;scrollbar-width:none;scroll-snap-type:x mandatory;border-bottom:1px solid #F0F0F0;"></div>'''
new = '''    <div style="position:relative;">
      <div id="bd-images" onscroll="updateImageCounter()" style="background:#fff;height:300px;padding-top:env(safe-area-inset-top,0px);display:flex;overflow-x:auto;scrollbar-width:none;scroll-snap-type:x mandatory;border-bottom:1px solid #F0F0F0;"></div>
      <div id="bd-img-counter" style="display:none;position:absolute;bottom:10px;right:12px;background:rgba(0,0,0,0.55);color:#fff;font-size:11px;font-weight:600;padding:3px 10px;border-radius:20px;">1/1</div>
    </div>'''
if old in content:
    content = content.replace(old, new)
    fixes += 1
    print("Fix 1 done: image counter overlay added")
else:
    print("Fix 1 FAILED")

# 2. Remove casual like/dislike + inline action buttons
old2 = '''      <!-- LIKES/DISLIKES -->
      <div style="display:flex;gap:8px;margin-bottom:12px;">
        <button id="bd-like-btn" onclick="likeItem()" style="flex:1;padding:10px;background:#E8F5EE;color:var(--green);border:1.5px solid var(--green);border-radius:10px;font-size:13px;font-weight:600;cursor:pointer;">👍 <span id="bd-likes">0</span></button>
        <button id="bd-dislike-btn" onclick="dislikeItem()" style="flex:1;padding:10px;background:#FDECEA;color:var(--red);border:1.5px solid var(--red);border-radius:10px;font-size:13px;font-weight:600;cursor:pointer;">👎 <span id="bd-dislikes">0</span></button>
      </div>
      <!-- ACTION BUTTONS -->
      <div style="display:flex;gap:8px;margin-bottom:14px;">
        <a id="bd-wa-btn" href="#" target="_blank" style="flex:1.3;padding:13px;background:#25D366;color:#fff;border-radius:11px;font-size:13px;font-weight:700;text-decoration:none;text-align:center;display:flex;align-items:center;justify-content:center;gap:5px;">💬 WhatsApp</a>
        <a id="bd-call-btn" href="#" style="flex:1;padding:13px;background:var(--dark);color:#fff;border-radius:11px;font-size:13px;font-weight:700;text-decoration:none;text-align:center;display:flex;align-items:center;justify-content:center;gap:5px;">📞 Call</a>
        <button id="bd-dir-btn" style="width:46px;flex-shrink:0;padding:13px 0;background:#fff;border:1.5px solid var(--border);color:var(--dark);border-radius:11px;font-size:16px;cursor:pointer;">📍</button>
      </div>
      <button id="bd-chat-btn" style="display:none;width:100%;padding:14px;background:var(--earth);color:#fff;border:none;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;margin-bottom:8px;">💬 Chat Now</button>'''
new2 = '''      <button id="bd-chat-btn" style="display:none;width:100%;padding:14px;background:var(--earth);color:#fff;border:none;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;margin-bottom:14px;">💬 Chat Now</button>'''
if old2 in content:
    content = content.replace(old2, new2)
    fixes += 1
    print("Fix 2 done: casual like/dislike removed")
else:
    print("Fix 2 FAILED")

# 3. Add sticky bottom action bar
old3 = '''      <!-- PRICE HISTORY MINI -->
      <div id="bd-history-section" style="display:none;background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px;">
        <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;margin-bottom:10px;">Price History</div>
        <canvas id="bd-price-chart" style="width:100%;height:140px;border-radius:8px;"></canvas>
        <div id="bd-history-list" style="margin-top:10px;"></div>
      </div>
    </div>
  </div>
</div>'''
new3 = '''      <!-- PRICE HISTORY MINI -->
      <div id="bd-history-section" style="display:none;background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px;margin-bottom:80px;">
        <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;margin-bottom:10px;">Price History</div>
        <canvas id="bd-price-chart" style="width:100%;height:140px;border-radius:8px;"></canvas>
        <div id="bd-history-list" style="margin-top:10px;"></div>
      </div>
      <div style="height:80px;"></div>
    </div>
    <!-- STICKY BOTTOM ACTION BAR -->
    <div style="position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid var(--border);padding:10px 16px calc(10px + env(safe-area-inset-bottom,0px));display:flex;gap:8px;z-index:20;box-shadow:0 -4px 16px rgba(0,0,0,0.06);">
      <a id="bd-wa-btn" href="#" target="_blank" style="flex:1.3;padding:13px;background:#25D366;color:#fff;border-radius:11px;font-size:13px;font-weight:700;text-decoration:none;text-align:center;display:flex;align-items:center;justify-content:center;gap:5px;">💬 WhatsApp</a>
      <a id="bd-call-btn" href="#" style="flex:1;padding:13px;background:var(--dark);color:#fff;border-radius:11px;font-size:13px;font-weight:700;text-decoration:none;text-align:center;display:flex;align-items:center;justify-content:center;gap:5px;">📞 Call</a>
      <button id="bd-dir-btn" style="width:46px;flex-shrink:0;padding:13px 0;background:#fff;border:1.5px solid var(--border);color:var(--dark);border-radius:11px;font-size:16px;cursor:pointer;">📍</button>
    </div>
  </div>
</div>'''
if old3 in content:
    content = content.replace(old3, new3)
    fixes += 1
    print("Fix 3 done: sticky bottom action bar added")
else:
    print("Fix 3 FAILED")

# 4. Fix crash: remove leftover DOM refs to deleted like/dislike buttons in openBuyerDetail
old4 = """  var liked = localStorage.getItem('liked_'+item.id);
  var disliked = localStorage.getItem('disliked_'+item.id);
  if(liked){
    document.getElementById('bd-like-btn').style.background='#0ECB81';
    document.getElementById('bd-like-btn').style.color='#fff';
  }
  if(disliked){
    document.getElementById('bd-dislike-btn').style.background='#F6465D';
    document.getElementById('bd-dislike-btn').style.color='#fff';
  }
  document.getElementById('bd-likes').textContent = item.likes||0;
  document.getElementById('bd-dislikes').textContent = item.dislikes||0;
  document.getElementById('bd-like-btn').style.background = '#E8F5EE';
  document.getElementById('bd-like-btn').style.color = 'var(--green)';
  document.getElementById('bd-dislike-btn').style.background = '#FDECEA';
  document.getElementById('bd-dislike-btn').style.color = 'var(--red)';"""
new4 = """  updateImageCounter();"""
if old4 in content:
    content = content.replace(old4, new4)
    fixes += 1
    print("Fix 4 done: removed crash-prone refs, hooked image counter")
else:
    print("Fix 4 FAILED")

# 5. Track gallery count + set/hide counter when images load
old5 = '''  if(galleryImgs.length > 0){
    galleryImgs.forEach(function(url){
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:20px;box-sizing:border-box;">'
        + '<img src="'+url+'" style="max-width:100%;max-height:100%;object-fit:contain;border-radius:8px;" loading="lazy" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });
  } else {
    imgEl.innerHTML='<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:64px;">🏪</div>';
  }'''
new5 = '''  window.bdGalleryCount = galleryImgs.length;
  var counterEl = document.getElementById('bd-img-counter');
  if(galleryImgs.length > 0){
    galleryImgs.forEach(function(url){
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:20px;box-sizing:border-box;">'
        + '<img src="'+url+'" style="max-width:100%;max-height:100%;object-fit:contain;border-radius:8px;" loading="lazy" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });
    if(counterEl){
      if(galleryImgs.length > 1){ counterEl.style.display='block'; counterEl.textContent='1/'+galleryImgs.length; }
      else { counterEl.style.display='none'; }
    }
  } else {
    imgEl.innerHTML='<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:64px;">🏪</div>';
    if(counterEl) counterEl.style.display='none';
  }'''
if old5 in content:
    content = content.replace(old5, new5)
    fixes += 1
    print("Fix 5 done: gallery counter tracking added")
else:
    print("Fix 5 FAILED")

# 6. Add updateImageCounter function before closeBuyerDetail
old6 = "function closeBuyerDetail() {"
new6 = """function updateImageCounter() {
  var el = document.getElementById('bd-images');
  var counterEl = document.getElementById('bd-img-counter');
  if(!el || !counterEl) return;
  var total = window.bdGalleryCount||0;
  if(total <= 1) { counterEl.style.display='none'; return; }
  var idx = Math.round(el.scrollLeft / (el.offsetWidth||1)) + 1;
  idx = Math.max(1, Math.min(total, idx));
  counterEl.style.display = 'block';
  counterEl.textContent = idx+'/'+total;
}
function closeBuyerDetail() {"""
if old6 in content:
    content = content.replace(old6, new6, 1)
    fixes += 1
    print("Fix 6 done: updateImageCounter function added")
else:
    print("Fix 6 FAILED")

with open('/storage/emulated/0/OjaLive/index.html', 'w') as f:
    f.write(content)

print(f"\nTotal: {fixes}/6")

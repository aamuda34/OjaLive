with open('/storage/emulated/0/OjaLive/index.html', 'r') as f:
    content = f.read()

fixes = 0

# 1. Update Seller Info section - add follow button and follower count
old = '''        <div style="display:flex;align-items:center;gap:12px;">
          <div id="bd-seller-photo" style="width:48px;height:48px;border-radius:50%;background:var(--earth);color:#fff;font-size:20px;display:flex;align-items:center;justify-content:center;flex-shrink:0;"></div>
          <div>
            <div id="bd-trader" style="font-size:15px;font-weight:700;color:var(--dark);"></div>
            <div id="bd-location" style="font-size:12px;color:var(--muted);margin-top:2px;"></div>
            <div id="bd-hours" style="font-size:11px;color:var(--green);margin-top:2px;"></div>
            <div id="bd-dist" style="font-size:11px;color:var(--green);font-weight:600;margin-top:2px;"></div>
          </div>
        </div>'''

new = '''        <div style="display:flex;align-items:flex-start;gap:12px;">
          <div id="bd-seller-photo" style="width:54px;height:54px;border-radius:50%;background:var(--earth);color:#fff;font-size:22px;display:flex;align-items:center;justify-content:center;flex-shrink:0;"></div>
          <div style="flex:1;">
            <div style="display:flex;align-items:center;justify-content:space-between;">
              <div id="bd-trader" style="font-size:15px;font-weight:700;color:var(--dark);"></div>
              <button id="bd-follow-btn2" onclick="toggleFollow()" style="padding:7px 14px;background:var(--earth);color:#fff;border:none;border-radius:20px;font-size:12px;font-weight:700;cursor:pointer;">+ Follow</button>
            </div>
            <div id="bd-followers-count" style="font-size:11px;color:var(--muted);margin-top:2px;"></div>
            <div id="bd-location" style="font-size:12px;color:var(--muted);margin-top:2px;"></div>
            <div id="bd-hours" style="font-size:11px;color:var(--green);margin-top:2px;"></div>
            <div id="bd-dist" style="font-size:11px;color:var(--green);font-weight:600;margin-top:2px;"></div>
          </div>
        </div>'''

if old in content:
    content = content.replace(old, new)
    fixes += 1
    print("Fix 1 done: Follow button moved to Seller Info")
else:
    print("Fix 1 FAILED")

# 2. Remove old separate seller section with duplicate follow button
old2 = '''      <!-- SELLER RATING & FOLLOW -->
      <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px;margin-bottom:12px;">
        <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;margin-bottom:12px;">Seller</div>
        <div style="display:flex;align-items:center;justify-content:space-between;">
          <div style="display:flex;align-items:center;gap:10px;">
            <div id="bd-seller-photo2" style="width:44px;height:44px;border-radius:50%;background:var(--earth);color:#fff;font-size:18px;display:flex;align-items:center;justify-content:center;flex-shrink:0;"></div>
            <div>
              <div id="bd-seller-name2" style="font-size:14px;font-weight:700;color:var(--dark);"></div>
              <div id="bd-seller-avg-rating" style="font-size:12px;color:#F59E0B;margin-top:2px;"></div>
            </div>
          </div>
          <button id="bd-follow-btn" onclick="toggleFollow()" style="padding:8px 16px;background:var(--earth);color:#fff;border:none;border-radius:20px;font-size:12px;font-weight:700;cursor:pointer;">+ Follow</button>
        </div>
        <div style="margin-top:12px;border-top:1px solid var(--border);padding-top:12px;">
          <div style="font-size:12px;font-weight:600;color:var(--dark);margin-bottom:8px;">Rate this Seller</div>
          <div style="display:flex;gap:6px;margin-bottom:0;font-size:26px;">
            <span onclick="setSellerRating(1)" style="cursor:pointer;" class="seller-star">☆</span>
            <span onclick="setSellerRating(2)" style="cursor:pointer;" class="seller-star">☆</span>
            <span onclick="setSellerRating(3)" style="cursor:pointer;" class="seller-star">☆</span>
            <span onclick="setSellerRating(4)" style="cursor:pointer;" class="seller-star">☆</span>
            <span onclick="setSellerRating(5)" style="cursor:pointer;" class="seller-star">☆</span>
          </div>
          <button onclick="submitSellerRating()" style="width:100%;margin-top:10px;padding:10px;background:var(--dark);color:#fff;border:none;border-radius:10px;font-size:13px;font-weight:600;cursor:pointer;">Submit Rating</button>
        </div>
      </div>'''

new2 = '''      <!-- SELLER RATING -->
      <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px;margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
          <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;">Rate this Seller</div>
          <div id="bd-seller-avg-rating" style="font-size:13px;font-weight:700;color:#F59E0B;"></div>
        </div>
        <div style="display:flex;gap:6px;margin-bottom:0;font-size:28px;">
          <span onclick="setSellerRating(1)" style="cursor:pointer;" class="seller-star">☆</span>
          <span onclick="setSellerRating(2)" style="cursor:pointer;" class="seller-star">☆</span>
          <span onclick="setSellerRating(3)" style="cursor:pointer;" class="seller-star">☆</span>
          <span onclick="setSellerRating(4)" style="cursor:pointer;" class="seller-star">☆</span>
          <span onclick="setSellerRating(5)" style="cursor:pointer;" class="seller-star">☆</span>
        </div>
        <button onclick="submitSellerRating()" style="width:100%;margin-top:10px;padding:10px;background:var(--dark);color:#fff;border:none;border-radius:10px;font-size:13px;font-weight:600;cursor:pointer;">Submit Rating</button>
      </div>'''

if old2 in content:
    content = content.replace(old2, new2)
    fixes += 1
    print("Fix 2 done: duplicate seller section removed")
else:
    print("Fix 2 FAILED")

# 3. Update toggleFollow to use new button ID and update followers count
old3 = """function toggleFollow() {
  if (!currentDetailTrader) return;
  var key = 'following_'+currentDetailTrader;
  var btn = document.getElementById('bd-follow-btn');
  if (localStorage.getItem(key)) {
    localStorage.removeItem(key);
    btn.textContent = '+ Follow';
    btn.style.background = 'var(--earth)';
    showToast('Unfollowed '+currentDetailTrader);
  } else {
    localStorage.setItem(key,'1');
    btn.textContent = '✓ Following';
    btn.style.background = 'var(--green)';
    showToast('Following '+currentDetailTrader+'!');
  }
}"""

new3 = """async function toggleFollow() {
  if (!currentDetailTrader) return;
  var key = 'following_'+currentDetailTrader;
  var btn = document.getElementById('bd-follow-btn2');
  var countEl = document.getElementById('bd-followers-count');
  if (localStorage.getItem(key)) {
    localStorage.removeItem(key);
    if(btn){btn.textContent='+ Follow';btn.style.background='var(--earth)';}
    var r = await db.from('traders').select('followers_count').eq('full_name',currentDetailTrader).single();
    var cur = (r.data&&r.data.followers_count)||0;
    await db.from('traders').update({followers_count:Math.max(0,cur-1)}).eq('full_name',currentDetailTrader);
    if(countEl) countEl.textContent = Math.max(0,cur-1)+' followers';
    showToast('Unfollowed '+currentDetailTrader);
  } else {
    localStorage.setItem(key,'1');
    if(btn){btn.textContent='\u2713 Following';btn.style.background='var(--green)';}
    var r = await db.from('traders').select('followers_count').eq('full_name',currentDetailTrader).single();
    var cur = (r.data&&r.data.followers_count)||0;
    await db.from('traders').update({followers_count:cur+1}).eq('full_name',currentDetailTrader);
    if(countEl) countEl.textContent = (cur+1)+' followers';
    showToast('Following '+currentDetailTrader+'!');
  }
}"""

if old3 in content:
    content = content.replace(old3, new3)
    fixes += 1
    print("Fix 3 done: toggleFollow updates DB follower count")
else:
    print("Fix 3 FAILED")

# 4. Update openBuyerDetail to set follow state on new button and load followers
old4 = """  var followBtn = document.getElementById('bd-follow-btn');
  if(followBtn){
    var isFollowing = localStorage.getItem('following_'+item.trader);
    followBtn.textContent = isFollowing ? '✓ Following' : '+ Follow';
    followBtn.style.background = isFollowing ? 'var(--green)' : 'var(--earth)';
  }
  var sn2 = document.getElementById('bd-seller-name2');
  if(sn2) sn2.textContent = item.trader;
  var sp2 = document.getElementById('bd-seller-photo2');
  if(sp2) sp2.textContent = item.trader.charAt(0).toUpperCase();"""

new4 = """  var followBtn2 = document.getElementById('bd-follow-btn2');
  if(followBtn2){
    var isFollowing = localStorage.getItem('following_'+item.trader);
    followBtn2.textContent = isFollowing ? '\u2713 Following' : '+ Follow';
    followBtn2.style.background = isFollowing ? 'var(--green)' : 'var(--earth)';
  }"""

if old4 in content:
    content = content.replace(old4, new4)
    fixes += 1
    print("Fix 4 done: openBuyerDetail uses new follow button")
else:
    print("Fix 4 FAILED")

# 5. Load follower count when seller data loads
old5 = """      if(selResult.data.photo_url){
        sellerPhotoEl.innerHTML='<img src="'+selResult.data.photo_url+'" style="width:48px;height:48px;border-radius:50%;object-fit:cover;">';
        var sp2=document.getElementById('bd-seller-photo2');
        if(sp2) sp2.innerHTML='<img src="'+selResult.data.photo_url+'" style="width:44px;height:44px;border-radius:50%;object-fit:cover;">';
      }"""

new5 = """      if(selResult.data.photo_url){
        sellerPhotoEl.innerHTML='<img src="'+selResult.data.photo_url+'" style="width:54px;height:54px;border-radius:50%;object-fit:cover;">';
      }
      var fCount = selResult.data.followers_count||0;
      var countEl = document.getElementById('bd-followers-count');
      if(countEl) countEl.textContent = fCount+' follower'+(fCount!==1?'s':'');"""

if old5 in content:
    content = content.replace(old5, new5)
    fixes += 1
    print("Fix 5 done: follower count loaded from DB")
else:
    print("Fix 5 FAILED")

with open('/storage/emulated/0/OjaLive/index.html', 'w') as f:
    f.write(content)

print(f"\nTotal: {fixes}/5")

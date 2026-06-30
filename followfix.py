f = open('index.html', 'r')
html = f.read()
f.close()

old = """async function toggleFollow() {
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
    if(btn){btn.textContent='✓ Following';btn.style.background='var(--green)';}
    var r = await db.from('traders').select('followers_count').eq('full_name',currentDetailTrader).single();
    var cur = (r.data&&r.data.followers_count)||0;
    await db.from('traders').update({followers_count:cur+1}).eq('full_name',currentDetailTrader);
    if(countEl) countEl.textContent = (cur+1)+' followers';
    showToast('Following '+currentDetailTrader+'!');
  }
}"""

new = """async function toggleFollow() {
  if (!currentDetailTrader) return;
  var key = 'following_'+currentDetailTrader;
  var btn = document.getElementById('bd-follow-btn2');
  var countEl = document.getElementById('bd-followers-count');
  var r = await db.from('traders').select('followers_count').eq('full_name',currentDetailTrader).single();
  if (r.error || !r.data) { showToast('Could not update follow status'); return; }
  var cur = r.data.followers_count || 0;
  if (localStorage.getItem(key)) {
    var newCount = Math.max(0, cur-1);
    var upd = await db.from('traders').update({followers_count:newCount}).eq('full_name',currentDetailTrader);
    if (upd.error) { showToast('Error updating follow status'); return; }
    localStorage.removeItem(key);
    if(btn){btn.textContent='+ Follow';btn.style.background='var(--earth)';}
    if(countEl) countEl.textContent = newCount+' follower'+(newCount!==1?'s':'');
    showToast('Unfollowed '+currentDetailTrader);
  } else {
    var newCount = cur+1;
    var upd = await db.from('traders').update({followers_count:newCount}).eq('full_name',currentDetailTrader);
    if (upd.error) { showToast('Error updating follow status'); return; }
    localStorage.setItem(key,'1');
    if(btn){btn.textContent='✓ Following';btn.style.background='var(--green)';}
    if(countEl) countEl.textContent = newCount+' follower'+(newCount!==1?'s':'');
    showToast('Following '+currentDetailTrader+'!');
  }
}"""

if old in html:
    html = html.replace(old, new)
    print('toggleFollow fixed')
else:
    print('ERROR: pattern not found')

f = open('index.html', 'w')
f.write(html)
f.close()

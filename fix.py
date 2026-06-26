with open('/storage/emulated/0/OjaLive/index.html', 'r') as f:
    content = f.read()

# 1. Fix loadListings - move event listeners to initDB, not loadListings
old = """async function loadListings() {
  try {
    var result = await db.from('Listing').select('*').eq('verified', true);
    if (result.error) { showToast('Error: '+result.error.message); return; }
    allListings = result.data || [];
    document.getElementById('filter-city').addEventListener('change', renderBoard);
  setTimeout(function() {
    var btn = document.getElementById('btn-use-location');
    if (btn) btn.click();
  }, 800);
    document.getElementById('filter-category').addEventListener('change', renderBoard);
    renderBoard();
  } catch(e) {
    showToast('Fatal error: '+e.message);
  }
}"""

new = """async function loadListings() {
  try {
    var result = await db.from('Listing').select('*').eq('verified', true);
    if (result.error) { showToast('Error: '+result.error.message); return; }
    allListings = result.data || [];
    renderBoard();
  } catch(e) {
    showToast('Fatal error: '+e.message);
  }
}"""

if old in content:
    content = content.replace(old, new)
    print("Step 1 done: loadListings cleaned up")
else:
    print("Step 1 FAILED")

# 2. Move filter listeners and location trigger to initDB
old2 = "  loadListings();\n  restoreSellerSession();\n}"
new2 = """  loadListings();
  restoreSellerSession();
  document.getElementById('filter-city').addEventListener('change', renderBoard);
  document.getElementById('filter-category').addEventListener('change', renderBoard);
  setTimeout(function() {
    var btn = document.getElementById('btn-use-location');
    if (btn) btn.click();
  }, 1200);
}"""

if old2 in content:
    content = content.replace(old2, new2)
    print("Step 2 done: listeners moved to initDB")
else:
    print("Step 2 FAILED")

# 3. Fix restoreSellerSession - switch to Sell tab automatically
old3 = """async function restoreSellerSession() {
  var saved = localStorage.getItem('ojalive_seller');
  if (!saved) return;
  try {
    var seller = JSON.parse(saved);
    var result = await db.from('traders').select('*').eq('id',seller.id).single();
    if (result.error||!result.data) { localStorage.removeItem('ojalive_seller'); return; }
    currentSeller = result.data;
    document.getElementById('seller-shop-name').textContent = result.data.full_name;
    sellerShowScreen('seller-dashboard');
    loadSellerDashboard();
  } catch(e) { localStorage.removeItem('ojalive_seller'); }
}"""

new3 = """async function restoreSellerSession() {
  var saved = localStorage.getItem('ojalive_seller');
  if (!saved) return;
  try {
    var seller = JSON.parse(saved);
    var result = await db.from('traders').select('*').eq('id',seller.id).single();
    if (result.error||!result.data) { localStorage.removeItem('ojalive_seller'); return; }
    currentSeller = result.data;
    document.getElementById('seller-shop-name').textContent = result.data.full_name;
    switchTab('supplier');
    sellerShowScreen('seller-dashboard');
    loadSellerDashboard();
  } catch(e) { localStorage.removeItem('ojalive_seller'); }
}"""

if old3 in content:
    content = content.replace(old3, new3)
    print("Step 3 done: restoreSellerSession switches to Sell tab")
else:
    print("Step 3 FAILED")

with open('/storage/emulated/0/OjaLive/index.html', 'w') as f:
    f.write(content)

print("All done!")

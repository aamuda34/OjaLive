with open('/storage/emulated/0/OjaLive/index.html', 'r') as f:
    content = f.read()

fixes = 0

# 1. Fix duplicate IDs in Edit Item form
old = """      <label>Location</label>
      <input type="text" id="edit-item-location" placeholder="Location">
      <label>Item Description (Optional)</label>
      <textarea id="add-item-description" placeholder="Describe your item... e.g. Fresh from farm, quality guaranteed, wholesale available" style="width:100%;padding:12px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;resize:none;height:80px;font-family:inherit;margin-bottom:0;"></textarea>
      <label>Stock Quantity (Optional)</label>
      <input type="number" id="add-item-stock" placeholder="e.g. 50 (how many units available)" min="0">
      <label>Item Photos (Optional)</label>
      <div id="edit-images-preview" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:8px;"></div>"""
new = """      <label>Location</label>
      <input type="text" id="edit-item-location" placeholder="Location">
      <label>Item Description (Optional)</label>
      <textarea id="edit-item-description" placeholder="Describe your item... e.g. Fresh from farm, quality guaranteed, wholesale available" style="width:100%;padding:12px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;resize:none;height:80px;font-family:inherit;margin-bottom:0;"></textarea>
      <label>Stock Quantity (Optional)</label>
      <input type="number" id="edit-item-stock" placeholder="e.g. 50 (how many units available)" min="0">
      <label>Item Photos (Optional)</label>
      <div id="edit-images-preview" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:8px;"></div>"""
if old in content:
    content = content.replace(old, new)
    fixes += 1
    print("Fix 1 done: duplicate IDs fixed in Edit form")
else:
    print("Fix 1 FAILED")

# 2. Prefill description/stock + reset photo state on edit screen open
old2 = """async function sellerEditListingScreen(id) {
  var result = await db.from('Listing').select('*').eq('id',id).single();
  if (result.error||!result.data) { showToast('Item not found'); return; }
  var item = result.data;
  currentEditingListingId = item.id;
  document.getElementById('edit-item-name').value = item.name;
  document.getElementById('edit-item-price').value = item.price;
  document.getElementById('edit-item-unit').value = item.unit;
  document.getElementById('edit-item-location').value = item.location;
  document.getElementById('edit-item-category').value = item.category;
  var editPreview = document.getElementById('edit-images-preview');
  editPreview.innerHTML = '';
  if (item.image_url) {
    try {
      var imgs = JSON.parse(item.image_url);
      imgs.forEach(function(url) {
        var div = document.createElement('div');
        div.style.cssText = 'width:70px;height:70px;border-radius:8px;overflow:hidden;border:1.5px solid var(--border);';
        div.innerHTML = '<img src="'+url+'" style="width:100%;height:100%;object-fit:cover;">';
        editPreview.appendChild(div);
      });
    } catch(e) {}
  }
  sellerShowScreen('seller-edit-listing');
}"""
new2 = """async function sellerEditListingScreen(id) {
  var result = await db.from('Listing').select('*').eq('id',id).single();
  if (result.error||!result.data) { showToast('Item not found'); return; }
  var item = result.data;
  currentEditingListingId = item.id;
  document.getElementById('edit-item-name').value = item.name;
  document.getElementById('edit-item-price').value = item.price;
  document.getElementById('edit-item-unit').value = item.unit;
  document.getElementById('edit-item-location').value = item.location;
  document.getElementById('edit-item-category').value = item.category;
  document.getElementById('edit-item-description').value = item.description || '';
  document.getElementById('edit-item-stock').value = item.stock || '';
  photoFiles.edit = [];
  document.getElementById('edit-item-images').value = '';
  var editBgTools = document.getElementById('edit-bg-tools');
  if (editBgTools) editBgTools.style.display = 'none';
  var editUploadProgress = document.getElementById('edit-upload-progress');
  if (editUploadProgress) editUploadProgress.style.display = 'none';
  var editPreview = document.getElementById('edit-images-preview');
  editPreview.innerHTML = '';
  if (item.image_url) {
    try {
      var imgs = JSON.parse(item.image_url);
      imgs.forEach(function(url) {
        var div = document.createElement('div');
        div.style.cssText = 'width:70px;height:70px;border-radius:8px;overflow:hidden;border:1.5px solid var(--border);';
        div.innerHTML = '<img src="'+url+'" style="width:100%;height:100%;object-fit:cover;">';
        editPreview.appendChild(div);
      });
    } catch(e) {}
  }
  sellerShowScreen('seller-edit-listing');
}"""
if old2 in content:
    content = content.replace(old2, new2)
    fixes += 1
    print("Fix 2 done: edit screen prefills description/stock, resets photo state")
else:
    print("Fix 2 FAILED")

# 3. Save description/stock on edit, clear stale photoFiles.edit after save
old3 = """async function sellerSaveEditListing() {
  if (!currentEditingListingId) { showToast('No item selected'); return; }
  var name = document.getElementById('edit-item-name').value.trim();
  var price = parseFloat(document.getElementById('edit-item-price').value);
  var unit = document.getElementById('edit-item-unit').value.trim();
  var category = document.getElementById('edit-item-category').value;
  var location = document.getElementById('edit-item-location').value.trim();
  if (!name||!price||!unit) { showToast('Fill all fields'); return; }
  if (!location) location = currentSeller.location || '';
  var oldItem = await db.from('Listing').select('price').eq('id',currentEditingListingId).single();
  var oldPrice = oldItem.data ? oldItem.data.price : null;
  var changeDir = 'stable';
  if (oldPrice && price > oldPrice) changeDir = 'up';
  if (oldPrice && price < oldPrice) changeDir = 'down';
  var result = await db.from('Listing').update({name:name,price:price,unit:unit,category:category,location:location,change:changeDir}).eq('id',currentEditingListingId);
  if (result.error) { showToast('Error: '+result.error.message); return; }
  if (oldPrice && oldPrice !== price) {
    await db.from('price_history').insert([{listing_id:currentEditingListingId,old_price:oldPrice,new_price:price,trader:currentSeller.full_name,location:currentSeller.location}]);
  }
  var editImgFiles = photoFiles.edit;
  if (editImgFiles.length > 0) {
    var editUrls = await uploadImagesWithProgress(editImgFiles, currentEditingListingId, 'edit');
    if (editUrls.length > 0) {
      await db.from('Listing').update({image_url:JSON.stringify(editUrls)}).eq('id',currentEditingListingId);
    }
  }
  showToast('Item updated!');
  loadSellerDashboard();
  loadListings();
  sellerShowScreen('seller-dashboard');
}"""
new3 = """async function sellerSaveEditListing() {
  if (!currentEditingListingId) { showToast('No item selected'); return; }
  var name = document.getElementById('edit-item-name').value.trim();
  var price = parseFloat(document.getElementById('edit-item-price').value);
  var unit = document.getElementById('edit-item-unit').value.trim();
  var category = document.getElementById('edit-item-category').value;
  var location = document.getElementById('edit-item-location').value.trim();
  var description = document.getElementById('edit-item-description').value.trim();
  var stock = document.getElementById('edit-item-stock').value ? parseInt(document.getElementById('edit-item-stock').value) : null;
  if (!name||!price||!unit) { showToast('Fill all fields'); return; }
  if (!location) location = currentSeller.location || '';
  var oldItem = await db.from('Listing').select('price').eq('id',currentEditingListingId).single();
  var oldPrice = oldItem.data ? oldItem.data.price : null;
  var changeDir = 'stable';
  if (oldPrice && price > oldPrice) changeDir = 'up';
  if (oldPrice && price < oldPrice) changeDir = 'down';
  var result = await db.from('Listing').update({name:name,price:price,unit:unit,category:category,location:location,change:changeDir,description:description,stock:stock}).eq('id',currentEditingListingId);
  if (result.error) { showToast('Error: '+result.error.message); return; }
  if (oldPrice && oldPrice !== price) {
    await db.from('price_history').insert([{listing_id:currentEditingListingId,old_price:oldPrice,new_price:price,trader:currentSeller.full_name,location:currentSeller.location}]);
  }
  var editImgFiles = photoFiles.edit;
  if (editImgFiles.length > 0) {
    var editUrls = await uploadImagesWithProgress(editImgFiles, currentEditingListingId, 'edit');
    if (editUrls.length > 0) {
      await db.from('Listing').update({image_url:JSON.stringify(editUrls)}).eq('id',currentEditingListingId);
    }
  }
  photoFiles.edit = [];
  showToast('Item updated!');
  loadSellerDashboard();
  loadListings();
  sellerShowScreen('seller-dashboard');
}"""
if old3 in content:
    content = content.replace(old3, new3)
    fixes += 1
    print("Fix 3 done: edit save now persists description/stock, clears stale photos")
else:
    print("Fix 3 FAILED")

# 4. Reset Add Item screen state fully on open
old4 = """function sellerAddListingScreen() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function(pos) { showToast('📍 GPS ready for your listing'); },
      function() { showToast('Enable GPS for exact location'); },
      { enableHighAccuracy:true, timeout:8000 }
    );
  }
  document.getElementById('add-item-name').value='';
  document.getElementById('add-item-price').value='';
  document.getElementById('add-item-unit').value='';
  document.getElementById('add-item-location').value=currentSeller.location;
  document.getElementById('add-item-location').style.display='none';
  document.querySelector('label[for="add-item-location"]') && (document.querySelector('label[for="add-item-location"]').style.display='none');
  sellerShowScreen('seller-add-listing');
}"""
new4 = """function sellerAddListingScreen() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function(pos) { showToast('📍 GPS ready for your listing'); },
      function() { showToast('Enable GPS for exact location'); },
      { enableHighAccuracy:true, timeout:8000 }
    );
  }
  document.getElementById('add-item-name').value='';
  document.getElementById('add-item-price').value='';
  document.getElementById('add-item-unit').value='';
  document.getElementById('add-item-location').value=currentSeller.location;
  document.getElementById('add-item-location').style.display='none';
  document.getElementById('add-item-description').value='';
  document.getElementById('add-item-stock').value='';
  document.getElementById('add-show-phone').checked = true;
  photoFiles.add = [];
  document.getElementById('add-item-images').value = '';
  document.getElementById('add-images-preview').innerHTML = '';
  var addBgTools = document.getElementById('add-bg-tools');
  if (addBgTools) addBgTools.style.display = 'none';
  var addUploadProgress = document.getElementById('add-upload-progress');
  if (addUploadProgress) addUploadProgress.style.display = 'none';
  sellerShowScreen('seller-add-listing');
}"""
if old4 in content:
    content = content.replace(old4, new4)
    fixes += 1
    print("Fix 4 done: Add Item screen fully resets on open")
else:
    print("Fix 4 FAILED")

# 5. Clear stale photoFiles.add after successful post
old5 = """  if (result.error) { showToast('Error: '+result.error.message); return; }
  showToast('Item posted!');
  loadSellerDashboard();
  loadListings();
  sellerShowScreen('seller-dashboard');
}
async function sellerEditListingScreen(id) {"""
new5 = """  if (result.error) { showToast('Error: '+result.error.message); return; }
  photoFiles.add = [];
  showToast('Item posted!');
  loadSellerDashboard();
  loadListings();
  sellerShowScreen('seller-dashboard');
}
async function sellerEditListingScreen(id) {"""
if old5 in content:
    content = content.replace(old5, new5)
    fixes += 1
    print("Fix 5 done: photoFiles.add cleared after post")
else:
    print("Fix 5 FAILED")

# 6. Add description/stock display rows to seller item detail HTML
old6 = """      <div style="margin-top:14px;padding-top:14px;border-top:1px solid var(--border);">
        <div id="detail-location" style="font-size:13px;color:var(--dark);margin-bottom:6px;"></div>
        <div id="detail-trader" style="font-size:13px;color:var(--muted);"></div>
      </div>"""
new6 = """      <div style="margin-top:14px;padding-top:14px;border-top:1px solid var(--border);">
        <div id="detail-location" style="font-size:13px;color:var(--dark);margin-bottom:6px;"></div>
        <div id="detail-trader" style="font-size:13px;color:var(--muted);"></div>
      </div>
      <div id="detail-stock-row" style="display:none;margin-top:10px;">
        <span style="font-size:11px;background:#E8F5EE;color:var(--green);border:1px solid var(--green);border-radius:6px;padding:3px 10px;font-weight:600;" id="detail-stock"></span>
      </div>
      <div id="detail-desc-row" style="display:none;margin-top:12px;padding-top:12px;border-top:1px solid var(--border);">
        <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;margin-bottom:6px;">Description</div>
        <div id="detail-description" style="font-size:13px;color:var(--dark);line-height:1.6;"></div>
      </div>"""
if old6 in content:
    content = content.replace(old6, new6)
    fixes += 1
    print("Fix 6 done: description/stock rows added to item detail HTML")
else:
    print("Fix 6 FAILED")

# 7. Populate description/stock in sellerItemDetail JS
old7 = """  document.getElementById('detail-location').textContent = '📍 '+item.location;
  document.getElementById('detail-trader').textContent = '🏪 '+item.trader;"""
new7 = """  document.getElementById('detail-location').textContent = '📍 '+item.location;
  document.getElementById('detail-trader').textContent = '🏪 '+item.trader;
  var stockRow = document.getElementById('detail-stock-row');
  if (item.stock) {
    stockRow.style.display = 'block';
    document.getElementById('detail-stock').textContent = item.stock+' in stock';
  } else {
    stockRow.style.display = 'none';
  }
  var descRow = document.getElementById('detail-desc-row');
  if (item.description) {
    descRow.style.display = 'block';
    document.getElementById('detail-description').textContent = item.description;
  } else {
    descRow.style.display = 'none';
  }"""
if old7 in content:
    content = content.replace(old7, new7)
    fixes += 1
    print("Fix 7 done: item detail populates description/stock")
else:
    print("Fix 7 FAILED")

# 8. Include stock/description when duplicating
old8 = """      phone: item.phone,
      image_url: item.image_url
    }]);"""
new8 = """      phone: item.phone,
      image_url: item.image_url,
      stock: item.stock,
      description: item.description
    }]);"""
if old8 in content:
    content = content.replace(old8, new8)
    fixes += 1
    print("Fix 8 done: duplicate now copies stock/description")
else:
    print("Fix 8 FAILED")

# 9. Rename dashboard label to Inventory Value
old9 = """      <div class="card" style="text-align:center;padding:14px 8px;">
        <div style="font-family:'Syne',sans-serif;font-size:24px;font-weight:800;color:var(--green);" id="dashboard-total-value">₦0</div>
        <div style="font-size:11px;color:var(--muted);font-weight:600;">Total Value</div>
      </div>"""
new9 = """      <div class="card" style="text-align:center;padding:14px 8px;">
        <div style="font-family:'Syne',sans-serif;font-size:24px;font-weight:800;color:var(--green);" id="dashboard-total-value">₦0</div>
        <div style="font-size:11px;color:var(--muted);font-weight:600;">Inventory Value</div>
      </div>"""
if old9 in content:
    content = content.replace(old9, new9)
    fixes += 1
    print("Fix 9 done: dashboard label renamed")
else:
    print("Fix 9 FAILED")

# 10. Rename stats label to Inventory Value
old10 = """      <div class="card" style="text-align:center;padding:14px 8px;">
        <div style="font-family:'Syne',sans-serif;font-size:22px;font-weight:800;color:var(--green);" id="stats-total-value">₦0</div>
        <div style="font-size:11px;color:var(--muted);font-weight:600;">Total Value</div>
      </div>"""
new10 = """      <div class="card" style="text-align:center;padding:14px 8px;">
        <div style="font-family:'Syne',sans-serif;font-size:22px;font-weight:800;color:var(--green);" id="stats-total-value">₦0</div>
        <div style="font-size:11px;color:var(--muted);font-weight:600;">Inventory Value</div>
      </div>"""
if old10 in content:
    content = content.replace(old10, new10)
    fixes += 1
    print("Fix 10 done: stats label renamed")
else:
    print("Fix 10 FAILED")

# 11. Fix Inventory Value calc (dashboard) - price x stock
old11 = "  var total = listings.filter(function(l){return l.verified!==false;}).reduce(function(s,l){return s+Number(l.price);},0);"
new11 = "  var total = listings.filter(function(l){return l.verified!==false;}).reduce(function(s,l){return s+(Number(l.price)*(l.stock?Number(l.stock):1));},0);"
if old11 in content:
    content = content.replace(old11, new11)
    fixes += 1
    print("Fix 11 done: dashboard inventory value = price x stock")
else:
    print("Fix 11 FAILED")

# 12. Fix Inventory Value calc (stats) - price x stock
old12 = "  var total = active.reduce(function(s,l){return s+Number(l.price);},0);"
new12 = "  var total = active.reduce(function(s,l){return s+(Number(l.price)*(l.stock?Number(l.stock):1));},0);"
if old12 in content:
    content = content.replace(old12, new12)
    fixes += 1
    print("Fix 12 done: stats inventory value = price x stock")
else:
    print("Fix 12 FAILED")

# 13. Give status badge an id
old13 = '        <div style="margin-top:6px;"><span class="spill">✔ Verified Seller</span></div>'
new13 = '        <div style="margin-top:6px;" id="profile-status-badge"><span class="spill">✔ Verified Seller</span></div>'
if old13 in content:
    content = content.replace(old13, new13)
    fixes += 1
    print("Fix 13 done: status badge id added")
else:
    print("Fix 13 FAILED")

# 14. Wire status badge to real currentSeller.status
old14 = """  var hoursEl = document.getElementById('profile-opening-hours');
  if (hoursEl) hoursEl.textContent = currentSeller.opening_hours || 'Not set';"""
new14 = """  var hoursEl = document.getElementById('profile-opening-hours');
  if (hoursEl) hoursEl.textContent = currentSeller.opening_hours || 'Not set';
  var statusBadge = document.getElementById('profile-status-badge');
  if (statusBadge) {
    if (currentSeller.status === 'approved') {
      statusBadge.innerHTML = '<span class="spill">✔ Verified Seller</span>';
    } else if (currentSeller.status === 'rejected') {
      statusBadge.innerHTML = '<span class="spill" style="background:#FDECEA;color:var(--red);">✕ Not Approved</span>';
    } else {
      statusBadge.innerHTML = '<span class="spill" style="background:#FDF6E3;color:var(--amber);">⏳ Pending Review</span>';
    }
  }"""
if old14 in content:
    content = content.replace(old14, new14)
    fixes += 1
    print("Fix 14 done: status badge reflects real approval status")
else:
    print("Fix 14 FAILED")

with open('/storage/emulated/0/OjaLive/index.html', 'w') as f:
    f.write(content)

print(f"\nTotal: {fixes}/14")

with open('/storage/emulated/0/OjaLive/index.html', 'r') as f:
    content = f.read()

old = """  document.getElementById('edit-profile-lat').value = currentSeller.latitude || '';
  document.getElementById('edit-profile-lng').value = currentSeller.longitude || '';
  document.getElementById('update-location-status').textContent = currentSeller.location ? '\U0001f4cd Current: '+currentSeller.location : '';
  sellerShowScreen('seller-edit-profile');"""

new = """  document.getElementById('edit-profile-lat').value = currentSeller.latitude || '';
  document.getElementById('edit-profile-lng').value = currentSeller.longitude || '';
  document.getElementById('update-location-status').textContent = currentSeller.location ? '📍 Current: '+currentSeller.location : '';
  document.getElementById('edit-profile-description').value = currentSeller.description || '';
  var epPreview = document.getElementById('edit-profile-photo-preview');
  if (epPreview) {
    if (currentSeller.photo_url) {
      epPreview.innerHTML = '<img src="'+currentSeller.photo_url+'" style="width:80px;height:80px;border-radius:50%;object-fit:cover;border:3px solid var(--earth);display:block;margin:0 auto 8px;">';
    } else {
      epPreview.innerHTML = '<div style="width:80px;height:80px;border-radius:50%;background:var(--earth);color:#fff;font-size:28px;display:flex;align-items:center;justify-content:center;margin:0 auto 8px;">'+currentSeller.full_name.charAt(0).toUpperCase()+'</div>';
    }
  }
  sellerShowScreen('seller-edit-profile');"""

if old in content:
    content = content.replace(old, new)
    print("Done: edit profile pre-fills photo and description")
else:
    print("FAILED")

with open('/storage/emulated/0/OjaLive/index.html', 'w') as f:
    f.write(content)

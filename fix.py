with open('/storage/emulated/0/OjaLive/index.html', 'r') as f:
    content = f.read()

# 1. Auto-trigger location when Buy tab is clicked
old = "document.getElementById('tab-buyer').addEventListener('click', function() { switchTab('buyer'); });"
new = "document.getElementById('tab-buyer').addEventListener('click', function() { switchTab('buyer'); requestBuyerLocation(); });"

if old in content:
    content = content.replace(old, new)
    print("Step 1 done: auto location on Buy tab click")
else:
    print("Step 1 FAILED")

# 2. Auto-trigger GPS when seller opens Add Item screen
old2 = "function sellerAddListingScreen() {"
new2 = """function sellerAddListingScreen() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function(pos) { showToast('📍 GPS ready for your listing'); },
      function() { showToast('Enable GPS for exact location'); },
      { enableHighAccuracy:true, timeout:8000 }
    );
  }"""

if old2 in content:
    content = content.replace(old2, new2)
    print("Step 2 done: GPS prompt on Add Item screen")
else:
    print("Step 2 FAILED")

with open('/storage/emulated/0/OjaLive/index.html', 'w') as f:
    f.write(content)

print("All done!")

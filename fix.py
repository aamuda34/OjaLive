with open('/storage/emulated/0/OjaLive/index.html', 'r') as f:
    content = f.read()

old = "  var listingIds = [...new Set(changes.map(function(h){return h.listing_id;}))];"
new = "  var listingIds = changes.map(function(h){return h.listing_id;}).filter(function(v,i,a){return a.indexOf(v)===i;});"

if old in content:
    content = content.replace(old, new)
    print("Fixed: spread operator replaced with compatible code")
else:
    print("FAILED")

with open('/storage/emulated/0/OjaLive/index.html', 'w') as f:
    f.write(content)

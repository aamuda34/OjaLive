f = open('index.html', 'r')
html = f.read()
f.close()

old = """async function loadListings() {
  try {
    var result = await db.from('Listing').select('*');
    if (result.error) { showToast('Error: '+result.error.message); return; }
    allListings = result.data || [];
    renderBoard();
  } catch(e) {
    showToast('Fatal error: '+e.message);
  }
}"""

new = """async function loadListings() {
  try {
    var result = await db.from('Listing').select('*');
    if (result.error) { document.getElementById('board').innerHTML = '<div class=\"empty\">DB Error: '+result.error.message+'</div>'; return; }
    allListings = result.data || [];
    document.getElementById('count').textContent = allListings.length + ' Listings';
    document.getElementById('board').innerHTML = allListings.map(function(item) {
      return '<div class=\"price-item\"><div><div class=\"mname\">'+item.name+'</div><div class=\"munit\">'+item.unit+' · '+item.trader+' · '+item.location+'</div></div><div class=\"pright\"><div class=\"pval\">&#8358;'+Number(item.price).toLocaleString()+'</div><span class=\"pbadge stable\">Stable</span></div></div>';
    }).join('') || '<div class=\"empty\">No listings yet</div>';
  } catch(e) {
    document.getElementById('board').innerHTML = '<div class=\"empty\">Error: '+e.message+'</div>';
  }
}"""

if old in html:
    html = html.replace(old, new)
    print('Replaced successfully')
else:
    print('ERROR: Could not find the function to replace')

f = open('index.html', 'w')
f.write(html)
f.close()

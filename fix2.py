f = open('index.html', 'r')
html = f.read()
f.close()

html = html.replace(
"  document.getElementById('filter-city').addEventListener('change', renderBoard);\n  document.getElementById('filter-category').addEventListener('change', renderBoard);",
"  var fc = document.getElementById('filter-city');\n  var fk = document.getElementById('filter-category');\n  if (fc) fc.addEventListener('change', renderBoard);\n  if (fk) fk.addEventListener('change', renderBoard);"
)

html = html.replace(
"  document.getElementById('count').textContent = data.length + ' Listings';\n  if (!data.length) { document.getElementById('board').innerHTML = '<div class=\"empty\">No listings found</div>'; return; }",
"  document.getElementById('count').textContent = allListings.length + ' Listings';\n  if (!data.length) { document.getElementById('board').innerHTML = '<div class=\"empty\">No listings found for this filter</div>'; return; }"
)

f = open('index.html', 'w')
f.write(html)
f.close()
print('Done!')

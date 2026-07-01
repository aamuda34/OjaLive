f = open('index.html', 'r')
html = f.read()
f.close()
changes = 0

old = '<div style="font-family:\'Syne\',sans-serif;font-size:15px;font-weight:800;color:var(--dark);" id="count">0 Listings</div>'
new = '<div style="font-family:\'Syne\',sans-serif;font-size:15px;font-weight:800;color:var(--dark);" id="count">Finding prices near you...</div>'

if old in html:
    html = html.replace(old, new)
    changes += 1
    print('Loading label branded')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()
print('Done:', changes)

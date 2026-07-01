f = open('index.html', 'r')
html = f.read()
f.close()

old = '<div id="board" style="padding:14px;"><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">'

new = '<div id="board" style="padding:14px;"><div style="text-align:center;padding:24px 0 20px;"><div style="font-family:\'Syne\',sans-serif;font-size:20px;font-weight:800;color:#E5D9C8;letter-spacing:0.5px;animation:skeleton-pulse 1.8s ease-in-out infinite;">Oja<span style="color:#D4A876;">Live</span></div></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">'

count = html.count(old)
print('Found', count, 'matches')

if count == 1:
    html = html.replace(old, new)
    print('Branded skeleton header added')
else:
    print('SKIP - expected exactly 1 match')

f = open('index.html', 'w')
f.write(html)
f.close()

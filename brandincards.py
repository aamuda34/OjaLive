f = open('index.html', 'r')
html = f.read()
f.close()

# Remove the separate header we added
old_header = '<div style="text-align:center;padding:24px 0 20px;"><div style="font-family:\'Syne\',sans-serif;font-size:20px;font-weight:800;color:#E5D9C8;letter-spacing:0.5px;animation:skeleton-pulse 1.8s ease-in-out infinite;">Oja<span style="color:#D4A876;">Live</span></div></div>'

if old_header in html:
    html = html.replace(old_header, '')
    print('1. Removed separate header')
else:
    print('1. SKIP - header not found')

# Replace the plain skeleton image block with one that has OjaLive watermark centered inside it
old_img_skel = '<div class="skeleton" style="width:100%;height:200px;"></div>'
new_img_skel = '<div class="skeleton" style="width:100%;height:200px;display:flex;align-items:center;justify-content:center;"><span style="font-family:\'Syne\',sans-serif;font-size:15px;font-weight:800;color:rgba(196,97,42,0.18);letter-spacing:0.5px;">OjaLive</span></div>'

count = html.count(old_img_skel)
print('Found', count, 'skeleton image blocks')
if count > 0:
    html = html.replace(old_img_skel, new_img_skel)
    print('2. OjaLive watermark added inside', count, 'skeleton cards')
else:
    print('2. SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

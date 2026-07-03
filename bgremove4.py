f = open('index.html', 'r')
html = f.read()
f.close()

old = "</style>"
new = "@keyframes spin{to{transform:rotate(360deg);}}\n</style>"

if old in html:
    html = html.replace(old, new, 1)
    print('Spinner animation added')
else:
    print('SKIP')

f = open('index.html', 'w')
f.write(html)
f.close()

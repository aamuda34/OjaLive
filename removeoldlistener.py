f = open('index.html', 'r')
html = f.read()
f.close()

old = "    document.getElementById('btn-register-seller').addEventListener('click', sellerRegister);\n"
new = ""

if old in html:
    html = html.replace(old, new)
    print('Removed duplicate event listener bypassing validation')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

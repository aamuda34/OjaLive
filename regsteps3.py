f = open('index.html', 'r')
html = f.read()
f.close()

old = """        <input type="tel" id="reg-phone" placeholder="080xxxxxxxx">
        <label>Country</label>"""

new = """        <input type="tel" id="reg-phone" placeholder="080xxxxxxxx">
        <button type="button" class="btn btn-p" onclick="regGoToStep(2)" style="margin-top:16px;">Continue</button>
        </div>
        <div id="reg-step-2" class="hidden">
        <label>Country</label>"""

if old in html:
    html = html.replace(old, new)
    print('1. Step 1 to Step 2 boundary added')
else:
    print('1. SKIP')

f = open('index.html', 'w')
f.write(html)
f.close()

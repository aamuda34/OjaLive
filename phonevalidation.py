f = open('index.html', 'r')
html = f.read()
f.close()

old = """  if (!phone) { errEl.textContent = 'Please enter your phone number'; errEl.style.display = 'block'; return; }
  if (phone.length < 10) { errEl.textContent = 'Please enter a valid phone number'; errEl.style.display = 'block'; return; }"""

new = """  if (!phone) { errEl.textContent = 'Please enter your phone number'; errEl.style.display = 'block'; return; }
  var phoneDigits = phone.replace(/\\D/g,'');
  var validNigerian = /^0[789][01]\\d{8}$/.test(phoneDigits);
  if (!validNigerian) { errEl.textContent = 'Please enter a valid Nigerian phone number (e.g. 08012345678)'; errEl.style.display = 'block'; return; }"""

if old in html:
    html = html.replace(old, new)
    print('Nigerian phone format validation added')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

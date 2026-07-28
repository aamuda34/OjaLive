f = open('index.html', 'r')
html = f.read()
f.close()

old = """  if (!name||!phone||!password) { showToast('Fill all fields'); return; }
  if (!document.getElementById('reg-lat').value) { showToast('Please capture your shop location first'); return; }
  if (password.length < 6) { showToast('Password must be 6+ characters'); return; }"""

new = """  if (!name||!phone||!password) { showToast('Fill all fields'); return; }
  if (!document.getElementById('reg-lat').value) { showToast('Please capture your shop location first'); return; }
  if (password.length < 6) { showToast('Password must be 6+ characters'); return; }
  var existingCheck = await db.from('traders').select('id').eq('phone',phone);
  if (existingCheck.data && existingCheck.data.length > 0) { showToast('This phone number is already registered. Please login instead.'); return; }"""

if old in html:
    html = html.replace(old, new)
    print('Duplicate phone check added')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

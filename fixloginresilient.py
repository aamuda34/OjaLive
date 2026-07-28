f = open('index.html', 'r')
html = f.read()
f.close()

old = """async function sellerLogin() {
  var phone = document.getElementById('login-phone').value.trim();
  var password = document.getElementById('login-password').value.trim();
  if (!phone||!password) { showToast('Enter phone and password'); return; }
  if (!db) { showToast('App still loading, please wait'); return; }
  var result = await db.from('traders').select('*').eq('phone',phone).eq('password',password).single();
  if (result.error||!result.data) { showToast('Wrong phone or password'); return; }
  currentSeller = result.data;"""

new = """async function sellerLogin() {
  var phone = document.getElementById('login-phone').value.trim();
  var password = document.getElementById('login-password').value.trim();
  if (!phone||!password) { showToast('Enter phone and password'); return; }
  if (!db) { showToast('App still loading, please wait'); return; }
  var result = await db.from('traders').select('*').eq('phone',phone).eq('password',password).order('created_at',{ascending:false}).limit(1);
  if (result.error || !result.data || result.data.length === 0) { showToast('Wrong phone or password'); return; }
  currentSeller = result.data[0];"""

if old in html:
    html = html.replace(old, new)
    print('Login made resilient to duplicates')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

f = open('index.html', 'r')
html = f.read()
f.close()

old = "async function sellerRegister() {"
new = """function switchAuthTab(tab) {
  var loginPanel = document.getElementById('auth-panel-login');
  var registerPanel = document.getElementById('auth-panel-register');
  var loginTab = document.getElementById('auth-tab-login');
  var registerTab = document.getElementById('auth-tab-register');
  if (tab === 'login') {
    loginPanel.classList.remove('hidden');
    registerPanel.classList.add('hidden');
    loginTab.style.background = 'var(--dark)';
    loginTab.style.color = '#fff';
    registerTab.style.background = 'transparent';
    registerTab.style.color = 'var(--muted)';
  } else {
    registerPanel.classList.remove('hidden');
    loginPanel.classList.add('hidden');
    registerTab.style.background = 'var(--dark)';
    registerTab.style.color = '#fff';
    loginTab.style.background = 'transparent';
    loginTab.style.color = 'var(--muted)';
  }
}
async function sellerRegister() {"""

if old in html:
    html = html.replace(old, new, 1)
    print('switchAuthTab function added')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

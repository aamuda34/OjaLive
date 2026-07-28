f = open('index.html', 'r')
html = f.read()
f.close()

old = """  if (tab === 'login') {
    loginPanel.classList.remove('hidden');
    registerPanel.classList.add('hidden');"""

new = """  var successPanel = document.getElementById('auth-panel-success');
  if (successPanel) successPanel.classList.add('hidden');
  if (tab === 'login') {
    loginPanel.classList.remove('hidden');
    registerPanel.classList.add('hidden');"""

if old in html:
    html = html.replace(old, new)
    print('Success panel now hides on tab switch')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

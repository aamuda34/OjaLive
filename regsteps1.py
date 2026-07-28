f = open('index.html', 'r')
html = f.read()
f.close()

old = "function switchAuthTab(tab) {"
new = """function regGoToStep(step) {
  [1,2,3].forEach(function(s) {
    document.getElementById('reg-step-'+s).classList.toggle('hidden', s !== step);
    document.getElementById('reg-progress-'+s).style.background = (s <= step) ? 'var(--earth)' : 'var(--border)';
  });
  document.getElementById('reg-step-label').textContent = 'Step '+step+' of 3';
}
function switchAuthTab(tab) {"""

if old in html:
    html = html.replace(old, new, 1)
    print('regGoToStep function added')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

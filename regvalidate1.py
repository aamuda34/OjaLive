f = open('index.html', 'r')
html = f.read()
f.close()

old = """        <button type=\"button\" class=\"btn btn-p\" onclick=\"regGoToStep(2)\" style=\"margin-top:16px;\">Continue</button>
        </div>"""

new = """        <div id=\"reg-step1-error\" style=\"color:#C0392B;font-size:12px;margin-top:8px;display:none;\"></div>
        <button type=\"button\" class=\"btn btn-p\" onclick=\"regValidateStep1()\" style=\"margin-top:16px;\">Continue</button>
        </div>"""

if old in html:
    html = html.replace(old, new, 1)
    print('1. Step 1 button updated to call validation')
else:
    print('1. SKIP')

old2 = "function regGoToStep(step) {"
new2 = """async function regValidateStep1() {
  var errEl = document.getElementById('reg-step1-error');
  errEl.style.display = 'none';
  var name = document.getElementById('reg-name').value.trim();
  var phone = document.getElementById('reg-phone').value.trim();
  if (!name) { errEl.textContent = 'Please enter your shop name'; errEl.style.display = 'block'; return; }
  if (!phone) { errEl.textContent = 'Please enter your phone number'; errEl.style.display = 'block'; return; }
  if (phone.length < 10) { errEl.textContent = 'Please enter a valid phone number'; errEl.style.display = 'block'; return; }
  errEl.textContent = 'Checking phone number...';
  errEl.style.color = 'var(--muted)';
  errEl.style.display = 'block';
  var check = await db.from('traders').select('id').eq('phone', phone);
  if (check.data && check.data.length > 0) {
    errEl.textContent = 'This phone number is already registered. Please login instead.';
    errEl.style.color = '#C0392B';
    return;
  }
  errEl.style.display = 'none';
  regGoToStep(2);
}
function regGoToStep(step) {"""

if old2 in html:
    html = html.replace(old2, new2, 1)
    print('2. regValidateStep1 function added')
else:
    print('2. SKIP')

f = open('index.html', 'w')
f.write(html)
f.close()

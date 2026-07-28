f = open('index.html', 'r')
html = f.read()
f.close()

old = "function regGoToStep(step) {"
new = """function togglePasswordVisibility(fieldId, btn) {
  var field = document.getElementById(fieldId);
  if (field.type === 'password') {
    field.type = 'text';
    btn.style.color = 'var(--earth)';
  } else {
    field.type = 'password';
    btn.style.color = 'var(--muted)';
  }
}
function checkPasswordStrength() {
  var pw = document.getElementById('reg-password').value;
  var bar = document.getElementById('reg-password-strength-bar');
  var label = document.getElementById('reg-password-strength-label');
  var score = 0;
  if (pw.length >= 6) score++;
  if (pw.length >= 9) score++;
  if (/[A-Z]/.test(pw) && /[a-z]/.test(pw)) score++;
  if (/[0-9]/.test(pw)) score++;
  if (!pw) { bar.style.width = '0%'; label.textContent = ''; return; }
  if (score <= 1) { bar.style.width = '33%'; bar.style.background = '#C0392B'; label.textContent = 'Weak password'; label.style.color = '#C0392B'; }
  else if (score <= 2) { bar.style.width = '66%'; bar.style.background = '#D4A017'; label.textContent = 'Medium strength'; label.style.color = '#D4A017'; }
  else { bar.style.width = '100%'; bar.style.background = '#2D7A4F'; label.textContent = 'Strong password'; label.style.color = '#2D7A4F'; }
}
function regValidateStep3() {
  var errEl = document.getElementById('reg-step3-error');
  var pw = document.getElementById('reg-password').value;
  var pwConfirm = document.getElementById('reg-password-confirm').value;
  var trade = document.getElementById('reg-trade').value;
  if (!pw) { errEl.textContent = 'Please enter a password'; errEl.style.display = 'block'; return; }
  if (pw.length < 6) { errEl.textContent = 'Password must be at least 6 characters'; errEl.style.display = 'block'; return; }
  if (!pwConfirm) { errEl.textContent = 'Please confirm your password'; errEl.style.display = 'block'; return; }
  if (pw !== pwConfirm) { errEl.textContent = 'Passwords do not match'; errEl.style.display = 'block'; return; }
  if (!document.getElementById('reg-terms-check').checked) { errEl.textContent = 'Please agree to the Terms of Service to continue'; errEl.style.display = 'block'; return; }
  errEl.style.display = 'none';
  sellerRegister();
}
function regGoToStep(step) {"""

if old in html:
    html = html.replace(old, new, 1)
    print('Password strength, visibility toggle, and step 3 validation added')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

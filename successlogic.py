f = open('index.html', 'r')
html = f.read()
f.close()

old = """  if (result.error) { showToast('Register Error: '+result.error.message); return; }
  showToast('Account created! Login now.');
  document.getElementById('reg-name').value='';
  document.getElementById('reg-phone').value='';
  document.getElementById('reg-location').value='';
  document.getElementById('reg-lat').value='';
  document.getElementById('reg-lng').value='';
  document.getElementById('reg-password').value='';
  document.getElementById('reg-description').value='';
  document.getElementById('reg-whatsapp').value='';
  document.getElementById('reg-photo-preview').innerHTML='';
  document.getElementById('reg-photo').value='';
  document.getElementById('btn-capture-location').textContent = '📍 Capture My Exact Shop Location';
  document.getElementById('btn-capture-location').style.background = 'var(--earth)';
  document.getElementById('btn-capture-location').disabled = false;
  document.getElementById('reg-gps-status').textContent = 'Tap above — your exact location will be auto-filled';
}"""

new = """  if (result.error) { showToast('Register Error: '+result.error.message); return; }
  document.getElementById('login-phone').value = phone;
  document.getElementById('reg-name').value='';
  document.getElementById('reg-phone').value='';
  document.getElementById('reg-location').value='';
  document.getElementById('reg-lat').value='';
  document.getElementById('reg-lng').value='';
  document.getElementById('reg-password').value='';
  document.getElementById('reg-password-confirm').value='';
  document.getElementById('reg-terms-check').checked = false;
  document.getElementById('reg-description').value='';
  document.getElementById('reg-whatsapp').value='';
  document.getElementById('reg-photo-preview').innerHTML='';
  document.getElementById('reg-photo').value='';
  document.getElementById('btn-capture-location').textContent = '📍 Capture My Exact Shop Location';
  document.getElementById('btn-capture-location').style.background = 'var(--earth)';
  document.getElementById('btn-capture-location').disabled = false;
  document.getElementById('reg-gps-status').textContent = 'Tap above — your exact location will be auto-filled';
  regGoToStep(1);
  document.getElementById('auth-panel-register').classList.add('hidden');
  document.getElementById('auth-panel-success').classList.remove('hidden');
}"""

if old in html:
    html = html.replace(old, new)
    print('Success flow logic added, login pre-filled with phone')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

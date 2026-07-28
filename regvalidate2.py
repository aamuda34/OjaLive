f = open('index.html', 'r')
html = f.read()
f.close()

old = """        <input type=\"hidden\" id=\"reg-lat\">
        <input type=\"hidden\" id=\"reg-lng\">
        <div style=\"display:flex;gap:8px;margin-top:16px;\">
          <button type=\"button\" class=\"btn btn-o\" onclick=\"regGoToStep(1)\" style=\"margin:0;flex:1;\">Back</button>
          <button type=\"button\" class=\"btn btn-p\" onclick=\"regGoToStep(3)\" style=\"margin:0;flex:2;\">Continue</button>
        </div>"""

new = """        <input type=\"hidden\" id=\"reg-lat\">
        <input type=\"hidden\" id=\"reg-lng\">
        <div id=\"reg-step2-error\" style=\"color:#C0392B;font-size:12px;margin-top:8px;display:none;\"></div>
        <div style=\"display:flex;gap:8px;margin-top:16px;\">
          <button type=\"button\" class=\"btn btn-o\" onclick=\"regGoToStep(1)\" style=\"margin:0;flex:1;\">Back</button>
          <button type=\"button\" class=\"btn btn-p\" onclick=\"regValidateStep2()\" style=\"margin:0;flex:2;\">Continue</button>
        </div>"""

if old in html:
    html = html.replace(old, new)
    print('1. Step 2 button updated to call validation')
else:
    print('1. SKIP')

old2 = "function regGoToStep(step) {"
new2 = """function regValidateStep2() {
  var errEl = document.getElementById('reg-step2-error');
  var state = document.getElementById('reg-state').value;
  var lat = document.getElementById('reg-lat').value;
  if (!state) { errEl.textContent = 'Please select your state'; errEl.style.display = 'block'; return; }
  if (!lat) { errEl.textContent = 'Please capture your shop location first'; errEl.style.display = 'block'; return; }
  errEl.style.display = 'none';
  regGoToStep(3);
}
function regGoToStep(step) {"""

if old2 in html:
    html = html.replace(old2, new2, 1)
    print('2. regValidateStep2 function added')
else:
    print('2. SKIP')

f = open('index.html', 'w')
f.write(html)
f.close()

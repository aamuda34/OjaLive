f = open('index.html', 'r')
html = f.read()
f.close()

old = """        <div id=\"reg-step3-error\" style=\"color:#C0392B;font-size:12px;margin-top:8px;display:none;\"></div>
        <div style=\"display:flex;gap:8px;margin-top:16px;\">
          <button type=\"button\" class=\"btn btn-o\" onclick=\"regGoToStep(2)\" style=\"margin:0;flex:1;\">Back</button>
          <button class=\"btn btn-p\" id=\"btn-register-seller\" onclick=\"regValidateStep3()\" style=\"margin:0;flex:2;\">Create Account</button>
        </div>"""

new = """        <label style=\"display:flex;align-items:flex-start;gap:8px;margin-top:16px;text-transform:none;font-size:13px;color:var(--dark);font-weight:500;cursor:pointer;\">
          <input type=\"checkbox\" id=\"reg-terms-check\" style=\"width:16px;height:16px;margin-top:2px;flex-shrink:0;accent-color:var(--earth);\">
          <span>I agree to OjaLive's <a href=\"#\" onclick=\"event.preventDefault();showToast('Terms page coming soon')\" style=\"color:var(--earth);text-decoration:underline;\">Terms of Service</a> and <a href=\"#\" onclick=\"event.preventDefault();showToast('Privacy page coming soon')\" style=\"color:var(--earth);text-decoration:underline;\">Privacy Policy</a></span>
        </label>
        <div id=\"reg-step3-error\" style=\"color:#C0392B;font-size:12px;margin-top:8px;display:none;\"></div>
        <div style=\"display:flex;gap:8px;margin-top:16px;\">
          <button type=\"button\" class=\"btn btn-o\" onclick=\"regGoToStep(2)\" style=\"margin:0;flex:1;\">Back</button>
          <button class=\"btn btn-p\" id=\"btn-register-seller\" onclick=\"regValidateStep3()\" style=\"margin:0;flex:2;\">Create Account</button>
        </div>"""

if old in html:
    html = html.replace(old, new)
    print('Terms of Service checkbox added')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

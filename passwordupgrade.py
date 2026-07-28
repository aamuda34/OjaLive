f = open('index.html', 'r')
html = f.read()
f.close()

old = """        <label>Password</label>
        <input type=\"password\" id=\"reg-password\" placeholder=\"Min 6 characters\">
        <div style=\"display:flex;gap:8px;margin-top:16px;\">
          <button type=\"button\" class=\"btn btn-o\" onclick=\"regGoToStep(2)\" style=\"margin:0;flex:1;\">Back</button>
          <button class=\"btn btn-p\" id=\"btn-register-seller\" onclick=\"sellerRegister()\" style=\"margin:0;flex:2;\">Create Account</button>
        </div>"""

new = """        <label>Password</label>
        <div style=\"position:relative;\">
          <input type=\"password\" id=\"reg-password\" placeholder=\"Min 6 characters\" oninput=\"checkPasswordStrength()\" style=\"padding-right:44px;\">
          <button type=\"button\" onclick=\"togglePasswordVisibility('reg-password',this)\" style=\"position:absolute;right:10px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--muted);font-size:16px;cursor:pointer;padding:4px;\">👁</button>
        </div>
        <div id=\"reg-password-strength\" style=\"height:4px;border-radius:2px;background:var(--border);margin-top:6px;overflow:hidden;\">
          <div id=\"reg-password-strength-bar\" style=\"height:100%;width:0%;background:#C0392B;transition:width 0.2s,background 0.2s;\"></div>
        </div>
        <div id=\"reg-password-strength-label\" style=\"font-size:11px;color:var(--muted);margin-top:4px;\"></div>
        <label style=\"margin-top:14px;\">Confirm Password</label>
        <div style=\"position:relative;\">
          <input type=\"password\" id=\"reg-password-confirm\" placeholder=\"Re-enter your password\" style=\"padding-right:44px;\">
          <button type=\"button\" onclick=\"togglePasswordVisibility('reg-password-confirm',this)\" style=\"position:absolute;right:10px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--muted);font-size:16px;cursor:pointer;padding:4px;\">👁</button>
        </div>
        <div id=\"reg-step3-error\" style=\"color:#C0392B;font-size:12px;margin-top:8px;display:none;\"></div>
        <div style=\"display:flex;gap:8px;margin-top:16px;\">
          <button type=\"button\" class=\"btn btn-o\" onclick=\"regGoToStep(2)\" style=\"margin:0;flex:1;\">Back</button>
          <button class=\"btn btn-p\" id=\"btn-register-seller\" onclick=\"regValidateStep3()\" style=\"margin:0;flex:2;\">Create Account</button>
        </div>"""

if old in html:
    html = html.replace(old, new)
    print('Password field upgraded with strength meter and confirm')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

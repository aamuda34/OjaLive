f = open('index.html', 'r')
html = f.read()
f.close()

old = """        <input type=\"hidden\" id=\"reg-lat\">
        <input type=\"hidden\" id=\"reg-lng\">
        <label>Profile/Shop Photo (Optional)</label>
        <div id=\"reg-photo-preview\" style=\"margin-bottom:8px;\"></div>
        <input type=\"file\" id=\"reg-photo\" accept=\"image/*\" style=\"display:none;\" onchange=\"previewRegPhoto()\">
        <button type=\"button\" onclick=\"document.getElementById('reg-photo').click()\" style=\"width:100%;padding:10px;background:#F7F2EA;border:1.5px dashed var(--border);border-radius:10px;font-size:13px;color:var(--muted);cursor:pointer;margin-bottom:10px;\">📷 Add Shop Photo</button>
        <label>Opening Hours (Optional)</label>
        <div style=\"display:flex;gap:8px;margin-bottom:10px;\">
          <input type=\"time\" id=\"reg-open-from\" style=\"flex:1;padding:10px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;\" placeholder=\"Open from\">
          <span style=\"align-self:center;color:var(--muted);\">to</span>
          <input type=\"time\" id=\"reg-open-to\" style=\"flex:1;padding:10px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;\" placeholder=\"Close at\">
        </div>
        <select id=\"reg-open-days\" style=\"width:100%;padding:10px 12px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;background:#fff;margin-bottom:10px;\">
          <option value=\"Mon-Fri\">Monday - Friday</option>
          <option value=\"Mon-Sat\">Monday - Saturday</option>
          <option value=\"Mon-Sun\">Monday - Sunday (All week)</option>
          <option value=\"Tue-Sun\">Tuesday - Sunday</option>
          <option value=\"Weekends\">Weekends Only</option>
        </select>
        <label>WhatsApp Number (Optional)</label>
        <input type=\"tel\" id=\"reg-whatsapp\" placeholder=\"e.g. 08012345678 (if different from phone)\">
        <label>Business Description (Optional)</label>
        <textarea id=\"reg-description\" placeholder=\"e.g. We sell quality building materials in Iwo since 2010...\" style=\"width:100%;padding:12px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;resize:none;height:80px;font-family:inherit;\"></textarea>
        <label>Business Type</label>
        <select id=\"reg-trade\">
          <option>Building Materials</option>
          <option>Foodstuff</option>
          <option>Hardware</option>
          <option>Roofing Supplies</option>
          <option>Timber & Plywood</option>
          <option>Fabric & Clothing</option>
          <option>Electronics</option>
          <option>Other</option>
        </select>
        <label>Password</label>
        <input type=\"password\" id=\"reg-password\" placeholder=\"Min 6 characters\">
        <button class=\"btn btn-p\" id=\"btn-register-seller\" onclick=\"sellerRegister()\" style=\"margin-top:16px;\">Create Account</button>
      </div>
      <div class=\"card\" id=\"auth-panel-login\">"""

new = """        <input type=\"hidden\" id=\"reg-lat\">
        <input type=\"hidden\" id=\"reg-lng\">
        <div style=\"display:flex;gap:8px;margin-top:16px;\">
          <button type=\"button\" class=\"btn btn-o\" onclick=\"regGoToStep(1)\" style=\"margin:0;flex:1;\">Back</button>
          <button type=\"button\" class=\"btn btn-p\" onclick=\"regGoToStep(3)\" style=\"margin:0;flex:2;\">Continue</button>
        </div>
        </div>
        <div id=\"reg-step-3\" class=\"hidden\">
        <label>Profile/Shop Photo (Optional)</label>
        <div id=\"reg-photo-preview\" style=\"margin-bottom:8px;\"></div>
        <input type=\"file\" id=\"reg-photo\" accept=\"image/*\" style=\"display:none;\" onchange=\"previewRegPhoto()\">
        <button type=\"button\" onclick=\"document.getElementById('reg-photo').click()\" style=\"width:100%;padding:10px;background:#F7F2EA;border:1.5px dashed var(--border);border-radius:10px;font-size:13px;color:var(--muted);cursor:pointer;margin-bottom:10px;\">📷 Add Shop Photo</button>
        <label>Opening Hours (Optional)</label>
        <div style=\"display:flex;gap:8px;margin-bottom:10px;\">
          <input type=\"time\" id=\"reg-open-from\" style=\"flex:1;padding:10px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;\" placeholder=\"Open from\">
          <span style=\"align-self:center;color:var(--muted);\">to</span>
          <input type=\"time\" id=\"reg-open-to\" style=\"flex:1;padding:10px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;\" placeholder=\"Close at\">
        </div>
        <select id=\"reg-open-days\" style=\"width:100%;padding:10px 12px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;background:#fff;margin-bottom:10px;\">
          <option value=\"Mon-Fri\">Monday - Friday</option>
          <option value=\"Mon-Sat\">Monday - Saturday</option>
          <option value=\"Mon-Sun\">Monday - Sunday (All week)</option>
          <option value=\"Tue-Sun\">Tuesday - Sunday</option>
          <option value=\"Weekends\">Weekends Only</option>
        </select>
        <label>WhatsApp Number (Optional)</label>
        <input type=\"tel\" id=\"reg-whatsapp\" placeholder=\"e.g. 08012345678 (if different from phone)\">
        <label>Business Description (Optional)</label>
        <textarea id=\"reg-description\" placeholder=\"e.g. We sell quality building materials in Iwo since 2010...\" style=\"width:100%;padding:12px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;resize:none;height:80px;font-family:inherit;\"></textarea>
        <label>Business Type</label>
        <select id=\"reg-trade\">
          <option>Building Materials</option>
          <option>Foodstuff</option>
          <option>Hardware</option>
          <option>Roofing Supplies</option>
          <option>Timber & Plywood</option>
          <option>Fabric & Clothing</option>
          <option>Electronics</option>
          <option>Other</option>
        </select>
        <label>Password</label>
        <input type=\"password\" id=\"reg-password\" placeholder=\"Min 6 characters\">
        <div style=\"display:flex;gap:8px;margin-top:16px;\">
          <button type=\"button\" class=\"btn btn-o\" onclick=\"regGoToStep(2)\" style=\"margin:0;flex:1;\">Back</button>
          <button class=\"btn btn-p\" id=\"btn-register-seller\" onclick=\"sellerRegister()\" style=\"margin:0;flex:2;\">Create Account</button>
        </div>
        </div>
      </div>
      <div class=\"card\" id=\"auth-panel-login\">"""

if old in html:
    html = html.replace(old, new)
    print('SUCCESS: Step 3 created, form fully split into 3 steps')
else:
    print('ERROR: pattern not found - no changes made')

f = open('index.html', 'w')
f.write(html)
f.close()

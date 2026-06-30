f = open('index.html', 'r')
html = f.read()
f.close()

old2 = '''    <div style="padding:16px;">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;">
        <div style="flex:1;">
          <div id="bd-name" style="font-family:'Syne',sans-serif;font-size:22px;font-weight:800;color:var(--dark);"></div>
          <div id="bd-category" style="font-size:12px;color:var(--muted);margin-top:4px;"></div>
        </div>
        <div style="text-align:right;">
          <div id="bd-price" style="font-family:'Syne',sans-serif;font-size:24px;font-weight:800;color:var(--earth);"></div>
          <div id="bd-unit" style="font-size:12px;color:var(--muted);margin-top:2px;"></div>
          <div id="bd-badge" style="margin-top:4px;"></div>
        </div>
      </div>
      <div id="bd-stock" style="display:none;background:#E8F5EE;color:var(--green);font-size:12px;font-weight:600;padding:6px 12px;border-radius:8px;margin-bottom:12px;"></div>'''

new2 = '''    <div style="padding:18px 16px 16px;border-radius:20px 20px 0 0;background:#fff;position:relative;margin-top:-16px;">
      <div id="bd-category" style="font-size:11px;color:var(--earth);font-weight:700;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:6px;"></div>
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:10px;margin-bottom:10px;">
        <div id="bd-name" style="font-family:'Syne',sans-serif;font-size:19px;font-weight:800;color:var(--dark);line-height:1.25;flex:1;"></div>
        <div id="bd-badge" style="flex-shrink:0;margin-top:2px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:6px;margin-bottom:10px;">
        <div id="bd-price" style="font-family:'Syne',sans-serif;font-size:26px;font-weight:800;color:var(--earth);"></div>
        <div id="bd-unit" style="font-size:13px;color:var(--muted);"></div>
      </div>
      <div id="bd-stock" style="display:none;background:#E8F5EE;color:var(--green);font-size:12px;font-weight:600;padding:6px 12px;border-radius:8px;margin-bottom:4px;"></div>'''

if old2 in html:
    html = html.replace(old2, new2)
    print('2. Name/price block upgraded')
else:
    print('2. SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()
print('Saved part 2')

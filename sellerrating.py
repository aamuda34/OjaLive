f = open('index.html', 'r')
html = f.read()
f.close()

old1 = '''            <div id="bd-trader" style="font-size:14px;font-weight:700;color:var(--dark);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"></div>
            <div id="bd-followers-count" style="font-size:11px;color:var(--muted);"></div>'''

new1 = '''            <div style="display:flex;align-items:center;gap:6px;">
              <div id="bd-trader" style="font-size:14px;font-weight:700;color:var(--dark);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"></div>
              <div id="bd-seller-inline-rating" style="font-size:11px;color:#F59E0B;font-weight:700;flex-shrink:0;display:none;"></div>
            </div>
            <div id="bd-followers-count" style="font-size:11px;color:var(--muted);"></div>'''

if old1 in html:
    html = html.replace(old1, new1)
    print('Seller rating slot added')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

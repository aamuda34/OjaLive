f = open('index.html', 'r')
html = f.read()
f.close()

old = "var selResult = await db.from('traders').select('photo_url,opening_hours,whatsapp').eq('full_name',item.trader).single();"
new = "var selResult = await db.from('traders').select('photo_url,opening_hours,whatsapp,followers_count').eq('full_name',item.trader).single();"

if old in html:
    html = html.replace(old, new)
    print('Fixed - followers_count now included in query')
else:
    print('ERROR: pattern not found')

f = open('index.html', 'w')
f.write(html)
f.close()

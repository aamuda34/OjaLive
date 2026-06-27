f = open('index.html', 'r')
html = f.read()
f.close()

html = html.replace(
"    var result = await db.from('Listing').select('*').eq('verified', true);",
"    var result = await db.from('Listing').select('*');"
)

f = open('index.html', 'w')
f.write(html)
f.close()
print('Done!')

f = open('index.html', 'r')
html = f.read()
f.close()

old = '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>\n<script src="https://cdn.jsdelivr.net/npm/@imgly/background-removal@1.7.0/dist/browser.js"></script>'
new = '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>'

if old in html:
    html = html.replace(old, new)
    print('Broken library script removed')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

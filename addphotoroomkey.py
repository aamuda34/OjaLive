f = open('index.html', 'r')
html = f.read()
f.close()

old = 'const SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml2eHRtaG9qcnd4ZnNmYmxxdGN2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIyMDA4NjksImV4cCI6MjA5Nzc3Njg2OX0.hnYsiqkLwnFlo4ZZD9iGbotphOh1lvlr_31sBkds2eM";'

new = old + '\nconst PHOTOROOM_KEY = "sandbox_sk_pr_default_682134b11d64d9a93db348a4dd0d9e6a1e675385";'

if old in html:
    html = html.replace(old, new)
    print('PhotoRoom key constant added')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

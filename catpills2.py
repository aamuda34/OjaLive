f = open('index.html', 'r')
html = f.read()
f.close()

replacements = [
    ('filterCat(this,\'Roofing Supplies\')"> 🏠 Roofing</button>', 'filterCat(this,\'Roofing Supplies\')">Roofing</button>'),
    ('filterCat(this,\'Timber & Plywood\')"> 🪵 Timber</button>', 'filterCat(this,\'Timber & Plywood\')">Timber</button>'),
    ('filterCat(this,\'Automobile Parts\')"> 🚗 Auto</button>', 'filterCat(this,\'Automobile Parts\')">Auto Parts</button>'),
]

count = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new)
        count += 1
    else:
        print('SKIP:', old[:50])

f = open('index.html', 'w')
f.write(html)
f.close()
print('Done! Replaced', count, 'of 3')

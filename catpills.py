f = open('index.html', 'r')
html = f.read()
f.close()

replacements = [
    ('">🌾 Food</button>', '">Foodstuff</button>'),
    ('">🏗️ Building</button>', '">Building</button>'),
    ('">🔧 Hardware</button>', '">Hardware</button>'),
    ('">📱 Electronics</button>', '">Electronics</button>'),
    ('">📲 Phones</button>', '">Phones</button>'),
    ('"> 🏠 Roofing</button>', '">Roofing</button>'),
    ('"> 🪵 Timber</button>', '">Timber</button>'),
    ('">👗 Fashion</button>', '">Fashion</button>'),
    ('">🥤 Drinks</button>', '">Beverages</button>'),
    ('">💄 Beauty</button>', '">Beauty</button>'),
    ('">🛋️ Furniture</button>', '">Furniture</button>'),
    ('"> 🚗 Auto</button>', '">Auto Parts</button>'),
    ('">🌱 Farm</button>', '">Farm</button>'),
    ('">🐓 Livestock</button>', '">Livestock</button>'),
    ('">📦 Other</button>', '">Other</button>'),
]

count = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new)
        count += 1

f = open('index.html', 'w')
f.write(html)
f.close()
print('Done! Replaced', count, 'of', len(replacements))

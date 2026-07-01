f = open('index.html', 'r')
html = f.read()
f.close()
changes = 0

# 1. Add skeleton CSS right before </style>
old_style_end = "</style>"
skeleton_css = """.skeleton{background:linear-gradient(90deg,#EFEFEF 25%,#F5F5F5 50%,#EFEFEF 75%);background-size:200% 100%;animation:skeleton-pulse 1.5s ease-in-out infinite;}
@keyframes skeleton-pulse{0%{background-position:200% 0;}100%{background-position:-200% 0;}}
</style>"""

if old_style_end in html:
    html = html.replace(old_style_end, skeleton_css, 1)
    changes += 1
    print('1. Skeleton CSS added')
else:
    print('1. SKIP')

# 2. Replace the loading text with skeleton cards
old_board = '<div id="board" style="padding:12px 14px;"><div class="empty">Loading prices...</div></div>'

skeleton_card = '<div style="background:#fff;border:1px solid #EEEEEE;border-radius:10px;overflow:hidden;"><div class="skeleton" style="width:100%;height:200px;"></div><div style="padding:11px 12px 13px;"><div class="skeleton" style="height:13px;border-radius:4px;margin-bottom:8px;width:80%;"></div><div class="skeleton" style="height:11px;border-radius:4px;margin-bottom:10px;width:50%;"></div><div class="skeleton" style="height:18px;border-radius:4px;width:60%;"></div></div></div>'

new_board = '<div id="board" style="padding:14px;"><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">' + (skeleton_card * 6) + '</div></div>'

if old_board in html:
    html = html.replace(old_board, new_board)
    changes += 1
    print('2. Skeleton cards added to board')
else:
    print('2. SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()
print('TOTAL:', changes, '/2')

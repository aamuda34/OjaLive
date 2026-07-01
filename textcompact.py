f = open('index.html', 'r')
html = f.read()
f.close()
changes = 0

old = """      +'<div style="padding:9px 10px 11px;display:flex;flex-direction:column;flex:1;">'
      +'<div style="font-size:12px;color:#222;line-height:1.35;margin-bottom:3px;font-weight:500;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;min-height:32px;">'+item.name+'</div>'
      +'<div style="font-size:10px;color:#C4612A;font-weight:600;margin-bottom:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">🏪 '+item.trader+'</div>'
      +'<div style="margin-top:auto;">'
      +'<div style="font-family:Syne,sans-serif;font-size:17px;font-weight:800;color:#1A1208;">₦'+Number(item.price).toLocaleString()+'</div>'
      +'<div style="font-size:10px;color:#999;margin-bottom:5px;">per '+unitClean+'</div>'
      +'<div style="font-size:10px;color:'+distColor+';font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">📍 '+distText+'</div>'
      +'</div>'
      +'</div>'"""

new = """      +'<div style="padding:7px 8px 9px;display:flex;flex-direction:column;flex:1;">'
      +'<div style="font-size:11.5px;color:#222;line-height:1.3;margin-bottom:2px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">'+item.name+'</div>'
      +'<div style="font-size:9.5px;color:#C4612A;font-weight:600;margin-bottom:4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">🏪 '+item.trader+'</div>'
      +'<div style="margin-top:auto;">'
      +'<div style="font-family:Syne,sans-serif;font-size:16px;font-weight:800;color:#1A1208;">₦'+Number(item.price).toLocaleString()+'</div>'
      +'<div style="font-size:9.5px;color:#999;margin-bottom:3px;">per '+unitClean+'</div>'
      +'<div style="font-size:9.5px;color:'+distColor+';font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">📍 '+distText+'</div>'
      +'</div>'
      +'</div>'"""

if old in html:
    html = html.replace(old, new)
    changes += 1
    print('Text area compacted')
else:
    print('SKIP - pattern not found')

f = open('index.html', 'w')
f.write(html)
f.close()

f = open('index.html', 'r')
html = f.read()
f.close()

# Increase image height
html = html.replace('var IMG_H = 175;', 'var IMG_H = 200;')

# Give text section more breathing room
old_text = """      +'<div style="padding:7px 8px 9px;display:flex;flex-direction:column;flex:1;">'
      +'<div style="font-size:11.5px;color:#222;line-height:1.3;margin-bottom:2px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">'+item.name+'</div>'
      +'<div style="font-size:9.5px;color:#C4612A;font-weight:600;margin-bottom:4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">🏪 '+item.trader+'</div>'
      +'<div style="margin-top:auto;">'
      +'<div style="font-family:Syne,sans-serif;font-size:16px;font-weight:800;color:#1A1208;">₦'+Number(item.price).toLocaleString()+'</div>'
      +'<div style="font-size:9.5px;color:#999;margin-bottom:3px;">per '+unitClean+'</div>'
      +'<div style="font-size:9.5px;color:'+distColor+';font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">📍 '+distText+'</div>'
      +'</div>'
      +'</div>'"""

new_text = """      +'<div style="padding:11px 12px 13px;display:flex;flex-direction:column;flex:1;">'
      +'<div style="font-size:13px;color:#222;line-height:1.4;margin-bottom:5px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">'+item.name+'</div>'
      +'<div style="font-size:11px;color:#C4612A;font-weight:600;margin-bottom:7px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">🏪 '+item.trader+'</div>'
      +'<div style="margin-top:auto;">'
      +'<div style="font-family:Syne,sans-serif;font-size:18px;font-weight:800;color:#1A1208;">₦'+Number(item.price).toLocaleString()+'</div>'
      +'<div style="font-size:11px;color:#999;margin-bottom:5px;">per '+unitClean+'</div>'
      +'<div style="font-size:11px;color:'+distColor+';font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">📍 '+distText+'</div>'
      +'</div>'
      +'</div>'"""

count = 0
if old_text in html:
    html = html.replace(old_text, new_text)
    count = 1

f = open('index.html', 'w')
f.write(html)
f.close()
print('Image height updated. Text section updated:', count == 1)

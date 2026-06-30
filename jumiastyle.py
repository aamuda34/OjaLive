f = open('index.html', 'r')
html = f.read()
f.close()

old = """    listingMap[item.id] = item;
    var likeCount = item.likes||0;
    var ratingBadge = likeCount>0 ? '<div style="position:absolute;bottom:8px;right:8px;background:rgba(0,0,0,0.7);color:#0ECB81;font-size:10px;font-weight:700;padding:2px 8px;border-radius:20px;">👍 '+likeCount+'</div>' : '';
    return '<div onclick="openBuyerDetail('+item.id+')" style="background:var(--card);border:1px solid var(--border);border-radius:12px;overflow:hidden;cursor:pointer;display:flex;flex-direction:column;">'
      +'<div style="position:relative;">'
      +imgHtml
      +'<div style="position:absolute;top:8px;left:8px;background:rgba(0,0,0,0.6);color:#fff;font-size:10px;font-weight:600;padding:2px 8px;border-radius:20px;">'+item.category+'</div>'
      +'<div style="position:absolute;top:8px;right:8px;background:rgba(0,0,0,0.6);color:'+chgColor+';font-size:10px;font-weight:700;padding:2px 8px;border-radius:20px;">'+chgArrow+' '+chgLabel+'</div>'
      +(item.stock?'<div style="position:absolute;bottom:8px;left:8px;background:#0ECB81;color:#fff;font-size:10px;font-weight:600;padding:2px 8px;border-radius:20px;">'+item.stock+' left</div>':'')
      +'</div>'
      +'<div style="padding:10px;">'
      +'<div style="font-size:13px;font-weight:700;color:var(--dark);line-height:1.3;margin-bottom:4px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;">'+item.name+'</div>'
      +'<div style="font-size:11px;color:var(--muted);margin-bottom:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">'+item.trader+'</div>'
      +'<div style="font-family:Syne,sans-serif;font-size:16px;font-weight:800;color:var(--earth);">₦'+Number(item.price).toLocaleString()+'</div>'
      +'<div style="font-size:10px;color:var(--muted);margin-bottom:4px;">per '+item.unit+'</div>'
      +(distBadge?'<div style="font-size:10px;color:var(--green);font-weight:600;">'+distBadge+'</div>':'<div style="font-size:10px;color:var(--muted);">📍 '+item.location+'</div>')
      +'</div>'
      +'</div>';"""

new = """    listingMap[item.id] = item;
    var likeCount = item.likes||0;
    var chgBadge = (chg==='up'||chg==='down') ? '<div style="position:absolute;top:8px;right:8px;background:'+(chg==='up'?'#0ECB81':'#F6465D')+';color:#fff;font-size:9px;font-weight:800;padding:3px 8px;border-radius:6px;">'+chgArrow+' '+chgLabel+'</div>' : '';
    var stockBadge = item.stock ? '<div style="position:absolute;top:8px;left:8px;background:#0ECB81;color:#fff;font-size:9px;font-weight:700;padding:3px 8px;border-radius:6px;">'+item.stock+' left</div>' : '';
    var unitClean = (item.unit||'').toLowerCase().startsWith('per ') ? item.unit.slice(4) : item.unit;
    var distText = (buyerLat && buyerLng && item.latitude && item.longitude) ? getDistance(buyerLat,buyerLng,item.latitude,item.longitude)+' km away' : item.location;
    return '<div onclick="openBuyerDetail('+item.id+')" style="background:#fff;border:1px solid #EBEBEB;border-radius:8px;overflow:hidden;cursor:pointer;">'
      +'<div style="position:relative;background:#F5F5F5;">'
      +imgHtml
      +chgBadge
      +stockBadge
      +'</div>'
      +'<div style="padding:8px 10px 12px;">'
      +'<div style="font-size:12px;color:#333;line-height:1.4;margin-bottom:6px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;">'+item.name+'</div>'
      +'<div style="font-family:Syne,sans-serif;font-size:17px;font-weight:800;color:#C4612A;">₦'+Number(item.price).toLocaleString()+'</div>'
      +'<div style="font-size:10px;color:#999;margin-bottom:6px;">per '+unitClean+'</div>'
      +'<div style="font-size:10px;color:#888;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">📍 '+distText+'</div>'
      +'</div>'
      +'</div>';"""

if old in html:
    html = html.replace(old, new)
    print('Cards upgraded to Jumia style')
else:
    print('ERROR: Could not find card code')

f = open('index.html', 'w')
f.write(html)
f.close()
print('Done!')

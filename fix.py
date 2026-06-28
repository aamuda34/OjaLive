with open('/storage/emulated/0/OjaLive/index.html', 'r') as f:
    content = f.read()

old = """  var updateData = {full_name:name,phone:phone,location:location,trade:trade,latitude:editLat,longitude:editLng,photo_url:photoUrl};
  if (description !== undefined) updateData.description = description;
  var result = await db.from('traders').update(updateData).eq('id',currentSeller.id);"""

new = """  var result = await db.from('traders').update({full_name:name,phone:phone,location:location,trade:trade,latitude:editLat,longitude:editLng,photo_url:photoUrl}).eq('id',currentSeller.id);
  if (!result.error && description) {
    await db.from('traders').update({description:description}).eq('id',currentSeller.id);
  }"""

if old in content:
    content = content.replace(old, new)
    print("Fixed")
else:
    print("FAILED")

with open('/storage/emulated/0/OjaLive/index.html', 'w') as f:
    f.write(content)

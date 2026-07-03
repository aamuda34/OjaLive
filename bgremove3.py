f = open('index.html', 'r')
html = f.read()
f.close()
changes = 0

old1 = """    var imgFiles = document.getElementById('add-item-images').files;
    if (imgFiles.length > 0 && result.data && result.data[0]) {
      showToast('Uploading photos...');
      var urls = await uploadImages(Array.from(imgFiles), result.data[0].id);"""

new1 = """    var imgFiles = photoFiles.add;
    if (imgFiles.length > 0 && result.data && result.data[0]) {
      showToast('Uploading photos...');
      var urls = await uploadImages(imgFiles, result.data[0].id);"""

if old1 in html:
    html = html.replace(old1, new1)
    changes += 1
    print('1. Add-listing save fixed to use enhanced photos')
else:
    print('1. SKIP')

old2 = """  var editImgFiles = document.getElementById('edit-item-images').files;
  if (editImgFiles.length > 0) {"""

new2 = """  var editImgFiles = photoFiles.edit;
  if (editImgFiles.length > 0) {"""

if old2 in html:
    html = html.replace(old2, new2)
    changes += 1
    print('2. Edit-listing save fixed to use enhanced photos')
else:
    print('2. SKIP')

old3 = "var editUrls = await uploadImages(Array.from(editImgFiles), currentEditingListingId);"
new3 = "var editUrls = await uploadImages(editImgFiles, currentEditingListingId);"

if old3 in html:
    html = html.replace(old3, new3)
    changes += 1
    print('3. uploadImages call fixed for edit')
else:
    print('3. SKIP')

f = open('index.html', 'w')
f.write(html)
f.close()
print('TOTAL:', changes, '/3')

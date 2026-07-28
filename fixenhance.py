f = open('index.html', 'r')
html = f.read()
f.close()

old = """async function enhancePhoto(mode, idx) {
  var thumb = document.getElementById(mode+'-thumb-'+idx);
  if (!thumb) return;
  var originalHTML = thumb.innerHTML;
  thumb.innerHTML = '<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:#F5F5F5;"><div style="width:16px;height:16px;border:2px solid var(--earth);border-top-color:transparent;border-radius:50%;animation:spin 0.8s linear infinite;"></div></div>';
  try {
    var blob = await window.imglyRemoveBackground(photoFiles[mode][idx]);
    var newFile = new File([blob], photoFiles[mode][idx].name.replace(/\\.[^.]+$/, '')+'-nobg.png', {type:'image/png'});
    photoFiles[mode][idx] = newFile;
    renderPhotoThumbnails(mode);
    showToast('Background removed');
  } catch(e) {
    thumb.innerHTML = originalHTML;
    showToast('Could not process photo, try again');
  }
}"""

new = """async function enhancePhoto(mode, idx) {
  var thumb = document.getElementById(mode+'-thumb-'+idx);
  if (!thumb) return;
  var originalHTML = thumb.innerHTML;
  thumb.innerHTML = '<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:#F5F5F5;"><div style="width:16px;height:16px;border:2px solid var(--earth);border-top-color:transparent;border-radius:50%;animation:spin 0.8s linear infinite;"></div></div>';
  try {
    var formData = new FormData();
    formData.append('image_file', photoFiles[mode][idx]);
    formData.append('background.color', 'FFFFFF');
    var response = await fetch('https://sdk.photoroom.com/v1/segment', {
      method: 'POST',
      headers: { 'x-api-key': PHOTOROOM_KEY },
      body: formData
    });
    if (!response.ok) throw new Error('API error: '+response.status);
    var blob = await response.blob();
    var newFile = new File([blob], photoFiles[mode][idx].name.replace(/\\.[^.]+$/, '')+'-nobg.png', {type:'image/png'});
    photoFiles[mode][idx] = newFile;
    renderPhotoThumbnails(mode);
    showToast('Background removed');
  } catch(e) {
    thumb.innerHTML = originalHTML;
    showToast('Could not process photo, try again');
  }
}"""

if old in html:
    html = html.replace(old, new)
    print('enhancePhoto rewritten with PhotoRoom API')
else:
    print('SKIP - pattern not found')

f = open('index.html', 'w')
f.write(html)
f.close()

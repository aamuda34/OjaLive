f = open('index.html', 'r')
html = f.read()
f.close()

old = """function previewImages(mode) {
  var input = document.getElementById(mode+'-item-images');
  var preview = document.getElementById(mode+'-images-preview');
  preview.innerHTML = '';
  var files = Array.from(input.files).slice(0,5);
  files.forEach(function(file) {
    var reader = new FileReader();
    reader.onload = function(e) {
      var img = document.createElement('div');
      img.style.cssText = 'width:70px;height:70px;border-radius:8px;overflow:hidden;border:1.5px solid var(--border);position:relative;';
      img.innerHTML = '<img src="'+e.target.result+'" style="width:100%;height:100%;object-fit:cover;">';
      preview.appendChild(img);
    };
    reader.readAsDataURL(file);
  });
}"""

new = """var photoFiles = {add:[], edit:[]};
function previewImages(mode) {
  var input = document.getElementById(mode+'-item-images');
  var preview = document.getElementById(mode+'-images-preview');
  preview.innerHTML = '';
  photoFiles[mode] = Array.from(input.files).slice(0,5);
  renderPhotoThumbnails(mode);
}
function renderPhotoThumbnails(mode) {
  var preview = document.getElementById(mode+'-images-preview');
  preview.innerHTML = '';
  photoFiles[mode].forEach(function(file, idx) {
    var reader = new FileReader();
    reader.onload = function(e) {
      var wrap = document.createElement('div');
      wrap.style.cssText = 'display:flex;flex-direction:column;align-items:center;gap:4px;';
      wrap.innerHTML = '<div id="'+mode+'-thumb-'+idx+'" style="width:70px;height:70px;border-radius:8px;overflow:hidden;border:1.5px solid var(--border);position:relative;background:repeating-conic-gradient(#f0f0f0 0% 25%, #fff 0% 50%) 50% / 12px 12px;"><img src="'+e.target.result+'" style="width:100%;height:100%;object-fit:cover;"></div>'
        + '<button type="button" onclick="enhancePhoto(\\''+mode+'\\','+idx+')" style="font-size:9px;padding:3px 7px;background:var(--earth);color:#fff;border:none;border-radius:12px;cursor:pointer;white-space:nowrap;">Remove BG</button>';
      preview.appendChild(wrap);
    };
    reader.readAsDataURL(file);
  });
}
async function enhancePhoto(mode, idx) {
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

if old in html:
    html = html.replace(old, new)
    print('previewImages rewritten with background removal')
else:
    print('SKIP - pattern not found')

f = open('index.html', 'w')
f.write(html)
f.close()

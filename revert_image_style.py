path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = """    galleryImgs.forEach(function(url){
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;flex-shrink:0;position:relative;">'
        + '<img src="'+url+'" style="width:100%;height:100%;object-fit:cover;display:block;" loading="lazy" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });"""

new = """    galleryImgs.forEach(function(url){
      imgEl.innerHTML += '<div style="min-width:100%;height:100%;scroll-snap-align:center;display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:20px;box-sizing:border-box;">'
        + '<img src="'+url+'" style="max-width:100%;max-height:100%;object-fit:contain;border-radius:8px;" loading="lazy" onclick="showFullImage(this.src)" onerror="this.style.display=\\'none\\'">'
        + '</div>';
    });"""

if old in content:
    content = content.replace(old, new, 1)
    print("Done. Image reverted to Jumia-style (contain).")
else:
    print("WARNING: pattern not found — image may already be in contain style, nothing to revert.")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

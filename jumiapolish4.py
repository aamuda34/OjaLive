f = open('index.html', 'r')
html = f.read()
f.close()

old = "function showFullImage(url) {"
new = """function shareItem() {
  if (!currentDetailItemId || !listingMap[currentDetailItemId]) return;
  var item = listingMap[currentDetailItemId];
  var text = item.name + ' - ₦' + Number(item.price).toLocaleString() + ' (' + item.unit + ') from ' + item.trader + ' on OjaLive';
  if (navigator.share) {
    navigator.share({ title: item.name, text: text, url: window.location.href }).catch(function(){});
  } else {
    navigator.clipboard.writeText(text).then(function(){ showToast('Copied to clipboard!'); }).catch(function(){ showToast('Could not share'); });
  }
}
function showFullImage(url) {"""

if old in html:
    html = html.replace(old, new)
    print('shareItem function added')
else:
    print('SKIP - not found')

f = open('index.html', 'w')
f.write(html)
f.close()

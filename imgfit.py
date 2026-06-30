f = open('index.html', 'r')
lines = f.readlines()
f.close()

for i, line in enumerate(lines):
    if 'IMG_H' in line and 'object-fit:cover' in line and 'display:block' in line:
        lines[i] = "          imgHtml='<div style=\"width:100%;height:'+IMG_H+'px;background:#F5F5F5;display:flex;align-items:center;justify-content:center;overflow:hidden;\"><img src=\"'+imgs[0]+'\" style=\"max-width:100%;max-height:'+IMG_H+'px;object-fit:contain;\" loading=\"lazy\" onerror=\"this.parentElement.innerHTML=\\'<div style=&quot;width:100%;height:'+IMG_H+'px;display:flex;align-items:center;justify-content:center;font-size:44px;background:#F5F5F5;&quot;>🏪</div>\\'\"></div>';\n"
        print('Fixed line', i+1)
        break

f = open('index.html', 'w')
f.writelines(lines)
f.close()
print('Done!')

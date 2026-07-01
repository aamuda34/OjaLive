f = open('index.html', 'r')
lines = f.readlines()
f.close()

for i, line in enumerate(lines):
    if 'IMG_H' in line and 'padding:6px' in line:
        lines[i] = "          imgHtml='<div style=\"width:100%;height:'+IMG_H+'px;background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden;\"><img src=\"'+imgs[0]+'\" style=\"width:100%;height:100%;object-fit:cover;\" loading=\"lazy\" onerror=\"this.parentElement.style.background=\\'#F5F5F5\\';\"></div>';\n"
        print('Fixed image line', i+1)
        break

for i, line in enumerate(lines):
    if 'var IMG_H = 130' in line:
        lines[i] = "    var IMG_H = 170;\n"
        print('Increased image height, line', i+1)
        break

f = open('index.html', 'w')
f.writelines(lines)
f.close()
print('Done!')

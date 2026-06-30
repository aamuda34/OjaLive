f = open('index.html', 'r')
lines = f.readlines()
f.close()

for i, line in enumerate(lines):
    if 'IMG_H' in line and ('object-fit:cover' in line or 'object-fit:contain' in line) and 'loading' in line:
        lines[i] = "          imgHtml='<div style=\"width:100%;height:160px;background:#fff;display:flex;align-items:center;justify-content:center;padding:8px;box-sizing:border-box;\"><img src=\"'+imgs[0]+'\" style=\"max-width:100%;max-height:144px;object-fit:contain;\" loading=\"lazy\" onerror=\"this.parentElement.style.background=\'#F5F5F5';this.style.display=\'none\'\"></div>';\n"
        print('Fixed line', i+1)
        break

# Also make emoji placeholder consistent height and white bg
for i, line in enumerate(lines):
    if 'catEmoji' in line and 'background:linear-gradient' in line and 'E5D9C8' in line:
        lines[i] = "      imgHtml='<div style=\"width:100%;height:160px;display:flex;align-items:center;justify-content:center;font-size:44px;background:#F5F5F5;\">'+emoji+'</div>';\n"
        print('Fixed emoji placeholder line', i+1)
        break

f = open('index.html', 'w')
f.writelines(lines)
f.close()
print('Done!')

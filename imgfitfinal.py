f = open('index.html', 'r')
lines = f.readlines()
f.close()

target_line = 1254
old_check = "object-fit:cover;display:block"

if old_check in lines[target_line - 1]:
    lines[target_line - 1] = "          imgHtml='<div style=\"width:100%;height:'+IMG_H+'px;background:#F5F5F5;display:flex;align-items:center;justify-content:center;padding:6px;box-sizing:border-box;\"><img src=\"'+imgs[0]+'\" style=\"max-width:100%;max-height:100%;object-fit:contain;\" loading=\"lazy\" onerror=\"this.parentElement.style.background=\\'#F5F5F5\\';\"></div>';\n"
    f = open('index.html', 'w')
    f.writelines(lines)
    f.close()
    print('SUCCESS: Line 1254 replaced safely')
else:
    print('SAFETY STOP: Line 1254 does not match expected content. No changes made.')
    print('Actual content:', lines[target_line - 1][:100])

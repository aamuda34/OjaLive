f = open('index.html', 'r')
lines = f.readlines()
f.close()

for i, line in enumerate(lines):
    if "object-fit:cover;\" loading=\"lazy\" onerror=\"this.parentElement.style.background" in line:
        lines[i] = line.replace(
            'style="width:100%;height:100%;object-fit:cover;"',
            'style="width:100%;height:100%;object-fit:contain;padding:10px;box-sizing:border-box;"'
        )
        print('Changed to object-fit:contain, line', i+1)
        break

f = open('index.html', 'w')
f.writelines(lines)
f.close()
print('Done!')

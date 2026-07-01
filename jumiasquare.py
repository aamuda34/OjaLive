f = open('index.html', 'r')
lines = f.readlines()
f.close()

for i, line in enumerate(lines):
    if 'var IMG_H = 165' in line:
        lines[i] = "    var IMG_H = 175;\n"
        print('IMG_H set to 175, line', i+1)
        break

f = open('index.html', 'w')
f.writelines(lines)
f.close()
print('Done!')

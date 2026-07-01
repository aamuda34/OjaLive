f = open('index.html', 'r')
lines = f.readlines()
f.close()
for i, line in enumerate(lines):
    if 'var IMG_H = 200' in line:
        lines[i] = "    var IMG_H = 230;\n"
        print('IMG_H set to 230')
        break
f = open('index.html', 'w')
f.writelines(lines)
f.close()

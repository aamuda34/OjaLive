f = open('index.html', 'r')
lines = f.readlines()
f.close()
for i, line in enumerate(lines):
    if 'var IMG_H = 240' in line:
        lines[i] = "    var IMG_H = 280;\n"
        print('IMG_H set to 280')
        break
f = open('index.html', 'w')
f.writelines(lines)
f.close()

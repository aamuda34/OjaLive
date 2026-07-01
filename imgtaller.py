f = open('index.html', 'r')
lines = f.readlines()
f.close()

for i, line in enumerate(lines):
    if 'var IMG_H = 215' in line:
        lines[i] = "    var IMG_H = 240;\n"
        print('IMG_H increased to 240, line', i+1)
        break

f = open('index.html', 'w')
f.writelines(lines)
f.close()
print('Done!')

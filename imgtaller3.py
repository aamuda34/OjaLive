f = open('index.html', 'r')
lines = f.readlines()
f.close()

for i, line in enumerate(lines):
    if 'var IMG_H = 175' in line:
        lines[i] = "    var IMG_H = 220;\n"
        print('IMG_H set to 220, line', i+1)
        break

f = open('index.html', 'w')
f.writelines(lines)
f.close()
print('Done!')

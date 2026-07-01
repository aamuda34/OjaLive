f = open('index.html', 'r')
lines = f.readlines()
f.close()

# 1. Increase image height to Jumia-style dominant proportion
for i, line in enumerate(lines):
    if 'var IMG_H = 190' in line:
        lines[i] = "    var IMG_H = 215;\n"
        print('IMG_H increased to 215, line', i+1)
        break

# 2. Reduce image padding so it fills more of the frame
for i, line in enumerate(lines):
    if "object-fit:contain;padding:10px" in line:
        lines[i] = lines[i].replace('padding:10px', 'padding:6px')
        print('Image padding reduced, line', i+1)
        break

f = open('index.html', 'w')
f.writelines(lines)
f.close()
print('Done!')

f = open('index.html', 'r')
lines = f.readlines()
f.close()

# Fix 1: increase IMG_H for bigger Jumia-style image
for i, line in enumerate(lines):
    if 'var IMG_H = 170' in line:
        lines[i] = "    var IMG_H = 190;\n"
        print('IMG_H increased to 190, line', i+1)
        break

# Fix 2: wrap image container as position:relative so badge can overlay on it
for i, line in enumerate(lines):
    if 'background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden;\'><img' in line:
        lines[i] = line.replace(
            "background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden;'>",
            "background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative;'>"
        )
        print('Image wrapper set to position:relative, line', i+1)
        break

f = open('index.html', 'w')
f.writelines(lines)
f.close()
print('Done!')

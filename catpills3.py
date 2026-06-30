f = open('index.html', 'r')
lines = f.readlines()
f.close()

for i, line in enumerate(lines):
    if 'Roofing Supplies' in line and 'cat-pill' in line:
        lines[i] = '    <button class="cat-pill" onclick="filterCat(this,\'Roofing Supplies\')">Roofing</button>\n'
        print('Fixed line', i+1, 'Roofing')
    elif 'Timber & Plywood' in line and 'cat-pill' in line:
        lines[i] = '    <button class="cat-pill" onclick="filterCat(this,\'Timber & Plywood\')">Timber</button>\n'
        print('Fixed line', i+1, 'Timber')
    elif 'Automobile Parts' in line and 'cat-pill' in line:
        lines[i] = '    <button class="cat-pill" onclick="filterCat(this,\'Automobile Parts\')">Auto Parts</button>\n'
        print('Fixed line', i+1, 'Auto')

f = open('index.html', 'w')
f.writelines(lines)
f.close()
print('Done!')

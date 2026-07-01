f = open('index.html', 'r')
lines = f.readlines()
f.close()

target = 1271
old_check = 'border:1px solid #EBEBEB;border-radius:10px'

if old_check in lines[target - 1]:
    lines[target - 1] = lines[target - 1].replace(
        'border:1px solid #EBEBEB;border-radius:10px;overflow:hidden;cursor:pointer;display:flex;flex-direction:column;height:100%;',
        'border:1px solid #EEEEEE;border-radius:10px;overflow:hidden;cursor:pointer;display:flex;flex-direction:column;height:100%;box-shadow:0 1px 4px rgba(0,0,0,0.06);'
    )
    f = open('index.html', 'w')
    f.writelines(lines)
    f.close()
    print('SUCCESS: Card shadow added on line', target)
else:
    print('SAFETY STOP: Line', target, 'did not match. No changes made.')
    print('Actual:', lines[target-1][:150])

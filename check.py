with open('/storage/emulated/0/OjaLive/index.html', 'r') as f:
    content = f.read()

# Find all script blocks
import re
scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
print(f"Found {len(scripts)} script blocks")

for i, script in enumerate(scripts):
    lines = script.split('\n')
    for j, line in enumerate(lines):
        # Check for literal newlines inside strings
        if "'" in line and '\n' in line:
            print(f"Block {i}, line {j}: possible broken string: {repr(line[:80])}")
        # Check for unclosed strings
        single = line.count("'") - line.count("\\'")
        if single % 2 != 0 and not line.strip().startswith('//'):
            print(f"Block {i}, line {j+1}: odd quotes: {repr(line[:80])}")

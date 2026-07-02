path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

count = 0
old_a = "ctx.globalAlpha=0.09;ctx.fillStyle='#C4612A';ctx.font='bold 12px sans-serif';ctx.textAlign='center';"
new_a = "ctx.globalAlpha=0.15;ctx.fillStyle='#C4612A';ctx.font='bold 13px sans-serif';ctx.textAlign='center';"
if old_a in content:
    content = content.replace(old_a, new_a, 1)
    count += 1
else:
    print("WARNING: alpha line not found")

old_b = "var stepX=80, stepY=44;"
new_b = "var stepX=70, stepY=40;"
if old_b in content:
    content = content.replace(old_b, new_b, 1)
    count += 1
else:
    print("WARNING: stepX line not found")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. " + str(count) + "/2 replacements applied.")

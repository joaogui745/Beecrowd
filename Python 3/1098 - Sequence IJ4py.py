# 1098 Sequence IJ4
i = 0
j = [1, 2, 3]

while i <= 2:
    for k in range(3):
        print(f'I={i:g} J={j[k]:g}')
    i += 0.2
    j = [x + 0.2 for x in j]
        
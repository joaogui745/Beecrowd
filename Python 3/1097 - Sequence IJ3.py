#1097 Sequence IJ3
i = 1
j = [7, 6, 5]
while i <= 9:
    for dado in range(3):
        print(f'I={i} J={j[dado]}')
    j[2] = j[0]
    j[0], j[1] = j[2] + 2, j[2] + 1
    i += 2
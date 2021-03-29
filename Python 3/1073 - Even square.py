# 1073 Even square
enesimo = int(input())
for valor in range(1, enesimo + 1):
    if valor % 2 == 0:
        print(f'{valor}^2 = {valor ** 2}')
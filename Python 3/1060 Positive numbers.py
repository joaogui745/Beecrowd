# 1060 Positive Numbers
contador = 0
for valor in range(6):
    dado = float(input())
    if dado > 0:
        contador += 1

print(f'{contador} valores positivos')
        
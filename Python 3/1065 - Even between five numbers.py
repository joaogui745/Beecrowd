contador = 0
for i in range(5):
    dado = float(input())
    if dado % 2 == 0:
        contador += 1

print(f'{contador} valores pares')
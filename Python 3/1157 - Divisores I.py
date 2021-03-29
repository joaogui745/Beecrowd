# Divisores I
dividendo = int(input())
for valor in range(1, dividendo + 1):
    if dividendo % valor == 0:
        print(valor)
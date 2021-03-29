# Resto da Divisão
valores = []
valores.append(int(input()))
valores.append(int(input()))
valores.sort()
soma = 0
for valor in range(valores[0] + 1, valores[1]):
    if valor % 5 == 2 or valor % 5 == 3:
        print(valor)


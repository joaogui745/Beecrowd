# Múltiplos de 13
valores = []
valores.append(int(input()))
valores.append(int(input()))
valores.sort()
soma = 0
for valor in range(valores[0], valores[1] + 1):
    if not valor % 13 == 0:
        soma += valor

print(soma)
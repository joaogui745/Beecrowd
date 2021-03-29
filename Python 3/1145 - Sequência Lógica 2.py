# Sequência Lógica 2
valores = input().split()
A = int(valores[0])
B = int(valores[1])

for valor in range(1, B + 1):
    if not valor % A == 0:
        print(valor, end=' ')
    else:
        print(valor)
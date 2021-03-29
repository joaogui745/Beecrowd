# Somando Inteiros Consecutivos
valores = input().split()
A = int(valores[0])
N = int(valores[-1])
soma = 0
for valor in range(0, N):
    soma += A + valor

print(soma)

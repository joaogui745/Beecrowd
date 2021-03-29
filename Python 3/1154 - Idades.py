# Idades
soma = 0
divisor = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    soma += idade
    divisor += 1

print(f'{soma / divisor:.2f}')
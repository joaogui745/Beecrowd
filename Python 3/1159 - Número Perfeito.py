# Número Perfeito
linhas = int(input())
for valor in range(linhas):
    numero = int(input())
    soma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            soma += divisor
    
    if numero == soma:
        print(f'{numero} eh perfeito')
    else:
        print(f'{numero} nao eh perfeito')
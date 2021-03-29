# Soma de Ímpares Consecutivos III
while True:
    X = int(input())
    if X <= 0:
        break
    contador = 0
    soma = 0
    while contador != 5:
        if X % 2 == 0:
            contador += 1
            soma += X
        X += 1
        
    print(soma)

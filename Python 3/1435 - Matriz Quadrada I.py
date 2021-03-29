# Matriz Quadrada I
from math import ceil
while True:
    valor = int(input())
    if valor == 0:
        break
    valores = [x for x in range(1, ceil(valor / 2) + 1)]
    matriz = [[0] * valor for x in range(valor)]
    inicio = 0
    final = valor
    for indice in valores:
        for linha in range(inicio, final):
            for coluna in range(inicio, final):
                matriz[linha][coluna] = indice
        inicio += 1
        final -= 1
    
    for linha in range(valor):
        for coluna in range(valor):
            if coluna < valor - 1:
                print(f'{matriz[linha][coluna]:3}', end=' ')
            else:
                print(f'{matriz[linha][coluna]:3}')
    print('')

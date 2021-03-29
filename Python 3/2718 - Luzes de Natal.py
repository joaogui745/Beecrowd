# Luzes de Natal
qtd = int(input())

for i in range(qtd):
    numero = int(input())
    cont = 0
    binario = bin(numero)[2:]
    binario = binario.split('0')
    print(len(max(binario)))

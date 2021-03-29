# Sequências Crescentes
while True:
    valor = int(input())
    if valor == 0:
        break
    for numero in range(1, valor + 1):
        if not numero == valor:
            print(numero, end=' ')
        else:
           print(numero) 
        
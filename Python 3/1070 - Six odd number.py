#1070 Six odd numbers
contador = 0
valor = int(input())
while contador <= 5:
    if not valor % 2 == 0:
        print(valor)
        contador += 1
    valor += 1
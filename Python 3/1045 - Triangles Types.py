#1045 Triangle Types

lista = input().split()



for i in range(3):
    lista[i] = float(lista[i])

lista.sort(reverse=True)

A = lista[0]
B = lista[1]
C = lista[2]

if A >= (B + C):
    print('NAO FORMA TRIANGULO')
else:
    if (A ** 2) == (B ** 2) + (C ** 2):
        print('TRIANGULO RETANGULO')
    if (A ** 2) > (B ** 2) + (C ** 2):
        print('TRIANGULO OBTUSANGULO')
    if (A ** 2) < (B ** 2) + (C ** 2):
        print('TRIANGULO ACUTANGULO')
    if A == B and B == C:
        print('TRIANGULO EQUILATERO')
    if (A == B and B != C) or (B == C and B != A):
        print('TRIANGULO ISOSCELES')
        

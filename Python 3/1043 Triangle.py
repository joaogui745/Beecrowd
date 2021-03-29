#1043 triangle
contador = 0
lista = input().split()

for i in range(3):
    lista[i] = float(lista[i])

tupla = tuple(lista)

for j in range(3):
    lado_analisado = lista.pop(1)
    soma = sum(lista)
    diferenca = abs(lista[0] - lista[1])
    if lado_analisado > diferenca and lado_analisado < soma:
        contador += 1
        
    lista.append(lado_analisado)

if contador < 3:
    print(f'Area = {((tupla[0] + tupla[1]) * tupla[2]) / 2:.1f}')
else:
    print(f'Perimetro = {sum(lista):.1f}')
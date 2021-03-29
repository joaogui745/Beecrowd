def calcula_numero(index, salario):
    if index == 1:
        salario = (salario - 2000) * 0.08
        return salario
    elif index == 2:
        salario = (salario - 3000) * 0.18 + calcula_numero(1, 3000)
        return salario
    elif index == 3:
        salario = (salario - 4500) * 0.28 + calcula_numero(2, 4500)
        return salario

i = 0
fundo = [2000.01, 3000.01, 4500.01]

valor = float(input())
if valor in fundo:
    i = 1
fundo.append(valor)
fundo.sort()
i += fundo.index(valor)

if i == 0:
    print('Isento')

else:
    print(f'R$ {calcula_numero(i, valor):.2f}')
    
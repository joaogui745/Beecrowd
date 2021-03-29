# 1048 Salary Increase
i = 0
fundos = [0, 400.01, 800.01, 1200.01, 2000.01]
dic = {1:0.15, 2:0.12, 3:0.1, 4:0.07, 5:0.04}

valor = float(input())
if valor in fundos:
    i = 1
fundos.append(valor)
fundos.sort()
i += fundos.index(valor)

print(f'Novo salario: {valor + (valor * dic[i]):.2f}\nReajuste ganho: {valor * dic[i]:.2f}\nEm percentual: {dic[i] * 100:.0f} %')

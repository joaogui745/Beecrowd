# PUM
contador = 0
valores = [1, 2, 3]
linhas = int(input())
while contador < linhas:
    print(f'{valores[0]} {valores[1]} {valores[2]} PUM')
    valores = [x + 4 for x in valores]
    contador += 1
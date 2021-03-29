# Quadrant
quebra = False
dic = {'pp':'primeiro', 'np':'segundo', 'nn':'terceiro', 'pn':'quarto'}
while True:
    quadrante = ''
    valores = input().split()
    for valor in range(len(valores)):
        valores[valor] = int(valores[valor])
        if valores[valor] > 0:
            quadrante += 'p'
        elif valores[valor] < 0:
            quadrante += 'n'
        else:
            quebra = True

    if quebra:
        break
    print(f'{dic[quadrante]}')
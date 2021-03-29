# Ascending and Descending
while True:
    valores = input().split()
    valores = [int(x) for x in valores]
    if valores[0] < valores[1]:
        print('Crescente')
    elif valores[0] > valores[1]:
        print('Decrescente')
    else:
        break

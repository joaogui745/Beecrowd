# Sequence of Numbers and Sum
while True:
    valores = input().split()
    valores = [int(x) for x in valores]
    if valores[0] <= 0 or valores[1] <= 0:
        break
    valores.sort()
    soma = 0
    sequencia = ''
    for valor in range(valores[0], valores[1] + 1):
        sequencia += str(valor) + ' '
        soma += valor
    
    print(f'{sequencia}Sum={soma}')
# Sequência Lógica
contador = 1
linhas = int(input())
while contador <= linhas:
    print(f'{contador} {contador ** 2} {contador ** 3}')
    print(f'{contador} {contador ** 2 + 1} {contador ** 3 + 1}')
    contador += 1
lista = []
contador = 0
for valor in range(6):
    dado = float(input())
    if dado > 0:
        contador += 1
        lista.append(dado)

print(f'{contador} valores positivos\n{(sum(lista)) / len(lista):.1f}')

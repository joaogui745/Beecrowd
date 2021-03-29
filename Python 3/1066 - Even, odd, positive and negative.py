lista = []
for i in range(5):
    dado = float(input())
    if dado > 0:
        lista.append('p')
    elif dado < 0:
        lista.append('n')
    if dado % 2 == 0:
        lista.append('a')
    else:
        lista.append('i')

print(f"{lista.count('a')} valor(es) par(es)\n{lista.count('i')} valor(es) impar(es)\n{lista.count('p')} valor(es) positivo(s)\n{lista.count('n')} valor(es) negativo(s)")
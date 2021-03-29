#1042 Simple sort
valores = input().split()
novos_valores = tuple(valores)


for i in range(3):
    valores[i] = int(valores[i])

for j in range(3):
    for k in range(j + 1, 3):
        if valores[j] > valores[k]:
            valores[k], valores[j] = valores[j], valores[k]
        
print(f'{valores[0]}\n{valores[1]}\n{valores[2]}\n')
print(f'{novos_valores[0]}\n{novos_valores[1]}\n{novos_valores[2]}')
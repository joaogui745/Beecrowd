valores = []
# 1079 Weighted average
linhas = int(input())
for valor in range(linhas):
    dado = input().split()
    for nota in range(3):
        if nota == 0:
            dado[nota] = float(dado[nota]) * 2
        elif nota == 1:
            dado[nota] = float(dado[nota]) * 3
        else:
            dado[nota] = float(dado[nota]) * 5

    valores.append(sum(dado) / 10)

for valor in range(linhas):
    print(f'{valores[valor]:.1f}')
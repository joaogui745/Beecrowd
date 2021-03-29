# 1080 Highest and position
maior = 0
i_maior = 0
for valor in range(1, 101):
    entrada = int(input())
    if entrada > maior:
        i_maior = valor
        entrada, maior = maior, entrada
    
print(f'{maior}\n{i_maior}')


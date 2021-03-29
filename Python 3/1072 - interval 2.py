# 1072 interval 2
cont_in = 0
index = int(input())
for dado in range(index):
    valor = int(input())
    if valor >= 10 and valor <= 20:
        cont_in += 1

print(f'{cont_in} in\n{index - cont_in} out')
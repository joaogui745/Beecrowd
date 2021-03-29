# Tipo de Combustível
dic = {'1':0,'2':0,'3':0}
while True:
    comb = input()
    if comb in dic:
        dic[comb] += 1
    elif comb == '4':
        break
print(f"MUITO OBRIGADO\nAlcool: {dic['1']}\nGasolina: {dic['2']}\nDiesel: {dic['3']}")
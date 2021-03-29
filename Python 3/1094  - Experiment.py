# 1094 Experiment
total = 0
experimentos = int(input())
dic = {'R':0, 'C':0, 'S':0}
for exp in range(experimentos):
    numero, animal = input().split()
    dic[animal] += int(numero)
    total += int(numero)

print(f"Total: {total} cobaias\nTotal de coelhos: {dic['C']}\nTotal de ratos: {dic['R']}\nTotal de sapos: {dic['S']}")

print(f"Percentual de coelhos: {dic['C'] * 100 / total:.2f} %\nPercentual de ratos: {dic['R'] * 100 / total:.2f} %\nPercentual de sapos: {dic['S'] * 100 / total:.2f} %")
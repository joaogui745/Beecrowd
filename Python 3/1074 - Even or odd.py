# 1074 Even or odd
valores = []
linhas = int(input())
for valor in range(linhas):
    car = ''
    dado = int(input())
    if dado == 0:
        car = 'NULL'
    else:
        if not dado % 2 == 0:
            car = 'ODD'
        else:
            car = 'EVEN'
            
        if dado > 0:
            car += ' POSITIVE'
        else:
            car += ' NEGATIVE'
            
    valores.append(car)

for numero in range(linhas):
    print(valores[numero])
    
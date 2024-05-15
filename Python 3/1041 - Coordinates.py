#1041 Coordinates
valores = input().split()

X = float(valores[0])
Y = float(valores[1])

if X == 0.0 or Y == 0.0:
    if X != 0:
        print('Eixo X')
    elif Y != 0:
        print('Eixo Y')
    else:
        print('Origem')
elif X > 0 and Y > 0:
    print('Q1')
elif X < 0 and Y > 0:
    print('Q2')
elif X < 0 and Y < 0:
    print('Q3')
else:
    print('Q4')
#1061 Event Time
from datetime import datetime
dia = int(input().split()[1])
hora, minu, seg = input().split(' : ')

inicio = datetime(2020, 4, dia, int(hora), int(minu), int(seg))

dia2 = int(input().split()[1])
hora2, minu2, seg2 = input().split(' : ')

final = datetime(2020, 4, dia2, int(hora2), int(minu2), int(seg2))

duracao = inicio - final

print(duracao)
#Relógio Antigo
while True:
    try:
        horas, minutos = [int(x) for x in input().split()]
        print(f'{int(horas / 30):02}:{int(minutos / 6):02}')
    except EOFError:
        break
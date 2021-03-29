# A Mudança
while True:
    try:
        dic = {0:'Bom Dia!!',
               1:'Boa Tarde!!',
               2:'Boa Noite!!',
               3:'De Madrugada!!',
               4:'Bom Dia!!'}
        
        valores = [89, 179, 269, 359]
        angulo = float(input())
        valores.append(angulo)
        valores.sort()
        print(dic[valores.index(angulo)])
        novo_angulo = angulo + 90
        segundos = novo_angulo * 240
        horas = segundos // 3600
        segundos -= (horas * 3600)
        minutos = segundos // 60
        segundos -= (minutos * 60)
        if horas == 24:
            horas = 0
        elif horas > 24:
            horas -= 24
        print(f'{int(horas):02}:{int(minutos):02}:{int(segundos):02}')
        
    except EOFError:
        break
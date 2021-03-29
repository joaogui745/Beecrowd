def calcula_media():
    quebra = 0
    soma = 0
    while True:
        score = float(input())
        if score < 0 or score > 10:
            print('nota invalida')
        else:
            quebra += 1
            soma += score
            
        if quebra >= 2:
            print(f'media = {soma / 2:.2f}')
            break

# inicio do programa

calcula_media()


while True:
    continua = input('novo calculo (1-sim 2-nao)\n')
    if continua == '1':
        calcula_media()
    elif continua == '2':
        break
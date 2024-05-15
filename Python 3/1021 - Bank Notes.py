def moeda_nota(indice):
    if indice >= 7:
        return 'moeda'
    else:
        return 'nota'

moedas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 50, 25, 10, 5, 1]

valores =  input().split('.')

valor_int = int(valores[0])

valor_fra = int(valores[1])

i = 1

print('NOTAS:')

for moeda in moedas:
    if i <= 7:
        print(f'{valor_int // moeda:.0f} {moeda_nota(i)}(s) de R$ {moeda:.2f}')
        valor_int %= moeda
        i += 1
        if i == 7 :
            print('MOEDAS:')
    else:
        print(f'{valor_fra // moeda:.0f} moeda(s) de R$ {moeda / 100:.2f}')
        valor_fra %= moeda
    
    
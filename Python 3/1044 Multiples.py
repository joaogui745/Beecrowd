#1044 Multiples
valores = input().split()

for i in range(2):
    valores[i] = int(valores[i])

if valores[0] > valores[1]:
    valores[0], valores[1] = valores[1], valores[0]
        
if valores[1] % valores[0] == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')

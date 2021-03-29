#1050 DDD
numeros = {61:'Brasilia', 71:'Salvador', 11:'Sao Paulo', 21:'Rio de Janeiro', 32:'Juiz de Fora', 19:'Campinas', 27:'Vitoria', 31:'Belo Horizonte'}
valor = int(input())
if valor in numeros:
    print(numeros[valor])
else:
    print('DDD nao cadastrado')
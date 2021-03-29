# Hora da corrida
from math import ceil
porcentagem = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
voltas, placas = [int(x) for x in input().split()]
lista = list(map(lambda x: ceil((voltas * placas) * x), porcentagem))
print(*lista, end='\n')
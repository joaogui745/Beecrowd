#Fibonacci em Vetor
teste = int(input())
indices = [int(input()) for x in range(teste)]
lookup = set(indices)
valores = {}
ultimo = 1
penultimo = 0

if 1 in lookup:
    valores[ultimo] = ultimo
if 0 in lookup:
    valores[penultimo] = penultimo
    
for indice in range(2, max(indices) + 1):
    atual = penultimo + ultimo
    if indice in lookup:
        valores[indice] = atual
    penultimo, ultimo = ultimo, atual

for indice in indices:
    print(f'Fib({indice}) = {valores[indice]}')


    




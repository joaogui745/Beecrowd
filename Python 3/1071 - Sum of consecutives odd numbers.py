#1071 Sum of consective odd numbers
lista = []
teto = int(input()) 
fundo = int(input()) + 1

for dado in range(fundo, teto):
    if not dado % 2 == 0:
        lista.append(dado)

print(sum(lista))
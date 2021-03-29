# Odd numbers
valor = int(input())
valor += 1
for dado in range(1, valor):
    if not dado % 2 == 0:
        print(dado)
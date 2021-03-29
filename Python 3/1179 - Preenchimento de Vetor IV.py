#Preenchimento de Vetor IV
pares = impares = []
for i in range(15):
    valor = int(input())
    if valor % 2 == 0:
        pares.append(valor)
        if len(pares) >= 3:
            [print(x) for x in pares]
            
        
        
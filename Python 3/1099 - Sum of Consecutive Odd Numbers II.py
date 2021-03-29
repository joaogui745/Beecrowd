# Sum of Consecutive Odd Numbers II
casos =int(input())
singulares = 0
soma = []

for caso in range(casos):
    lista = input().split()
    lista = [int(x) for x in lista]
    lista.sort()
    if lista[0] + 1 == lista[1] or lista[0] == lista[1]:
        soma.append(0)
    
    else:
        for numero in range(lista[0] + 1,lista[1]):
            if not numero % 2 == 0:
                singulares += numero
        
        soma.append(singulares)
                
        singulares = 0

[print(x) for x in soma]

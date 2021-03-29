# Grenais
def calcula_grenal(lista):
    inter = 0
    gremio = 0
    empate = 0
    for i in range(len(lista)):
        for j in range(2):
            lista[i][j] = int(lista[i][j])
        if lista[i][0] > lista[i][1]:
            inter += 1
        elif lista[i][0] < lista[i][1]:
            gremio += 1
        else:
            empate += 1
    
    print(f'{len(lista)} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{empate}')
    
    if gremio < inter:
        print('Inter venceu mais')
    elif gremio > inter:
        print('Gremio venceu mais')
    else:
        print('Nao houve vencedor')

# inicio do programa
lista_grenais = []
lista_grenais.append(input().split())
while True:
    novo_grenal = input('Novo grenal (1-sim 2-nao)\n')
    if novo_grenal == '1':
        lista_grenais.append(input().split())
    else:
        break

calcula_grenal(lista_grenais)
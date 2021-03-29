# As Moedas de Robbie

def ehprimo(n):
    if n == 1:
        return False

    for numero in range(2, n):
        if n % numero == 0:
            return False
        
    return True

#Início do programa
    
while True:
    try:
        linhas = int(input())
        valores = []
        for entrada in range(linhas):
            
            valores.append(int(input()))

        pulo = int(input())

        valor = sum([ valores[-x] for x in range(1, linhas + 1, pulo)])

        if ehprimo(valor):
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')
        
    except EOFError:
        break






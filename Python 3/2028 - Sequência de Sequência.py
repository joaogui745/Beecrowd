# Sequência de Sequência
dic = {}
caso = 1
while True:
    try:
        valor_dado = int(input())
        if valor_dado in dic:
            qtd = dic[valor_dado][0]
            numero = dic[valor_dado][1]
        else:
            numero = [0]
            qtd = 1
            for i in range(1, valor_dado + 1):
                qtd += i
                for x in range(i):
                    numero.append(i)
            dic[valor_dado] = [qtd, numero]
        
        print(f'Caso {caso}: {qtd} numero{"s" if qtd > 1 else ""}')
        print(*numero, end='\n\n')
        caso += 1
    except EOFError:
        break
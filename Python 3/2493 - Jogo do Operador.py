# Jogo do Operador
def calcula_tudo(string):
    AeB = string.split('=')[0]
    C = int(string.split('=')[1])
    if C == eval(AeB.replace(' ', '+')):
        return False
    if C == eval(AeB.replace(' ', '-')):
        return False
    if C == eval(AeB.replace(' ', '*')):
        return False
    return True
    
    
while True:
    pessoas = ''
    acertou = []
    qtd = int(input())
    expressoes = [input() for x in range(qtd)]
    respostas = [input() for x in range(qtd)]
    
    for r in range(qtd):
        if respostas[r][-1] != 'I':
            indice = int((respostas[r]).split()[1]) - 1
            equacao, resultado = expressoes[indice].split('=')
            equacao = equacao.replace(' ', respostas[r][-1])
            acertou.append((eval(equacao) == int(resultado)))
        else:
            indice = int((respostas[r]).split()[1]) - 1
            acertou.append(calcula_tudo(expressoes[indice]))
    acertos = sum(acertou)
    if acertos == 0:
        print('None Shall Pass!')
    elif acertos == qtd:
        print('You Shall All Pass!')
    else:
        acertados = [respostas[x].split()[0] for x in range(qtd) if not acertou[x]]
        acertados.sort()
        for pessoa in acertados:
            pessoas += ' ' + pessoa
        print(pessoas.lstrip())
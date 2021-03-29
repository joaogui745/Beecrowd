# Fixed Password
while True:
    senha = 2002
    senha_dada = int(input())
    if not senha_dada == senha:
        print('Senha Invalida')
    else:
        print('Acesso Permitido')
        break
# Crescimento Populacional
casos_teste = int(input())

for valor in range(casos_teste):
    
    anos = 0 
    valores = input().split()
    pa = int(valores[0])
    pb = int(valores[1])
    ga = float(valores[2]) / 100
    gb = float(valores[3]) / 100
    
    while pa <= pb and anos <= 101:
        
        pa = int(pa * (1 + ga))
        pb = int(pb * (1 + gb))
        anos += 1
        
    if anos <= 100:
        print(f'{anos} anos.')
    else:
        print('Mais de 1 seculo.')
        
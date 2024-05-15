#1046 Game Time

valores = input().split()

A = int(valores[0])
B = int(valores[1])
C = int(valores[2])
D = int(valores[3])

if A == C:
    if D > B:
        delta_minutos = D - B
        delta_horas = 0
    else:
        delta_minutos = (60 - B) + D
        delta_horas = C + (24 - (A + 1))
        if delta_minutos >= 60:
            delta_horas += (delta_minutos // 60)
            delta_minutos = (delta_minutos % 60)
        

if C > A:
    delta_minutos = (60 - B) + D
    delta_horas = C - (A + 1)
    if delta_minutos >= 60:
        delta_horas += (delta_minutos // 60)
        delta_minutos = (delta_minutos % 60)
if C < A:
    delta_minutos = (60 - B) + D
    delta_horas = C + (24 - (A + 1))
    if delta_minutos >= 60:
        delta_horas += (delta_minutos // 60)
        delta_minutos = (delta_minutos % 60)

print(f'O JOGO DUROU {delta_horas} HORA(S) E {delta_minutos} MINUTO(S)')
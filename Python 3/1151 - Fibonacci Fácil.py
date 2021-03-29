# Fibonacci Fácil
seq = int(input())
dic = {0:0, 1:1, 2:1}
fibonacci = []

for valor in range(seq):
    if valor <= 2:
        fibonacci.append(dic[valor])
    else:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
print(*fibonacci)    
    


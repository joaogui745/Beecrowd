# Ultrapassando Z
X = int(input())
while True:
    Z = int(input())
    if Z > X:
        break

contador = 2

while X < Z:
    X += X + 1
    contador += 1

print(contador)
    
    
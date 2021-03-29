# Quanta Mandioca?

dic = {
    1:300,
    2:1500,
    3:600,
    4:1000,
    5:150,
}

mandioca = 225 + sum([ dic[i] * int(input()) for i in range(1, 6)])

print(mandioca)

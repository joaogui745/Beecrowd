# 1049 Animal
animais = {'vertebrado':{'ave':{'carnivoro':'aguia', 'onivoro':'pomba'}, 'mamifero':{'onivoro':'homem', 'herbivoro':'vaca'}}, 'invertebrado':{'inseto':{'hematofago':'pulga', 'herbivoro':'lagarta'}, 'anelideo':{'hematofago':'sanguessuga', 'onivoro':'minhoca'}}}

A = input()
B = input()
C = input()

print(f'{animais[A][B][C]}')
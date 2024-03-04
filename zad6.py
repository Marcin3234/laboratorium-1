lista_slow = ["agrafka", "anonim", "ławka", "owoc", "białko"]

slowa_na_a = list(filter(lambda x: x.startswith('a'), lista_slow))

print(slowa_na_a)


lista_liczb = [1, 2, 3, 4, 5]

kwadraty_liczb = list(map(lambda x: x**2, lista_liczb))

print(kwadraty_liczb)
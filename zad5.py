parzyste_elementy = lambda lista: list(filter(lambda x: x % 2 == 0, lista))

lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wynik = parzyste_elementy(lista_liczb)

print(wynik)

pole_prostokata = lambda a, b: a * b

dlugosc_boku_a = 5
dlugosc_boku_b = 10
wynik_pola = pole_prostokata(dlugosc_boku_a, dlugosc_boku_b)

print(wynik_pola)
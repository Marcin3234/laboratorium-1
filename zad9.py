from functools import reduce
def znajdz_najwieksza(liczby):
    return reduce(lambda x, y: x if x > y else y, liczby)
def oblicz_srednia(liczby):
    suma = reduce(lambda x, y: x + y, liczby)
    return suma / len(liczby) if len(liczby) > 0 else 0

lista_liczb = [3, 8, 1, 6, 2, 9, 4]

najwieksza = znajdz_najwieksza(lista_liczb)
srednia = oblicz_srednia(lista_liczb)
print("Największa liczba:", najwieksza)
print("Średnia z listy liczb:", srednia)
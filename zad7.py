def podnies_do_kwadratu(x):
    return x ** 2

def dodaj_piec(x):
    return x + 5

def funkcje(lista_funkcji, wartosc):
    for funkcja in lista_funkcji:
        wartosc = funkcja(wartosc)
    return wartosc

liczby = [2, 4, 6]

wyniki = [funkcje([podnies_do_kwadratu, dodaj_piec], liczba) for liczba in liczby]

print(wyniki)
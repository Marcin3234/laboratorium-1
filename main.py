print("ZADANIE 1")
#range
for h in range(10):
    print(h)
#help
def p(r):
    '''
    Funkcja pokazująca helpa
    '''

help(p)
#chr zamienia na ASCII
print("Funkcja chr",chr(89))
#hash zwraca wartosc hash
print("Funkcja hash",hash(p))
#abs liczba bezwgledna
print("Funkcja abs",abs(h))

print("ZADANIE 2")
def a(b):
    print("wywołana funkcja a to:",b)
print(a(5))

print("ZADANIE 3")
def a(b):
    print("wywołana funkcja a",b)
print(a(2))

print("ZADANIE 4")
def fun1(text):
    print(text)
def fun2(super, arg="super"):
    print("jesteś")
    super(arg)
    print("duży")
print("START")
fun2(fun1, "Tekst do funkcji wewnetrznej")
print("KONIEC")


print("ZADANIE 5")

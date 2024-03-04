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
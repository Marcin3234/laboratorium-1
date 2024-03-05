def kwadrat(x):
    return x * x

lista = [1, 2, 3, 4, 5]
squared_numbers = list(map(kwadrat, lista))

print(squared_numbers)
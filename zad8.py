from functools import reduce
lista  = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, lista)

print(sum_of_numbers)
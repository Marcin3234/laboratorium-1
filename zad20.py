def analiza(data):
    match data:
        case (x, y):
            return f"Tuple with elements {x} and {y}"
        case [x, y, z]:
            return f"List with elements {x}, {y}, and {z}"
        case _:
            return "Unknown type"

print(analiza((1, 2)))
print(analiza([1, 2, 3]))
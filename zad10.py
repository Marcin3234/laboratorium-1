def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_gen = fibonacci_generator()
for _ in range(10):
    print(next(fibonacci_gen))

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

large_file_path = 'duzy_plik.txt'
line_generator = read_large_file(large_file_path)

for line in line_generator:
    print(line)
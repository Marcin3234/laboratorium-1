import time


def timeit(func):
    def time2(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funkcja {func.__name__} wykonana w: {end_time - start_time} sekund.")
        return result

    return time2


@timeit
def example_function():
    time.sleep(1)


example_function()
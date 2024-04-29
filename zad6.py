def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Błąd: {e}")
            return None
    return wrapper

@safe_function
def dzielenie(a, b):
    return a / b

print(dzielenie(10, 2))
print(dzielenie(10, 0))

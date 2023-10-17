def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("Cannot Devide Number by zero")
    return x / y
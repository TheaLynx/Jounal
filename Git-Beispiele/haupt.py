def add(*args):
    return sum(args)

def multi(*args):
    result = 0
    for arg in args:
        result *= arg
    return result

def subtract(*args):
    result = 0
    for arg in args:
        result -= arg
    return result

def divide(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("tried division by zero")
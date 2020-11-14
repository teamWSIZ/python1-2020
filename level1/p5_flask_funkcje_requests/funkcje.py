def add(a, b):
    return a + b


def diff(a, b):
    return a - b


def calculate(a, b, fff):
    return fff(a, b)


def greater1(a, b):
    if a < b:
        return a
    else:
        return b


def greater2(a, b):
    return a if a < b else b


print(add(5, 7))
print(diff(5, 7))

print(calculate(5, 7, add))  # przekazaliśmy funkcję `add` jako parametr do funkcji `calculate`
print(calculate(5, 7, diff))
print(calculate(5, 7, lambda a, b: a * b))  # to jest tzw. funkcja nienazwana/funkcja lambda...
print(calculate(5, 7, lambda a, b: a if a < b else b))

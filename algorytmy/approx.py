"""
Problem: znaleźć takie "x", że f(x) = x**3 + x == 1

"""


def f(x):
    return x ** 4 + x


bmi = 0
bmx = 10  # to jest napewno więcej niż poszukiwany x
b = (bmi + bmx) / 2

while bmx - bmi > 10**(-10):
    print(f'bmi={bmi} b={b} bmx={bmx}', end='')
    if f(b) > 1:
        bmx = b
        print(' ←')
    else:
        bmi = b
        print(' →')
    b = (bmi + bmx) /2

print(f'dla x={b}, mamy f(x)={f(b)}')

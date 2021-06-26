"""
Problem: znaleźć takie "sim_annealing", że f(sim_annealing) = sim_annealing**3 + sim_annealing == 1

"""


def f(x):
    return x ** 4 + x


bmi = 0
bmx = 10  # to jest napewno więcej niż poszukiwany sim_annealing
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

print(f'dla sim_annealing={b}, mamy f(sim_annealing)={f(b)}')

from _algorytmy.utils import ts

st = ts()
x = 0
for t in range(10 ** 3):
    w = [0] * (10 ** 6)
    x += len(w)

print(x, f'{ts()-st:.3f}s')

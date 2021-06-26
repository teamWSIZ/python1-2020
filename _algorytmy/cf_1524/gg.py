from _algorytmy.utils import ts

w = [0] * (10**4)
st = ts()
for i in range(10000):
    a = w.copy()

en = ts()
print(f'{en-st:.3f}s')

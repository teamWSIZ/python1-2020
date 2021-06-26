"""
W jaki sposób z dużego zbioru losować elementy.

np.
w = [....]
len(w) = 10000

... chcemy przeszukać podzbiory `w` ... jakoś losowo...

"""
from random import choice, shuffle, seed, randint

from _algorytmy.utils import ts


def my_shuffle(ww, k=100):
    for i in range(k):
        # zamienimy ze sobą dwa elementy ww
        a = randint(0, len(ww) - 1)
        b = randint(0, len(ww) - 1)
        t = ww[a]
        ww[a] = ww[b]
        ww[b] = t


N = 10 ** 5
seed(111)

w = [randint(0, N) for _ in range(N)]
st = ts()
for i in range(300):
    # shuffle(w)
    my_shuffle(w)

en = ts()
print(f'{en - st:.3f}ms')

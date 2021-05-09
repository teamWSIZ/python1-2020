from bisect import bisect_left, bisect_right

from algorytmy.utils import ts

w = [1, 4, 8, 10, 50]
x = 10

i = bisect_left(w, x) # 3
print(i)
print(w[i])     # 10

from random import randint

w = [randint(0, 10 ** 8) for i in range(10 ** 6)]

w.sort()
st = ts()
for i in range(1000):
    x = bisect_left(w, 123456)
en = ts()
print(f'Elapsed: {(en-st)*1000:.3f} ms')

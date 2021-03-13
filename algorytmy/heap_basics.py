from heapq import heappush, heappop

from algorytmy.utils import ts, delta

h = []
heappush(h, 5)
heappush(h, 2)
heappush(h, 2)
heappush(h, 15)
heappush(h, 1)

while len(h) > 0:
    print(heappop(h))

from random import randint, seed

seed(5)
N = 2 ** 20
w = [randint(1, 100000) for i in range(N)]

st = ts()
hs = set()  # slower!
for x in w:
    heappush(h, x)
    # hs.add(x)

en = ts()
delta(st, en)

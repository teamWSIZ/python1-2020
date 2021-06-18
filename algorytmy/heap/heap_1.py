# Struktura do której można szybko dodawać elementy...
# i która zawsze podaje b. szybko jaki jest najmniejszy element w zbiorze...

# PriorityQueue
from heapq import heappush, heappop
from random import randint, seed

from algorytmy.utils import ts, delta

h = []

# heappush(h, 10)
# heappush(h, 1)
# heappush(h, 20)
# heappush(h, -1)
#
# while len(h) > 0:
#     print(heappop(h))

N = 2 ** 22
seed(5)
w = [randint(1, 10 ** 8) for _ in range(N)]

st = ts()

# w.sort()
# ss = set()
for x in w:
    heappush(h, x)
#     ss.add(sim_annealing)
en = ts()
delta(st, en)

"""
N = 2**22
set: 680ms
sort: 980ms
heap: 402ms
"""
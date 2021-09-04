from random import randint, seed
from typing import List


def solve(x, t):
    rights = []
    lefts = []
    for i, v in enumerate(x):
        if t[i] == 'R':
            rights.append(i)
        else:
            if len(rights) > 0:
                pickedIndex = rights.pop()
                print(f'exploded: {pickedIndex}↔{i}')
            else:
                lefts.append(i)
    print(f'pozostałe: lefts:{lefts}, rights: {rights}')


def reduce(lefts: List[int]):
    """
    Reduces all remaining left-going robots -- they will explode among themselves. 0↔1, 2↔3 etc...
    at most 1 will remain
    :param lefts:
    :return:
    """
    for u, v in zip(lefts[0::2], lefts[1::2]):
        dist = u + v
        print(f'zderzenie {u}↔{v} z dystansem={dist}')


def generate(n, m):
    s = set()
    x = []
    while len(x) < n:
        p = randint(0, m // 2)
        if p in s:
            continue
        s.add(p)
        x.append(p * 2)

    w = ['R' if randint(0, 1) == 0 else 'L' for _ in range(n)]
    t = ''.join(w)
    return x, t


seed(111)
# x, t = generate(7, 20)
# x.sort()
# print(x, t)
# solve(x, t)

w = [2, 4, 6, 8]
reduce(w)
m = 9
w_reversed = sorted([m - v for v in w])
print(w)
print(w_reversed)
reduce(w_reversed)

"""
Krok 1: uruchomić solve ↑↑, przez co z układu robotów ()()())))(()))(()() powstanie coś typu )))(
Krok 2: idące w lewo roboty parami się pozderzają (funkcja reduce), zostanie ewentualnie ostatni (nieparzysty)
Krok 3: ----||---- prawo roboty się pozderzają ... zostanie (może) jeden...
Krok 4: ew. wykonać zderzenie pozostałych dwóch robotów... 


"""


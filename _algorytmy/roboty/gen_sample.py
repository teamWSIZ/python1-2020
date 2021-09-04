# x = [5, 10, 15, 13]
# t = 'RLRL'

# Dane tylko na parzystych pozycjach
from random import randint


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


print(generate(5, 10))

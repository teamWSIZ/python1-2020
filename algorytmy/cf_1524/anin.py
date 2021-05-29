import sys
from typing import List

input = sys.stdin.readline


def ri(): return [int(i) for i in input().split()]


def rs(): return input().split()[0]


"""
1

4 2 3 1 1
1 3
"""


def read_test_case():
    x = ri()
    n = x[0]
    w = [i for i in x[1:]]
    x = ri()
    k = x[0]
    ma = [i - 1 for i in x[1:]]

    edges = ri()[0]

    ch: List[List[int]] = [[] for _ in range(n)]
    pa: List[List[int]] = [[] for _ in range(n)]

    for _ in range(edges):
        u, v = ri()
        # połączenie od `u-1` do `v-1`
        ch[u - 1].append(v - 1)
        pa[v - 1].append(u - 1)
    return n, w, ma, ch, pa


def print_test_case(n, w, ma, ch, pa):
    print(f'n={n} w={w}')
    print(f'k={len(ma)} ma={ma}')
    for i in range(n):
        print(i, ' → ', *ch[i])
    for i in range(n):
        print(i, ' ← ', *pa[i])


if __name__ == '__main__':
    # g = ri()[0]
    # ri()
    n, w, ma, ch, pa = read_test_case()
    print_test_case(n, w, ma, ch, pa)
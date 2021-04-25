from typing import Set

from algorytmy.utils import ts, delta
from hash_utils import *
# from utils import ts, delta

MOD = 1000000007


def long(a: str, b: str):
    # założenie: len(a)<len(b)
    if len(a) > len(b):
        return '!'
    n = len(b)
    for sublen in range(len(a), 0, -1):
        for start in range(1 + sublen):
            if start + sublen > n:
                break
            if b.__contains__(a[start:start + sublen]):
                return a[start:start + sublen]


def get_hashes(s, sublen):
    # znajduje wszystkie hash-e dla substring-ów długości `sublen`
    hashes = set()
    roll_p = 1234
    ppow = get_ppow(roll_p, sublen)

    if len(s) >= sublen:
        h = compute_hash(s, roll_p, MOD)
        hashes.add(h)
        for i in range(1, len(s) - sublen):
            h = shift_hash(h, ppow, MOD, roll_p, s[i + sublen], s[i - 1])
            hashes.add(h)
    return hashes


def faster(a: str, b: str):
    if len(a) > len(b):
        return '!'
    n = len(b)
    # Zadanie do wykonania: chcemy zrobić binary search po sublen.....; sublen=1 jest napewno OK, sublen=len(a) napewno zły
    mi_sublen = 1
    mx_sublen = len(a)
    sublen = (mi_sublen + mx_sublen) // 2
    best_start = -1
    while mx_sublen - mi_sublen > 1:
        found = False
        for start in range(n - sublen + 1):
            if b.__contains__(a[start:start + sublen]):
                found = True
                best_start = start
                break
        if found:
            mi_sublen = sublen
        else:
            mx_sublen = sublen
        sublen = (mi_sublen + mx_sublen) // 2
    return sublen


def fast_hash_solution(a: str, b: str):
    if len(a) > len(b):
        return '!'
    mi_sublen = 1
    mx_sublen = len(a)
    sublen = (mi_sublen + mx_sublen) // 2
    best_start = -1
    while mx_sublen - mi_sublen > 1:
        found = False

        a_hashes: Set = get_hashes(a, sublen)
        b_hashes: Set = get_hashes(b, sublen)

        for h in a_hashes:
            if h in b_hashes:
                found = True
                break
        if found:
            mi_sublen = sublen
        else:
            mx_sublen = sublen
        sublen = (mi_sublen + mx_sublen) // 2
    return sublen


# [!!!!!!!!!!!!...................]
# ---> O(N * log(N))

letters = 26
LEN = 1600
st = ts()
a = random_string(nsymbols=letters, length=LEN)
b = random_string(nsymbols=letters, length=LEN)
# gg = long(random_string(nsymbols=NS, length=LEN), random_string(nsymbols=NS, length=LEN))
# gg = faster(a, b)
gg = fast_hash_solution(a, b)
ed = ts()
delta(st, ed)

"""
Simple algo, O(N**3)

100     1.571
200     7.853
300     24.333
400     50.992
600     160.7
800     366.106
1600    2631.371
3200    19903

Faster,  N**2 log(N)
1600    12.895
3200    47.498
6400    206.809
12800   840.949
25600   3624.133
51200   15974

Hash-Based solution N log(N)

1600    19
3200    42
6400    88
12800   194
25600   410
51200   740
102400  886
204800  1653
409600  3010
819200  5678
1000000 6931

"""

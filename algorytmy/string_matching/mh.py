from datetime import datetime
from random import randint

from algorytmy.utils import delta


def ts():
    return datetime.now().timestamp()


def random_string(nsymbols, length):
    num = []
    for i in range(length):
        num.append(chr(randint(0, nsymbols - 1) + 97))  # 'a' + ...
    return ''.join(num)


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
    return a[best_start:best_start + sublen]


# [!!!!!!!!!!!!...................]
# ---> O(N * log(N))

NS = 6
LEN = 3200
st = ts()
# gg = long(random_string(nsymbols=NS, length=LEN), random_string(nsymbols=NS, length=LEN))
gg = faster(random_string(nsymbols=NS, length=LEN), random_string(nsymbols=NS, length=LEN))
ed = ts()
delta(st, ed)

"""
100     1.571
200     7.853
300     24.333
400     50.992
600     160.7
800     366.106
1600    2631.371
3200    19903
"""

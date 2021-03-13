import math
from datetime import datetime
from typing import Tuple


def ts():
    return datetime.now().timestamp()


def find_fraction(x: float, mx_ab=100) -> Tuple[int, int]:
    # TO jest O(N^2)
    best = 10000000
    res = (0, 0)
    st = ts()
    for a in range(1, mx_ab):
        for b in range(1, mx_ab):
            y = a / b
            if abs(x - y) < best:
                best = abs(x - y)
                res = (a, b)
    ed = ts()
    print(f'execution time: {(ed - st) * 1000:.3f} ms')
    return res


def find_fraction_binary_search(x: float, mx_ab=100) -> Tuple[int, int]:
    # TO jest O(N^2)
    best = 10000000
    res = (0, 0)
    st = ts()
    for a in range(1, mx_ab):
        b_mi = 1
        b_mx = mx_ab  # ten b napewno jest za duży, tzn. wyznaczona liczba jest za mała
        b = (b_mx + b_mi) // 2
        print(f'rozpoczynam szukanie dla a={a}')
        while b_mx - b_mi > 1:
            print(f'bmi={b_mi} b={b} bmx={b_mx}', end='')
            y = a / b
            print(f' y={y:.2f}', end='')
            if y > x:
                b_mi = b
                print(' →')
            else:
                b_mx = b
                print(' ←')
            b = (b_mi + b_mx) // 2

        # tutaj b, b-1 i b+1 są najlepszymi mianownikami...
        w = [b - 1, b, b + 1]
        for b in w:
            if b == 0:
                continue
            y = a / b
            if abs(x - y) < best:
                best = abs(x - y)
                res = (a, b)
    ed = ts()
    print(f'execution time: {(ed - st) * 1000:.3f} ms')
    return res


find_fraction_binary_search(3.141592, 129)

# for i in range(4, 20):
# print(f'mxab={2**i}', find_fraction(3.141592, 2**i))
# print(f'mxab={2**i}', find_fraction_binary_search(3.141592, 2**i))


# w = [3 / b for b in range(1, 100)]
# print(w)

# print(find_fraction_binary_search(3.141592, 100))

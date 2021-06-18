# for sim_annealing in range(0, 1000):
#     for y in range(0, 1000):
#         if sim_annealing ** 2 - y ** 2 == 25:
#             print(sim_annealing, y)
from math import hypot
from typing import Tuple

"""
  Szukamy okręgów przechodzących przez poniższe punkty.
  Wyznaczanie środka okręgu na podstawie:
  https://codeforces.com/blog/entry/17313
"""
points = [(5, 0), (-5, 0), (13, 12), (-13, 12), (13, -12), (-13, -12)]


def v_add(v1, v2) -> Tuple:
    return v1[0] + v2[0], v1[1] + v2[1]


def v_mul(v, alpha: float) -> Tuple:
    return v[0] * alpha, v[1] * alpha


def v_diff(v1, v2) -> Tuple:
    return v_add(v1, v_mul(v2, -1))


def v_len(v) -> float:
    return hypot(*v)


def compute_center(A, B, C) -> Tuple:
    a = v_len(v_diff(B, C))
    b = v_len(v_diff(A, C))
    c = v_len(v_diff(A, B))
    cos_gamma = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    cos_alpha = (c ** 2 + b ** 2 - a ** 2) / (2 * c * b)
    cos_beta = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    denom = a * cos_alpha + b * cos_beta + c * cos_gamma
    xa = a * cos_alpha / denom
    xb = b * cos_beta / denom
    xc = c * cos_gamma / denom
    AA = v_mul(A, xa)
    BB = v_mul(B, xb)
    CC = v_mul(C, xc)
    return round(AA[0] + BB[0] + CC[0], 3), round(AA[1] + BB[1] + CC[1], 3)


# testy
# print(compute_center((-1, 0), (0, 1), (0, -1)))
# print(compute_center((0, 1), (1, 0), (1 / 1.4142, 1 / 1.4142)))
print(points)

for i in range(0, 6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            print(f'{i}|{j}|{k}| --> {compute_center(points[i], points[j], points[k])}')

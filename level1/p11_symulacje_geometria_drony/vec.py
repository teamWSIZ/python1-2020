from copy import copy
from math import hypot, sqrt
from typing import List

"""
Prosty pakiet funkcji do geometrii.
Działa na 2D, 3D etc.
"""

def norm(v) -> float:
    """
    :return: Długość wektora `v`
    """
    return sqrt(sum([a ** 2 for a in v]))


def normalized(v) -> List[float]:
    """
    :param v: Wektor który będzie normalizowany.
    :return: Kopia wektora `v` znormalizowana do jednostkowej długości.
    """
    n = norm(v)
    g = [x / n for x in v]
    return g


def scalar_product(v, w) -> float:
    """
    Dla wektorów (v,w) daje liczbę |v|*|w|*cos(theta), gdzie theta jest kątem między tymi wektorami.
    https://pl.wikipedia.org/wiki/Iloczyn_skalarny
    :param v:
    :param w:
    :return:
    """
    return sum([a * b for (a, b) in zip(v, w)])


def normal(v, axis) -> List[float]:
    """
    Zwraca tą część wektora `v`, która jest równoległa do `axis`.
    :param v:
    :param axis:
    :return:
    """
    n_axis = normalized(axis)
    scalar = scalar_product(v, n_axis)
    return [a * scalar for a in n_axis]


def tangential(v, axis) -> List[float]:
    """
    :param v:
    :param axis:
    :return: Zwraca tą część wektora `v` która jest prostopadła do osi `axis`
    """
    n_v = normal(v, axis)
    return [vv - nn for (vv, nn) in zip(v, n_v)]


if __name__ == '__main__':
    w = [1, 1, 0]
    print(norm(w))
    print(normalized(w))
    v = [0, 1, 0]
    print(scalar_product(w, v))  # powinno być 1

    m = [1, 2, 3]
    print(normal(m, [1, 0, 0]))  # [1.0, 0.0, 0.0]
    print(normal(m, [0, 10, 0]))  # [0.0, 2.0, 0.0]
    print(normal(m, [0, 0, 0.1]))  # [0.0, 0.0, 3.0]

    print(tangential(m, [1, 0, 0]))  # [0.0, 2.0, 3.0]
    print(tangential(m, [0, 1, 0]))  # [1.0, 0.0, 3.0]
    print(tangential(m, [0, 0, 1]))  # [1.0, 2.0, 0.0]

    print(tangential([2, 2, 0], [0, 3, 0]))  # [2.0, 0.0, 0.0]

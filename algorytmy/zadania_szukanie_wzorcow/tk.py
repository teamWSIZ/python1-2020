from random import getrandbits

from algorytmy.utils import ts, delta


def generate_n_lists(n, m):
    start = ts()
    output_lists = []
    x = 107
    for i in range(n):
        temp_list = []
        for j in range(m):
            x = (x * 37 + 103) % 1013
            temp_list.append(1)
        output_lists.append(temp_list)
    end = ts()
    delta(start, end)
    return output_lists


generate_n_lists(10 ** 5, 20)  # 179.584ms

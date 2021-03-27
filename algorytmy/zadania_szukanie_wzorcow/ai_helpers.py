from random import randint
from typing import List

from algorytmy.utils import ts, delta


def num_to_list(x, len):
    res = [0] * len
    for i in range(len):
        res[len - 1 - i] = (x % 2)
        x //= 2
    return res


def gen_lists(n, m):
    maxnumber = (2 ** m)
    numbers = [randint(0, maxnumber) for _ in range(n)]  # 6 ---> [0,1,1,0]
    return [num_to_list(d, m) for d in numbers]


# print(gen_lists(10, 5))

def find_pattern_exact(line: List[int], pattern: List[int]) -> int:
    s_line = ''
    for x in line:
        s_line += str(x)
    s_pattern = ''
    for x in pattern:
        s_pattern += str(x)

    idx = s_line.find(s_pattern)  # tu trzeba sprawdzić czy rzeczywiście szukanie podnapisów w pythonie jest szybkie...
    if idx == -1:
        return 0
    # teraz trzeba sprawdzić czy tylko ten pattern jest tutaj...
    rest = s_line[:idx] + s_line[idx + len(pattern):]
    if int(rest) == 0:
        return 1
    else:
        return 0


st = ts()
# w = gen_lists(10 ** 5, 20)
print(find_pattern_exact([0, 0, 0, 1, 1, 0, 0], [1, 1]))
en = ts()
delta(st, en)

# print('00010'.find('x'))
# print(int('00000100'))

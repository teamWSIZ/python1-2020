from random import randint
from typing import Tuple

from algorytmy.utils import ts, delta


def mfind(tekst: str, pattern: str):
    for st in range(len(tekst)):
        cnt = 0
        for i in range(len(pattern)):
            if st + i >= len(tekst):
                break
            if tekst[st + i] != pattern[i]:
                break
            else:
                cnt += 1
        if cnt == len(pattern):
            return st
    return -1


def run(N: int, M: int) -> Tuple[float, float]:
    # tekst = 'a' * N + 'x'  # prosty powtarzający się tekst -- długo zgodny z pattern
    tekst = ''.join([chr(randint(60, 100)) for _ in range(N)]) #tekst szybko niezgodny z kazdą pattern
    pattern = 'a' * M + 'z'

    st = ts()
    # i = tekst.find(pattern) # używa algorytmu BMH https://stackoverflow.com/questions/681649/how-is-string-find-implemented-in-cpython
    i = mfind(tekst, pattern)
    en = ts()
    return st, en


patt_i = 16
for txt_i in range(2, 20):
    st, en = run((2 ** txt_i), (2 ** patt_i))
    print(txt_i, patt_i, f'{(en - st) * 1000:.3f}ms')

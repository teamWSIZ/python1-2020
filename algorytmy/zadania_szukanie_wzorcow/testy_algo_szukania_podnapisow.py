from random import randint
from typing import Tuple

from algorytmy.utils import ts, delta

"""

txt = aaaaaaaaaaaaaaaaaaaaaaaabcd
pat = aaaaaaaad

O(N * M)


"""

def mfind(tekst: str, pattern: str):
    """
    Dumb idea....

    :param tekst:
    :param pattern:
    :return:
    """
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
    """

    :param N: Długość napisu w którym szukamy
    :param M: Długość patternu który próbujemy znaleźć
    :return:
    """
    # generujemy napis i pattern
    tekst = 'a' * N + 'x'  # prosty powtarzający się tekst -- długo zgodny z pattern
    # tekst = ''.join([chr(randint(97, 122)) for _ in range(N)]) #tekst szybko niezgodny z kazdą pattern
    pattern = 'a' * M + 'z'

    st = ts()
    # przeszukujemy
    # i = tekst.find(pattern) # używa algorytmu BMH https://stackoverflow.com/questions/681649/how-is-string-find-implemented-in-cpython
    i = mfind(tekst, pattern)
    en = ts()
    return st, en


patt_i = 6
for txt_i in range(patt_i, 20):
    st, en = run((2 ** txt_i), (2 ** patt_i))
    print(txt_i, patt_i, f'{(en - st) * 1000:.3f}ms')
    # tu mamy dane typu (x,y,z), gdzie x == txt_i, y=patt_i, z=czas wykonania... potrzeba density plot

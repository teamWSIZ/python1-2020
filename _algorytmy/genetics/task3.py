from _algorytmy.genetics.task2 import random_dna
from _algorytmy.genetics.utils import ts


def complement(a: str):
    nowy = ''
    for l in range(len(a)):
        if a[l] == 'T':
            nowy += 'A'
        elif a[l] == 'C':
            nowy += 'G'
        elif a[l] == 'A':
            nowy += 'T'
        else:
            nowy += 'C'
    return nowy


def complement_(a: str):
    a = a.replace('T', '*')
    a = a.replace('A', 'T')
    a = a.replace('*', 'A')

    a = a.replace('C', '*')
    a = a.replace('G', 'C')
    a = a.replace('*', 'G')
    return a


g = random_dna(10 ** 7)

start = ts()
g_ = complement(g)
end = ts()
print(f'complement {len(g)} trwał {end - start:.3f}s')

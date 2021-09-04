from datetime import datetime
from random import randint

def ts():
    return datetime.now().timestamp()


# def random_dna(length: int) -> str:
#     l = ["T", "C", "A", "G"]
#     dna = ""
#     for _ in range(length):
#         dna += l[randint(0, 3)]
#     return dna

def random_dna(length: int) -> str:
    l = ["T", "C", "A", "G"]
    w = []
    for _ in range(length):
        w.append(l[randint(0, 3)])
    return ''.join(w)

if __name__ == '__main__':
    start = ts()
    g = random_dna(10 ** 6)
    end = ts()
    print(f'genrowanie {len(g)} trwało {end - start:.3f}s')

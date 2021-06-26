from random import seed, randint

N = 10 ** 4
A = 1_000
B = 1_000_100

seed(111)
monety = [randint(0, N) for _ in range(N)]


def is_acceptable(sum: int):
    return A <= sum <= B


ways = [-1] * (B + 1)
ways[0] = 0

for (i, m) in enumerate(monety):
    for at in range(B, -1, -1):
        if at - m < 0:
            break
        if ways[at - m] >= 0:
            ways[at] = max(ways[at], ways[at - m] + 1)
    if i % 10 == 0:
        print(i)

print(max(ways[A:B]))

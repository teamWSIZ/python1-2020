from random import randint

from algorytmy.utils import ts, delta

h = set([5, 8, 10, 34, 8, 5])

# szukanie liczby 8 w `h` jest O(1)...

N = 10000000
M = 10000
for i in range(N):
    h.add(randint(0, 10 ** 9))

# sprawdzam przeszukiwanie
st = ts()
x = 0
for i in range(M):
    if h.__contains__(8):
        x += 1
en = ts()
delta(st, en)


# Jeśli mamy zbiór M liczb (z napisu `a`, podnapisy długości sublen), ... i N liczb z napisu `b` (podnapisy długości sublen)
# to przeszukanie czy któraś z tych M liczb powtarza się gdzieś w tych N z napisu `b` zajmie O(M)
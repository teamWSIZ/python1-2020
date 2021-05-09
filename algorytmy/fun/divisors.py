from collections import defaultdict
from datetime import datetime


def ts():
    return datetime.now().timestamp()


rrr = 7
m = 10 ** 7
a = 17
b = 31


def next_random():
    global rrr
    rrr = (rrr * a + b) % m
    return rrr


CNT = 10 ** 7

w = [next_random() for _ in range(CNT)]

# Q 1020 ... 20000
# naiwne
# print(w[1020:20001].count(150))
# print(w[1020:20001].count(150))
# print(w[1020:20001].count(150))
# print(w[1020:20001].count(150))
# print(w[1020:20001].count(150))
# print(w[1020:20001].count(150))
# print(w[1020:20001].count(150))
# print(w[1020:20001].count(150))

print(w[:10])

# hint.. stworzyć tablicę `s`, z interpretacją s[x].. ile razy `150` występuje na lewo od `x`, czyli
# na indeksach `0, 1, 2, ..., x-1`

# Zadanie: mamy `w`, obliczyć `s`


# pytanie: jak to zrobić, jeśli interesują nas nie tylko argument 150, ale też... 0... do 10**6
# pomysł: dla każdej z interesujących nas liczb, zebrać sobie pozycje na których ona występuje...


ww = [0, 50, 80, 300, 412]

# zadanie: dla każdej z występujących w "w" liczb, zebrać pozycje na których one występują......

pozycje = defaultdict(lambda: [])
for i, x in enumerate(w):
    pozycje[x].append(i)  # pozycje na których występuje "x"

for x in range(250):
    print(x, pozycje[x])

# Zadanie X: mając dane pozycje na któch występuje liczba X (np jak powyżej w "ww") napisać funkcję, która
# poda ile razy X występuje między pozycjami L i R (niekoniecznie obecnymi w "ww").
# (wykorzystać "bisect_left" i podobne)

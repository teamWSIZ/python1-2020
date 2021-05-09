from random import randint

m = 10
cnt = 10

w = [(min(a, b), max(a, b)) for _ in range(cnt) for (a, b) in [(randint(0, m - 1), randint(0, m - 1))]]
print(w)

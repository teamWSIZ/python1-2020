def podzial(w, h):
    r = 0
    while w % 2 == 0:
        r += 1
        w /= 2
    while h % 2 == 0:
        r += 1
        h /= 2
    return 2 ** r


t = int(input())

for i in range(t):
    w, h, n = [int(s) for s in input().split()]
    possible = podzial(w, h)
    if possible >= n:
        print('YES')
    else:
        print('NO')
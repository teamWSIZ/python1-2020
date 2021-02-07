from math import sqrt

y = 240

divisors = []

for i in range(2, int(sqrt(y))):
    if y % i == 0:
        divisors.append(i)
        divisors.append(y // i)

divisors.sort()

res = {}
print(type(res))
for d in divisors:
    count = 0
    z = y
    while z % d == 0:
        count += 1
        z //= d
    res[d] = count

print(res)
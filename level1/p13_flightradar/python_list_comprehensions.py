from math import sqrt

a = [1, 2, 3]
b = [5, 5, 1]

c = [aa - bb for (aa, bb) in zip(a, b)]

for k in zip(a, b):
    print(k)

true_distance = sqrt(sum([(x - y) ** 2 for (x, y) in zip(a, b)]))




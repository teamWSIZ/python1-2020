d = dict()

d[1] = 12
d[8] = 2
d[7] = 10
d[0] = 1

print(d)
print(d.items())
w = list(d.items())
print(w)
w.sort(key=lambda x: x[1])
print(w)
print(w[-1])

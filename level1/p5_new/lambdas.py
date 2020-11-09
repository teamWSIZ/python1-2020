def add(a, b):
    return a + b


def diff(a, b):
    return a - b


def act_on(a, b, fff):
    return fff(a, b)


def second(a):
    return a[1]


print(act_on(5, 2, diff))
print(act_on(5, 3, add))
print(act_on(5, 3, lambda a, b: (a * b)))

w = [(1, 2), (2, 1)]
print(sorted(w, key=second))

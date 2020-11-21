from random import randint, seed

# seed(111)
for i in range(100):
    x = randint(1, 30)
    # print(x)


# idea testów: wygenerować 2 listy długości 9,
# a potem do tej która ma mniejszą sumę dodać taką monetę, by sumy były równe


def generate_equal_sum_lists():
    a = []
    b = []
    for _ in range(3):
        a.append(randint(1, 5))
        b.append(randint(1, 5))

    diff = sum(a) - sum(b)
    if diff > 0:
        b.append(diff)
    else:
        a.append(-diff)
    return a, b


a, b = generate_equal_sum_lists()
a.extend(b)
print(a)

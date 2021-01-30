import itertools

# powiedzmy, że mamy 6 monet

for a in itertools.product(range(2), repeat=6):
    print(a)

# ↑↑ generuje wszystkie możliwe listy składające się z elementów 0 i 1 o długości 6,


# for a in itertools.product(range(4), repeat=6):
#     print(a)
# ↑↑ generuje wszystkie możliwe listy składające się z elementów 0 i 1, 2, 3 o długości 6,


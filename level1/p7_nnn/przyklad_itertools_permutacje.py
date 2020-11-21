import itertools

w = list(itertools.permutations([1, 2, 3]))  # wszystkie 'permutacje', tj. możliwe kolejności elementów tej listy

for p in w:
    print(p)
"""
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
"""

print(list(itertools.permutations('kadabra')))  # uwaga -- tego jest len('kadabra')! (silnia), czyli tu: 5040
# już dla 'abra kadabra' (len=12) byłoby 479001600 permutacji........

from math import factorial
print(factorial(12))

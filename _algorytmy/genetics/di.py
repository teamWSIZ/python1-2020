# Słownik
from random import random

d = {}
d['abc'] = 12
d['aaa'] = 5
d['ccc'] = 'possible'

print(d)  # {'abc': 12, 'aaa': 5, 'ccc': 'possible'}
print(len(d))  # 3

print('abc' in d)  # True
d['abc'] += 1  # dziala

d[888] = 12     # też działa -- kluczami mogą być też liczby całkowite

for (k, v) in d.items():    #pętla po elementach dictionary
    print(k, v)

"""
abc 13
aaa 5
ccc possible
888 12
"""

from random import random
print(random())

s = 'abc'
s = s.replace('a','')
print(s)
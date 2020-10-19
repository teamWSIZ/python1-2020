from datetime import datetime
from random import randint
from time import sleep

b = datetime.now().timestamp()
sleep(0.2)
e = datetime.now().timestamp()
print(f'{e - b}')  # 0.2009

s = set()
s.add(12)
s.add(12)
s.add(13)
print(s.__len__())  # 2
print(s.__contains__(12))  # True
w = set()
w.add(10)
w.add(13)
g = w.intersection(s)
print(g)  # {13}

for i in range(10):
    print(randint(1, 10))

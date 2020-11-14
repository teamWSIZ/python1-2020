w = [1, 3, 2, 1, 1]
from random import randint, seed
seed(111)
w = [randint(0,20) for i in range(21)]
print(w)


pozycja = 0

for i in range(20):
    print(f'lis Ciel na pozycji {pozycja}')
    print(f'lis Ciel przechodzi do {w[pozycja]}')
    print('--------')
    pozycja = w[pozycja]

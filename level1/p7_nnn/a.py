import itertools

coins = [1, 2, 3, 4]

su = sum(coins)
# for i in range(len(coins)):
for a in itertools.product(range(len(coins)), repeat=3):
    print(a)


    #         if sum(coins[n] for n in a) == su / 2:
    #             return True
    # return False

from random import randint

total = 0
won = 0

for rep in range(100000):
    our = randint(0, 2)
    gold = randint(0, 2)
    he = randint(0, 2)
    if he == our or he == gold:
        continue
    total += 1
    if our == gold:
        won += 1

print(won / total)
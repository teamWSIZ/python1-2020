from random import randint, choice

total = 0
won = 0

for rep in range(100000):
    our = randint(0, 2)
    gold = randint(0, 2)

    possible = set([0,1,2])
    possible.remove(our)
    if gold in possible:
        possible.remove(gold)

    he = choice(list(possible))
    total += 1
    if our == gold:
        won += 1

print(won / total)
"""
Przykład do simulated annealing.

Mamy duży zbiór "monet". Wybieramy podzbiory ... i chcemy by suma monet w podzbiorze była między [A,B]...
i jednocześnie chcemy jak najwięcej monet użyć w rozwiązaniu.


SA:
- zbiór dotychczasowych "rozwiązań"... (może posortowany...)   "grupa agentów"
- algorytm:
   (A) albo tworzymy kompletnie nowe rozwiązanie i sprawdzamy czy jest lepsze... (ma sens na początku)
   (B) albo bierzemy jedno z rozwiązań i sprawdzamy "małe modyfikacje" wokół tego rozwiązania...

"""
from dataclasses import dataclass
from random import seed, randint
from typing import List

N = 10 ** 4
A = 1_000
B = 1_000_100

seed(111)
monety = [randint(0, N) for _ in range(N)]


def my_shuffle(ww, k=100):
    for i in range(k):
        # zamienimy ze sobą dwa elementy ww
        a = randint(0, len(ww) - 1)
        b = randint(0, len(ww) - 1)
        t = ww[a]
        ww[a] = ww[b]
        ww[b] = t


# potrzeba podzbiorów z "monety" ...
# potrzeba mieć możliwość "dorzucenia/wyrzucenia" elementów

@dataclass
class Agent:
    """
    "Jakieś" aktualne rozwiązanie
    """
    taken: List[int]
    rejected: List[int]
    sum: int
    score: int  # ile elementów wzięliśmy, czyli len(taken)


# będziemy trzymali/pamiętali grupę 100 agentów...
# a = Agent([1, 2, 3], [2, 2, 2], 6, 3)
# print(a)

def is_acceptable(a: Agent):
    return A <= a.sum <= B


def random_attempt(epsilon=0.01):
    """
    complexity: O(N); w praktyce
    """
    my_shuffle(monety)
    at = 0
    sum = 0
    taken = []
    while sum <= B and at < len(monety):
        sum += monety[at]
        taken.append(monety[at])
        at += 1
        x = randint(0, 1000) / 1000
        if x < epsilon and sum >= A:
            break
    # ↓↓ tutaj monety[at:] robi kopię tablicy monety... i jest O(N) (główne obciążenie complexity)
    return Agent(taken, monety[at:], sum, len(taken))


def modify_attempt(a: Agent):
    # dodajemy losową monetę do agenta

    my_shuffle(a.rejected, k=10)
    new_taken = a.taken.copy()
    a.rejected.sort(reverse=True)
    new_taken.append(a.rejected[-1])
    new_sum = a.sum + a.rejected[-1]
    new_rejected = a.rejected[:-1].copy()  # O(N)...   -- obciąża complexity..

    return Agent(new_taken, new_rejected, new_sum, a.score + 1)


def enlarge_agent(a: Agent):
    # dodajemy losową monetę do agenta `source` (modyfikowany)
    old_score = a.score

    my_shuffle(a.rejected, k=10)  # ostatni element z .rejected zostanie dodany
    element = a.rejected[-1]
    a.taken.append(element)
    a.sum += element
    a.rejected = a.rejected[:-1]
    a.score += 1
    if not is_acceptable(a):
        # rollback
        a.score -= 1
        a.sum -= element
        a.rejected.append(element)
        a.taken = a.taken[:-1]


def modify_agent(a: Agent):
    # wymieniamy jedną z wziętych liczb z jedną rejected; akceptujemy zmianę jeśli jest OK
    old_score = a.score

    # randomizacja
    i = randint(0, len(a.taken) - 1)
    t = a.taken[i]
    a.taken[i] = a.taken[-1]
    a.taken[-1] = t
    i = randint(0, len(a.rejected) - 1)
    t = a.rejected[i]
    a.rejected[i] = a.rejected[-1]
    a.rejected[-1] = t

    e1 = a.rejected[-1]
    e2 = a.taken[-1]
    a.sum += e1 - e2
    a.taken = a.taken[:-1]
    a.rejected = a.rejected[:-1]
    a.taken.append(e1)
    a.rejected.append(e2)

    if not is_acceptable(a):
        # rollback
        a.sum -= e1 - e2
        a.taken = a.taken[:-1]
        a.rejected = a.rejected[:-1]
        a.taken.append(e2)
        a.rejected.append(e1)


agents: List[Agent] = []

# od tego miejsca -- "magia" różnych pomysłów na zarządzanie agentami...

nops = 0

while len(agents) < 300:
    a = random_attempt()
    nops += 1
    if is_acceptable(a):
        agents.append(a)

for j in range(50000):
    for i in range(10):
        a = random_attempt()
        nops += 1
        if is_acceptable(a):
            agents.append(a)

    agents.sort(key=lambda a: a.score, reverse=True)

    to_modify = agents[-10:]
    for x in to_modify:
        a = modify_attempt(x)
        if is_acceptable(a):
            agents.append(a)

    agents = agents[:30]
    agents.sort(key=lambda a: a.score, reverse=True)

    # selected = agents[:10]
    # for a in selected:
    #     nops += 1
    #     enlarge_agent(a)
    # selected = agents[10:20]
    # for a in selected:
    #     nops += 1
    #     modify_agent(a)

    # agents.sort(key=lambda a: a.score, reverse=True)

    if j % 200 == 0:
        print(f'best:{agents[0].score}')

agents.sort(key=lambda a: a.score, reverse=True)

print([a.score for a in agents][:10])
print(f'nops={nops}')

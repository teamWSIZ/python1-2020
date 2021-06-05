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


def modify_attempt(source: Agent):
    # dodajemy losową monetę do agenta

    my_shuffle(source.rejected, k=10)
    new_taken = source.taken.copy()
    new_taken.append(source.rejected[-1])
    new_sum = source.sum + source.rejected[-1]
    new_rejected = source.rejected[:-1].copy()  # O(N)...   -- obciąża complexity..

    return Agent(new_taken, new_rejected, new_sum, source.score + 1)


agents: List[Agent] = []

# od tego miejsca -- "magia" różnych pomysłów na zarządzanie agentami...

for j in range(5000):
    for i in range(100):
        a = random_attempt()
        if is_acceptable(a):
            agents.append(a)

    agents.sort(key=lambda a: a.score, reverse=True)
    agents = agents[:100]

    selected = agents[:10]
    for a in selected:
        na = modify_attempt(a)
        if is_acceptable(na):
            agents.append(na)

agents.sort(key=lambda a: a.score, reverse=True)

print([a.score for a in agents][:10])

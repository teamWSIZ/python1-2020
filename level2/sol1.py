"""
-- wygenerować 10**5 liczb losowych z przedziału [1..10**4];
-- sprawdzić ile zajęło czasu samo generowanie liczb,
   a ile zbieranie ich w strukturze typu listy, albo typu set
- wyliczyć ile jest elementów unikalnych w tym ↑↑
sprawdzić ile trwa takie samo generowanie dla 10**6 elementów
"""
from datetime import datetime
from random import randint

mx = 10 ** 4


def ts():
    return datetime.now().timestamp()


b = ts()
s = set()
for i in range(10 ** 7):
    x = randint(1, 10 ** 4)
    s.add(x)
e = ts()

print(f'czas wykonania to {1000 * (e - b):.1f}ms')
# zwykły python 3.8
# generowanie:
# 92ms → 910ms (dla 1mln)
# ze zbieraniem:
# 102ms → 1025ms (dla 1mln)
# ↑↑↑ skaluje się OK -- liniowo z rozmiarem danych

# pypy PyPy 7.3.0 (python 3.6.9)
# generowanie:
# 30ms → 157ms (dla 1mln)
# ze zbieraniem:
# 32ms → 170ms (dla 1mln) → 1540ms (dla 10mln)
# ↑↑↑ skaluje się mniej niż liniowo -- pypy ma jakiś startup delay; potem powinno iść liniowo

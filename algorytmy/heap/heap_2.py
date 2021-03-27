from heapq import heapify, heappush
from statistics import median_low

from algorytmy.utils import print_heap

h = [(5, 'a'), (7, 'c'), (1, 'z'), (1, 'a')]

heapify(h)

heappush(h, (-1, 'zzzz'))
heappush(h, (-1, 'zz'))

print_heap(h)


"""
Problem: mamy wartości liczbowe zbierane co 1 sek.... za ostatnie 3 lata.... ==> lista "a" (100mln liczb)
Chcemy znaleźć dla każdej pozycji minimalną wartość w "a" między aktualną pozycją, a pozycją wcześniej o 3600 elementów
(1 godzina).

"sliding window" .... 

[ 2, 3, 6, 8, 2, 5, 4, 2, 1, 4, 6, 2, 3, 7, 9]
jeśli zasięg = 4 ↓↓

[2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, ....] 

- wykorzystać heap wielkości 3600 elementów, i dodawać jeden przy przesunięciu w prawo, oraz usuwać jeden (ten który
  wypada z okna)
- ??? można spróbować wykorzystać "set"
"""



"""
Zadanie: 
Wylosować początkowo 10**6 liczb; potem w pojedynczym kroku: 
  - dolosować kolejne 1000 liczb
  - usunąć 1000 najmniejszych liczb ze zbioru

Na koniec znaleźć najmniejszy element zbioru oraz: 
  - średnią z elementów zbioru
  - medianę elementów zbioru
  
Wykorzystać strukturę heap. 
"""


print(median_low([1,1,1,2,3,4,4,3,2,12,1]))
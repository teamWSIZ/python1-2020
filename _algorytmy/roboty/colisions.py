"""
Zadanie: mamy posortowane tablice:
left = [...]    (idą w lewo)
rigt = [...]    (idą w prawo)

... dla każdego elementu z "left" znaleźć po jakim czasie (jeśli wogóle) zderzy się z jakimś elementem z rigt
"""

# w = [1, 4, 8, 10, 50]
# x = 10
# i = bisect_left(w, x) # 3
from bisect import bisect_left, bisect_right

left = [16, 22, 100]
rigt = [0, 4, 8, 20]

# by posortować po czasie... ... może użyć heap((r-l, r, l))

for e in left:
    i = bisect_right(rigt, e)
    print(f'{e} zderza się z elementem na pozycji {rigt[i-1]}')

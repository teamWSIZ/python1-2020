from collections import deque
from datetime import datetime


def ts():
    return datetime.now().timestamp()


def test_for(n):
    w = [i for i in range(n)]
    q = deque(w)

    st = ts()

    # usuwanie z przodu listy
    # for i in range(n):
    #     del w[0]

    #usuwanie z tyłu listy
    # for i in range(n):
    #     del w[w.__len__()-1]

    # usuwanie z deque
    for i in range(n):
        # w.pop()
        q.popleft()

    en = ts()
    print(f'czas wykonania: {(en - st) * 1000:.3f}ms')


test_for(1 * 10 ** 4)
test_for(1 * 10 ** 5)
test_for(2 * 10 ** 5)
test_for(4 * 10 ** 5)

# usuwanie z przodu dla listy i deque
# czas wykonania: 9.275ms      (10**4)      deque:0.831ms
# czas wykonania: 1905.136ms  (1*10**5)     deque:5.823ms
# czas wykonania: 8464.871ms  (2*10**5)     deque:11.721ms
# czas wykonania: 35042.341ms (4*10**5)     deque:23.747ms
# ↑↑ rośnie kwadratowo z rozmiarem
# dla pypy/deque:
# czas wykonania: 1.723ms
# czas wykonania: 0.966ms
# czas wykonania: 0.844ms
# czas wykonania: 1.870ms
#############
# usuwanie z tyłu:
# czas wykonania: 1.825ms  (10**4)      deque:0.590ms
# czas wykonania: 19.708ms (1*10**5)    deque:6.115ms
# czas wykonania: 36.044ms (2*10**5)    deque:11.978ms
# czas wykonania: 71.945ms (4*10**5)    deque:24.389ms
# ↑↑ rośnie liniowo z rozmiarem
# czasy dla pypy/deque:
# czas wykonania: 1.773ms
# czas wykonania: 0.978ms
# czas wykonania: 6.462ms
# czas wykonania: 2.239ms



# Deque ... w python ???

from datetime import datetime


def ts():
    return datetime.now().timestamp()


n = 4 * 10 ** 5
w = [i for i in range(n)]
# print(w)

st = ts()

#usuwanie z przodu
# for i in range(n):
#     del w[0]

#usuwanie z tyłu
for i in range(n):
    del w[len(w)-1]

en = ts()
print(f'czas wykonania: {(en-st)*1000:.3f}ms')
# czas wykonania: 9.275ms      (10**4)
# czas wykonania: 1905.136ms  (1*10**5)
# czas wykonania: 8464.871ms  (2*10**5)
# czas wykonania: 35042.341ms (4*10**5)
# ↑↑ rośnie kwadratowo z rozmiarem
#############
# usuwanie z tyłu:
# czas wykonania: 1.825ms  (10**4)
# czas wykonania: 19.708ms (1*10**5)
# czas wykonania: 36.044ms (2*10**5)
# czas wykonania: 71.945ms (4*10**5)
# ↑↑ rośnie liniowo z rozmiarem

# Deque ... w python ???
from heapq import heappush, heappop, heapify

h = [(0,'a'), (10,'a')]
heapify(h)


heappush(h, (1, 'a'))
heappush(h, (2, 'bur'))
heappush(h, (1, 'zor'))
heappush(h, (-1, 'zzz'))
heappush(h, (-1, 'zzzz'))


while len(h)>0:
    print(heappop(h))
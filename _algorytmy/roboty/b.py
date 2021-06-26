from heapq import heappush, heappop

w = ['a', 'b']
print(''.join(w))


h = []
heappush(h, 12)
heappush(h, 11)
heappush(h, 18)
while len(h):
    print(heappop(h))
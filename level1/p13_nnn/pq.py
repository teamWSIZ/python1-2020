import heapq
# https://dbader.org/blog/priority-queues-in-python

q = []

heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))
heapq.heappush(q, (2, 'code'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)
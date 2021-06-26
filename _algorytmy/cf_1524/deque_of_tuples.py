from collections import deque

g = deque()
g.append((1, 2))
g.append((3, 2))
while len(g) > 0:
    x = g.popleft()
    print(x)

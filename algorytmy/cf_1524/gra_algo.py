from collections import deque


def simple_bfs_pass(n, ch, w, start):
    # zwraca długości ścieżek do "dolnych" nodów grafu...
    # "dolny" node, to taki który nie ma "dzieci"
    q = deque()  # w deque trzymamy parę (node, koszt_osiągnięcia_go)
    q.append((0, 0))
    min_cost = [10 ** 9] * n
    bottom_nodes = set()
    while len(q):
        at, cost = q.popleft()
        print(f'procesuję {(at,cost)}')
        if cost < min_cost[at]:
            print('lepsze rozwiązanie od dotychczasowego!')
            min_cost[at] = cost
            if len(ch[at]) == 0:
                bottom_nodes.add(at)
            else:
                for c in ch[at]:
                    q.append((c, cost + w[at]))

    for b in bottom_nodes:
        print(f'({b})→{min_cost[b] + w[b]} | ', end='')
    print()


if __name__ == '__main__':
    n = 16
    ch = [[1, 2], [3, 4], [4, 5], [6], [7, 8], [8, 9], [10, 11], [12], [13], [14, 15], [], [], [13], [], [], []]
    w = [0, 10, 10, 30, 20, 10, 10, 30, 20, 10, 10, 10, 20, 10, 10, 10]
    w[8] = 100
    simple_bfs_pass(n, ch, w, 0)

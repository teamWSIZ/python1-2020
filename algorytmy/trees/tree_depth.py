from algorytmy.trees.inputz import read_test_case


def dfs(origin, current, chs, depth):
    print(f'analizuję {current}, głębokość {depth}')
    for c in chs[current]:
        if c == origin: continue
        dfs(current, c, chs, depth + 1)


if __name__ == '__main__':
    n, chs = read_test_case('t1.txt')
    dfs(-1, 0, chs, 0)

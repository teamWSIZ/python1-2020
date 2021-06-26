def print_robots(x, t):
    b = ['.'] * 30
    for (xx, tt) in zip(x, t):
        b[xx] = '→' if tt == 'R' else '←'
    print(''.join(b))


def simulate(x, t, n_turns=10):
    # []  ... [0]==even, [1]==odd....
    # [] ... [0]==R, [1]==L
    robots = [[set() for dir in range(2)] for parity in range(0, 2)]  # robots[0][.] ... roboty o parzystości even
    # drugi indeks to 0 jeśli są R i 1 jeśli są 'L'
    # print(robots)
    for xx, tt in zip(x, t):
        robots[xx % 2]['RL'.index(tt)].add(xx)
    # print(robots)
    for time in range(n_turns):
        for p in range(2):
            for dir in range(2):
                ss = set()
                for e in robots[p][dir]:
                    ss.add(e + 1 - 2 * dir)
                robots[p][dir] = ss
            to_delete = set()
            for e in robots[p][0]:
                if e in robots[p][1]:
                    to_delete.add(e)
            robots[p][0] -= to_delete
            robots[p][1] -= to_delete


        print(robots)

# for _ in range(n_turns):


if __name__ == '__main__':
    x = [5, 10, 15, 13]
    t = 'RLRL'
    # print_robots(x, t)
    simulate(x, t)

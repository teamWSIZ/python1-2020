def sort_data(x, t):
    x = [15, 10, 5]
    t = 'RLR'

    w = sorted([(xx, tt) for xx, tt in zip(x, t)])
    x, t = [], []
    for xx, tt in w:
        x.append(xx)
        t.append(tt)
    return x, t

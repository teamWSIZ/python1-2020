g = [
    '.....',
    '.#...',
    '.###.',
    '...#.',
    '..##.',
    '.#...',
    '...#.',
]


def go(pos) -> bool:
    if pos == (5,5):
        return True # koniec labiryntu

    nposs = [(), (), (), ()]  # nowe dozwolone pozycje -- idziemy w ←↑→↓, sprawdzając brzegi i skały
    for np in nposs:
        if go(np) == True:
            return True
    return False
    # todo: zablokować wchodzenie w pozycje w których już byliśmy...


# rozwiązanie
go([0, 0])

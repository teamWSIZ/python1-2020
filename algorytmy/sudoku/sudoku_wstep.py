from typing import List


def check_quartet(q: List[int]):
    """
    :param q: Cztery liczby całkowite [0..4]
    :return: Liczby które się nie pojawiają w "q" (poza 0), lub None jeśli króraś liczba pojawia się >1 razy
    """
    cnt = [0] * 5  # ile razy występują...
    for i in q:
        cnt[i] += 1
    cnt[0] = -1
    if max(cnt) > 1:
        return None
    return [idx for idx in range(1, 5) if cnt[idx] == 0]


def print_board(b):
    ll = []
    for l in b:
        ll.append(f'{l[0]} {l[1]} | {l[2]} {l[3]} ')
    ll = ll[:2] + ['---------'] + ll[2:]
    for l in ll:
        print(l)

def check_board(board):
    """
    :return: False, jeśli pozycja jest nielegalna
    """
    # sprawdzamy rzędy
    for r in board:
        a = check_quartet(r)
        if a is None:
            return False

    # sprawdzamy kolumny
    for c in range(4):
        q = [board[r][c] for r in range(4)]
        a = check_quartet(q)
        if a is None:
            return False

    # sprawdzamy kwadraty
    # tu zrobić jakoś pętlę po sim_annealing skaczącą co 2 ... i wewnątrz zebrać kwadrat o lewym górnym rogu w (sim_annealing,sim_annealing)
    return True


board = [[0, 0, 0, 1], [1, 0, 2, 3], [0, 1, 2, 4], [0, 0, 0, 0]]
print_board(board)

# print([1,2,3] + [2,3,4])

print(check_quartet([0, 0, 3, 4]))
print(check_board(board))
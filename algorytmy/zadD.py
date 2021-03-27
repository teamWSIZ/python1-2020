# 24 -> 12 12 -> 12 6 6 -> 12 6 3 3 -> 6 6 6 3 3 itd
from heapq import heappush, heappop
from typing import List


# [10, 10, 8, 2, 2, 1]

def allocate(space: List[int], file_size: int):
    space.sort(reverse=True)
    h = []
    heappush(h, -file_size)
    at = 0
    while len(h) > 0 and at < len(space):
        print(h)
        piece = - heappop(h)
        print(f'umieszczam kawałek {piece}')

        if at == len(space) - 1 and piece>space[at]:
            print('nie można umieścić pliku na dysku')
            heappush(h, -piece)
            break

        if piece > space[at]:
            # piece nie mieści się na aktualnej pozycji --> rozbić
            if piece % 2 == 0:
                heappush(h, -piece // 2)
                heappush(h, -piece // 2)
            else:
                heappush(h, -(piece // 2))
                heappush(h, -(piece // 2) - 1)
        else:
            # piece mieści się na aktualnej pozycji --> umieścić, i iść dalej
            print(f'umieszczam na pozycji {at} kawałek {piece}')
            at += 1
    if len(h) > 0:
        print('nie udało się zapisać pliku')
    else:
        print(f'zapisano na pozycjach [0..{at - 1}]')


allocate([8, 4, 2, 1, 1, 1, 1], 15)

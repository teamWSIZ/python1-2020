from random import randint

data = [[2, 2, 4, 5, 8], [4, 5, 5, 10], [1, 1, 1, 4, 10], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ,[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

# problem: usunąć jak najmniejszą liczbę monet z "data", tak, aby zachodziło:
mi = min([sum(a) for a in data])
mx = max([sum(a) for a in data])

print(mi / mx >= 0.9)


def masked_sum(arr, mask):
    s = 0
    for i in range(len(arr)):
        if mask & 1:
            s += arr[i]
        mask >>= 1
    return s


best_mi = 0  # ile monet zostało
best_masks = []

while True:
    mi_ = randint(1, mi)  # próbujemy ustawić sumę między [mi_, 10/9 * mi_]
    masks_ = []
    for arr in data:
        n = len(arr)
        # ... liczba binarna... 1 oznacza, że wliczamy do sumy... ma mieć tyle bitów co n
        mask = randint(0, (1 << n) - 1)  # np. dla n=2 --> 0='00', 1='01', 2='10', 3='11'
        s = masked_sum(arr, mask)
        if mi_ <= s <= (10 * mi_ // 9):
            masks_.append(mask)
        else:
            break
    if len(masks_) < len(data):
        continue

    remained = 0
    for m in masks_:
        remained += bin(m).count('1')
    if remained > best_mi:
        best_mi = remained
        best_masks = masks_
        print(f'{best_mi} → {[bin(m) for m in masks_]}')
        print(f'{[masked_sum(ar, m) for (ar, m) in zip(data, best_masks)]}')

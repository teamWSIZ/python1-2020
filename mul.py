from random import randint

w = randint(1, 100)
print(w)

# ii = input('>')  # to wczytuje napis (tzw. string, str)
# iii = int(ii)  # próba zamiany napisu na liczbę całkowitą...
# print(ii == 11)

correct = 0
total = 0

# powtórz 10 razy
for i in range(10):
    a = randint(1, 16)
    b = randint(1, 16)
    w = input(f'podaj wynik mnożenia {a} * {b} > ')
    wynik = int(w)  # zamieniamy na liczbę
    if wynik == a * b:
        print('OK')
        correct += 1
    else:
        print('Źle')
    total += 1
    print(f'Wynik dotychczasowy: {correct} / {total} = {correct / total * 100 :.2f} %')

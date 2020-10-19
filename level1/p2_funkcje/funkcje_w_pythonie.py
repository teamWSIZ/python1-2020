# zadanie: mając daną listę liczb zumować kwadraty

def sum_sqares_test(lista, napis, wykladnik):
    print(f'lista:{lista}')
    print(f'napis:{napis}')


def suma_liczb(a, b):
    print(f'a={a} b={b}')
    return a + b


sum_sqares_test(1, 2, 3)
sum_sqares_test(['a', 'b', 'c'], 2, 3)
sum_sqares_test(555, 2, 3)
sum_sqares_test(999, 2, 3)

wynik = suma_liczb(2, 999)
print(wynik)

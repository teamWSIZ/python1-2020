"""
Program ilustrujący definicje funkcji
"""


# Funkcja liczy sumę elementów podniesionych do potęgi `wykladnik`
def sum_squares(lista, wykladnik):
    wynik = 0
    for i in lista:
        wynik += i ** wykladnik
    return wynik


# Funkcja sprawdza czy wykonanie `sum_squares` na `lista` daje `dobry_wynik`.
def testuj(lista, dobry_wynik):
    wynik = sum_squares(lista, 2)
    if wynik == dobry_wynik:
        print(f'dla {lista} wynik OK')
    else:
        print(f'dla {lista} błąd! jest:{wynik}, ma być:{dobry_wynik}')


w = [1, 2, 3]

# print(sum_squares(w, 2))
# print(sum_squares(w, 3))
# print(sum_squares(w, 1))

testuj([1, 2, 3], 14)
testuj([1], 1)
testuj([1, 1], 2)

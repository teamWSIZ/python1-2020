from random import randint

w = [1, 1, 4, 3, 2, 3, 4, 5, 6, 7]
print(w.__contains__(6))

m = {}  # słownik / dictionary / mapa .... {key → value}

m['Kowalski'] = 10
m['Xiaoping'] = 5
m['Wu'] = 17
m['Wu'] = 18  # nadpisze poprzednią wartość...

print(m.__contains__('Wux'))  # sprawdzenie czy element o kluczu `Wux` jest w mapie
print(m)

# przejście pętlą przez mapę/dict
for k in m.keys():
    print(f'dla klucza:{k} wartość wynosi:{m[k]}')

print(m.get('xxx')) # to przejdzie nawet jak klucza `xxx` nie ma w mapie -- wyprodukuje None
# print(m['xxx']) # to _nie_ przejdzie jeśli klucza `xxx` nie ma w mapie -- wyprodukuje błąd


w[0] = 15
w[0] = 20  # ta wartość nadpisuje dotychczasową...

print(m.__len__())  # liczba elementów w dict/słowniku/mapie....
print('--------')

# zadanie - wylosować 100 liczb z przedziału 1..100, i sprawdzić ile z tych liczb było unikalnych...
liczby = {}
for i in range(100):
    x = randint(1, 100)
    liczby[x] = 1
print(liczby.__len__())



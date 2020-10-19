"""
Program pokazuje jak adresować elementy list,
jak wybierać podlisty, oraz jak przechodzić przez wszystkie elementy list
dwoma typami pętli.
"""

w = [1, 0, 8, 2, 5]

print(w)
print(w[0])  # pierwszy elemenet listy
print(w[1])
print(w[-1])  # ostatni element listy

bb = w[1:]  # podlista `w` od elementu 1 do końca
print(bb)

cc = w[1:4]  # podlista `w` od elementu nr 1 do elementu 3 włącznie (bez 4)
print(cc)

dd = w[0:-1]  # cała lista poza ostatim elementem
print(dd)

print(f'-----')

# przejście po elementach kolekcji (listy) bezpośrednio
for element in w:
    print(f'element:{element}, kwadrat: {element ** 2}')
    print(f'-----')

# przejście po elementach listy po indeksach
for i in range(len(w)):
    print(f'element nr {i} to {w[i]}')

w = [1, 0, 8, 2, 5]

print(w)
print(w[0])  # pierwszy elemenet listy
print(w[1])
print(w[-1])  # ostatni element listy
w[0] = 111
print(w[0])
w.append(333)
w.append(777)
print(w)
print(len(w))  # ile elementów w liście

for g in w:
    print(f'elemenet listy: {g}')

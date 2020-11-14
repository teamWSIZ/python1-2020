w = [['kowalski', 2], ['nowak', 1], ['nowak', 0], ['zzak', 30]]

s1 = sorted(w)  # posortowane alfabetycznie
print(s1)


def punkty(lista):
    return lista[1]


s2 = sorted(w, key=punkty)
print(s2)

s3 = sorted(w, key=lambda a: a[1], reverse=True)
print(s3)

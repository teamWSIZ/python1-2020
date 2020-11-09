w = [
    '1. NOWAK 90488',
    '2. KOWALSKA 63003',
    '3. WIŚNIEWSKA 49968',
    '4. WÓJCIK 45041',
    '5. KOWALCZYK 44756',
    '6. KAMIŃSKA 43032',
    '7. LEWANDOWSKA 42678',
    '8. ZIELIŃSKA 41143',
    '9. SZYMAŃSKA 40438',
    '10. WOŹNIAK 40269'
]
d = {}
for e in w:
    r = e.split(' ')
    d[r[1]] = int(r[2])


# print(d)

def surname_count_by_prefix(prefix: str):
    sum = 0
    for k in d.keys():
        if k.startswith(prefix):
            sum += d[k]  # wardość w dict odpowiadająca kluczowi k, który się zaczyna na `prefix`
    return sum


print(surname_count_by_prefix('K'))  # 150791

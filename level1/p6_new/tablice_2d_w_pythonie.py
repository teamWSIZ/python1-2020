w = [[1, 2], [3, 4]]
print(w)
print(w[0])  # 0-rząd
print(w[1])  # 1-rząd

t = [[0], [1, 2, 3, 4], 'abra kadabra']
print(t)

print('---------')
mmm = [i * i for i in range(1, 10)]  # sposób na inicjalizację tablicy
print(mmm)

m2m = [[i * j for j in range(1, 11)] for i in range(1, 11)] # sposób inicjalizacji tablicy 2d
for row in m2m:
    print(row)

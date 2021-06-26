a = 37

print(bin(a))
a >>= 2
print(bin(a))

b = 0b101100111000111101001010  # 101100111000 111101001010   -> f0 f1 f2 f3    n0 n1 n2 n3 ; n: liczba(1-4) f:liczba 0/1
# b = 0xffac
print(b)
print(bin(b))

print('-----')

ostatnie8 = b & 0b11111111
print(bin(ostatnie8))

n3 = (ostatnie8 & 0b11)
print(n3)

x = 0b001100011011  # czyli maska=0011 liczby=[00,01,10,11] zakodowane liczby 1,2,3,4, z maską 0011

row = []
for i in range(4):
    print('*', x & 0b11)
    row.append(1 + (x & 0b11))
    x >>= 2
row = row[::-1]
print(row)

for i in range(4):
    mask = x & 0b1
    x >>= 1
    if mask == 0:
        row[3 - i] = 0
print(row)

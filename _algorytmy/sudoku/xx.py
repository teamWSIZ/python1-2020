# zadanie: przychodzi rząd... trzeba zrobić maskę, i zakodować cyfry...

row = [1, 2, 3, 4]  # mask = [1,1,0,1]

mask = 0
for x in row:
    mask <<= 1
    if x > 0:
        mask |= 0b1

print(bin(mask))

result = mask

for x in row:
    result <<= 2
    if x > 0:
        x -= 1
        result |= (x & 0b11)

print(bin(result))
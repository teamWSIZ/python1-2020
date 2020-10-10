print('Hello World!')

x = 12
y = 38
z = x + y
w = x**y
print(f'x + y = {z}')
print(f'x do potęgi y = {w}')
# teraz jak działają napisy (string-i) w python

s = 'abrać'
b = 'kadabra'
print(s)
print(s+b)
print(len(s))

# metody dla string-ów
print(s.__contains__('ra'))  # poszukiwanie podnapisu 'ra' w napisie `s`

print('๓๓๓๓๓๓๓๓๓'.isdigit())
print('abra kadabra'.upper())

mod = 15

"""
2 
10
18 -> 3
11
19 -> 4
12
20 -> 5


(a - b ) % mod ... (a + mod - b ) % mod


istnieje "modular inverse":

mając "a" (<mod) znaleźć takie "a_" (<mod), że

(a * a_ ) % mod = 1

Liczba "P" (roll_p) jest dana, i < MOD
"""


def compute_hash(s: str, roll_p: int, mod: int):
    h = 0
    for c in s:
        c = ord(c)
        h = (h * roll_p + c) % mod
    return h


def mod_inverse(a, mod):
    print('*')
    a = a % mod
    return 0 if a == 0 else ((1 - mod_inverse(mod % a, a) * mod) // a) % mod


MOD = 1000000007
MOD2 = 1000000009

# a = 1007
# a_ = mod_inverse(a, MOD)
# print(a_)
# print((a_ * a ) % MOD)

print(compute_hash('Litwo ojczyzno moja...', 38, MOD))
print(compute_hash('Litwo ojczyzon moja...', 38, MOD))  # ~ MD5 / SHA-1 ... SHA256 ....

print(compute_hash('Litwo ojczyzno moja...', 38, MOD2))
print(compute_hash('Litwo ojczyzon moja...', 38, MOD2))  # ~ MD5 / SHA-1 ... SHA256 ....
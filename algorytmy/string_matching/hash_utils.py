"""

Rolling hashes,

hash_next = (hash_prev * roll_p + new_char) % mod
hash = c[0] * roll_p**(n-1) + c[1] * roll_p**(n-2) + ... + c[n-1]    % mod


Basic:
https://codeforces.com/blog/entry/60445

Adv:
https://codeforces.com/blog/entry/60442

rng_58:
http://rng-58.blogspot.com/2017/02/hashing-and-probability-of-collision.html

Primes - good for `mod`
m = 1000000007,1000000009, 1000000021
m = 10007
m = 100003
m = 1009, 1013, 1019

"""


from random import randint

# m = 1019
# m = 10007
mod = 100003
# m = 1000000007
roll_p = 1234
ns = 26


def mod_pow(x, exp, mod):
    if exp == 0:
        return 1
    res = 1 if (exp % 2 == 0) else x
    half = mod_pow(x, exp // 2, mod)
    return (res * half * half) % mod


def random_string(nsymbols, length):
    num = []
    for i in range(length):
        num.append(chr(randint(0, nsymbols - 1) + 97))  # 'a' + ...
    return ''.join(num)


def compute_hash(s: str, roll_p: int, mod: int):
    h = 0
    for c in s:
        c = ord(c)
        h = (h * roll_p + c) % mod
    return h


def get_ppow(p, len):
    return mod_pow(p, len - 1, mod)


def shift_hash(prev_hash, ppow, mod, roll_p, in_char, out_char):
    """
    For rolling hash: ppow == p**(len(window) - 1) % mod
    """
    incoming_number = ord(in_char)
    outgoing_number = ord(out_char)
    return ((prev_hash + mod - (outgoing_number * ppow) % mod) % mod * roll_p + incoming_number) % mod


# generowanie hashów z napisów

s = 'abra kadabra loem ipsum'


def compute_hash(s):
    hash = 1
    p = 17
    m = 1013

    for c in s:
        x = ord(c)
        hash = (hash * p + x) % m
    return hash


print(compute_hash('kadabrx'))

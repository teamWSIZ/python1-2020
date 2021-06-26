"""
Kodujemy rząd pozycji
00 00 00 00 4x2B... rząd wartości = 8bitów = 1B
flaga... 4-bitowa...maska zer rzędu = 4bity  = 0.5B ...
====
łącznie 12 bitów na rząd...
czyli 48 bitów na board ... zmieści się w pojedynczym int-cie 8-bytes...


"""
from typing import List


# b = [[0, 0, 0, 1], [1, 0, 2, 3], [0, 1, 2, 4], [0, 0, 0, 0]]    # 16 * 8 = 128 B

def decode_row(x: int) -> List[int]:
    row = []
    for i in range(4):
        row.append(1 + (x & 0b11))
        x >>= 2
    row = row[::-1]

    for i in range(4):
        mask = x & 0b1
        x >>= 1
        if mask == 0:
            row[3 - i] = 0
    return row


def encode_row(row: List[int]) -> int:
    mask = 0
    for x in row:
        mask <<= 1
        if x > 0:
            mask |= 0b1
    result = mask
    for x in row:
        result <<= 2
        if x > 0:
            x -= 1
            result |= (x & 0b11)
    return result


def encode_board(board) -> int:
    nums = [encode_row(r) for r in board]
    result = 0
    for n in nums:
        result <<= 12
        result |= n
    return result


def decode_board(x: int) -> List[List[int]]:
    result = []
    for i in range(4):
        encodedrow = x & 0b111111111111 # ostatnie 12 bitów
        result.append(decode_row(encodedrow))
        x >>= 12
    return result[::-1]


print(decode_row(0b011000011011))  # [0, 2, 3, 0]
print(decode_row(0b111100011011))  # [1, 2, 3, 4]
print(decode_row(0b111000011011))  # [1, 2, 3, 0]
print(decode_row(0b111110101111))  # [3, 3, 4, 4]

print('--------')
code = encode_row([0,4,2,1])
print(decode_row(code))
print('*********')

b = [[0, 0, 0, 1], [1, 0, 2, 3], [0, 1, 2, 4], [4, 1, 1, 1]]
x = encode_board(b)
print(bin(x))
B = decode_board(x)
print(B)

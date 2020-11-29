def g(x):
    if x < 0:
        raise RuntimeError('X jest mniejsze niż 0!')
    return x


# g(-1)

for i in [2, 3, 4, -1, 2, 3, 4]:
    print(g(i))

#     try:
#         g(i)
#     except RuntimeError as e:
#         print(f'powstał błąd: {e} dla i={i}')

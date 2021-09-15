from datetime import datetime
from math import sin


# def timeit(method):
#     def timed(*args, **kw):
#         ts = datetime.now().timestamp()
#         result = method(*args, **kw)
#         te = datetime.now().timestamp()
#         print(f'Duration: {te - ts:.3f}s')
#         return result
from timeit import timeit


@timeit
def jjj():
    x = 0
    for j in range(10 ** 7):
        x += sin(j)
    print(x)


if __name__ == '__main__':
    jjj()

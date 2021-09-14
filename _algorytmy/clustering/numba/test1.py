from datetime import datetime

from numba import jit
import random


def ts():
    return datetime.now().timestamp()


@jit(nopython=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


t_start = ts()
monte_carlo_pi(10 ** 8)
t_end = ts()
print(f'execution time: {t_end - t_start:.3f}s')

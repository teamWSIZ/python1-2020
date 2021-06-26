from datetime import datetime
from heapq import heappop


def ts():
    return datetime.now().timestamp()

def delta(st,en):
    print(f'Elapsed: {(en-st)*1000:.3f}ms')


def print_heap(h):
    while len(h)>0:
        print(heappop(h))
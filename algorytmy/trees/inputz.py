import sys

input = sys.stdin.readline


def ri(): return [int(i) for i in input().split()]


def rs(): return input().split()[0]


def read_test_case(filename=None):
    global input
    if filename:
        sys.stdin = open(filename, 'r')
        input = sys.stdin.readline
    n = ri()[0]
    chs = [ri() for i in range(n)]
    return n, chs

if __name__ == '__main__':
    n, chs = read_test_case('t0.txt')
    print(n)
    print(chs)

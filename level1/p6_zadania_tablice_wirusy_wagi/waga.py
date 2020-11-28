import itertools
import unittest
from typing import List
from random import randint, seed

"""
Podana jest lista zabytkowych monet, każda oznaczona jedynie ich wagą. 
Monety trzeba podzielić na monety grupy o równej (łącznej) wadze. Ocenić, czy da się to zrobić...

- wersja 1, prosta: poprzez wyznaczenie pozycji w liście tak, że elementy 
    na lewo od tej pozycji wchodzą do grupy1, a na prawo od niej (włącznie) do grupy 2. 
- wersja 2, trudniejsza: poprzez dowolny podział monet. 

[Uwaga: monet jest nie więcej niż 20.]

"""


def waga(coins: List[int]):
    n = len(coins)
    for a in itertools.product(range(2), repeat=n):
        left = []
        rght = []
        for i in range(n):
            if a[i] == 0:
                left.append(coins[i])
            else:
                rght.append(coins[i])
        if sum(left) == sum(rght):
            return True
    return False


def generate_equal_sum_lists():
    a = []
    b = []
    for _ in range(3):
        a.append(randint(1, 30))
        b.append(randint(1, 30))

    diff = sum(a) - sum(b)
    if diff > 0:
        b.append(diff)
    else:
        a.append(-diff)
    return a, b


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(waga([1, 1, 2]), True, '')

    def test_2(self):
        self.assertEqual(waga([1, 2, 3, 2]), True, '')  # True w wersji 2

    def test_3(self):
        self.assertEqual(waga([1, 1, 1]), False, '')

    def test_4(self):
        self.assertEqual(waga([1, 1, 1]), False, '')

    def test_5(self):
        self.assertEqual(waga([1, 1, 1, 1, 1, 1, 6]), True, '')

    def test_6(self):
        self.assertEqual(waga([2, 2, 3, 4, 5]), True, '')  # True w wersji 2

    def test_random(self):
        MAX = 100
        seed(111)
        for _ in range(MAX):
            a, b = generate_equal_sum_lists()
            a.extend(b)  # łączymy listy, ale wiemy, że rozwiązanie isnieje, bo sum(a) == sum(b)
            self.assertEqual(waga(a), True)

    def test_X(self):
        self.assertEqual(waga([1, 2, 2, 7]), False, '')


if __name__ == '__main__':
    unittest.main()

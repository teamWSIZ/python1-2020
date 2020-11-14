import unittest
from typing import List
from random import randint, seed

"""
Późno wieczorem w ulubionej kebabiarni po koncercie ustawiła się kolejka.
 Lista zamówień jest podana -- składa się wyłącznie z liczby kebabów które każdy z klientów 
 ma zamiar zamówić. Każdy kebab wymaga `x` porcji mięsa i `y` porcji sałaty. 
 Kebabiarnia ma do dyspozycji już tylko `xx` porcji mięsa i `yy` porcji sałaty. 
 Podać numer (startując od 0) ostatniego klienta który zostanie obsłużony, 
tj. całe jego zamówienie zostanie zrealizowane. 

"""


def kebab(x, y, xx, yy, zam: List):
    return 0


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(kebab(1, 1, 5, 5, [3, 3, 3, 3, 3]), 0, '')

    def test_2(self):
        self.assertEqual(kebab(1, 1, 6, 6, [3, 3, 3, 3, 3]), 1, '')

    def test_3(self):
        self.assertEqual(kebab(1, 2, 10, 10, [2, 2, 2, 2]), 1, '')

    def test_4(self):
        self.assertEqual(kebab(1, 10, 100, 100, [1 for i in range(100)]), 9, '')

    def test_5(self):
        self.assertEqual(kebab(1, 1, 10, 10, [1]), 0, '')

    def test_7(self):
        self.assertEqual(kebab(1, 1, 10, 10, [1, 1]), 1, '')

    def test_6(self):
        seed(112)
        self.assertEqual(kebab(4, 7, 500, 500, [randint(1, 10) for i in range(100)]), 9, '')


if __name__ == '__main__':
    unittest.main()

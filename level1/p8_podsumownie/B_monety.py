import unittest
import random
from typing import List

"""
Zadanie B:
Dany jest zbiór nominałów monet, np. (1,2,5,10) lub (2,7,9), oraz kwota X. 
Wyznaczyć _jakiś_ sposób rozmienienia X na podane nominały, lub napisać że to nie możliwe.

"""


def monety(X, nom: List[int]) -> List[int]:
    return []


class TestSum(unittest.TestCase):
    def all_coins_valid(self, res, nom):
        all_ok = True
        for r in res:
            all_ok &= nom.__contains__(r)
        return all_ok

    def test_1(self):
        X = 2
        nom = [1, 2, 5]
        res = monety(X, nom)

        self.assertEqual(sum(res), X, '')
        self.assertTrue(self.all_coins_valid(res, nom))

    def test_2(self):
        xx = [10, 20, 30, 40, 50, 60, 99, 113]
        nom = [1, 2, 5]
        for X in xx:
            res = monety(X, nom)
            self.assertEqual(sum(res), X, '')
            self.assertTrue(self.all_coins_valid(res, nom))

    def test_3(self):
        xx = [10, 20, 30, 40, 50, 60, 99, 113]
        nom = [2, 5, 7]
        for X in xx:
            res = monety(X, nom)
            self.assertEqual(sum(res), X, '')
            self.assertTrue(self.all_coins_valid(res, nom))


if __name__ == '__main__':
    unittest.main()

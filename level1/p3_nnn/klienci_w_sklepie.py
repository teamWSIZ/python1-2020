import unittest

"""
dana jest tablica liczb klientów w sklepie w odcinkach 10-minutowych...
czyli np. od 16:00 - 16:10, potem 16:10 - 16:20, potem 16:20-16:30 itd...
czyli
klienci = [4,6,9,1,10,5,8,30,4,2,1]
"""


def ile_w_30min(klienci):
    return 0


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(ile_w_30min([1, 1, 1, 1]), 3, 'Dla listy jedynek -- po prostu 3')

    def test_2(self):
        self.assertEqual(ile_w_30min([1, 0, 0, 1]), 1, 'Pojedynczy klienci')

    def test_3(self):
        self.assertEqual(ile_w_30min([4, 6, 9, 1, 10, 5, 8, 30, 4, 2, 1]), 43, 'Realistyczny przykład')

    def test_4(self):
        self.assertEqual(ile_w_30min([1] * 100000), 3, 'Długa lista')


if __name__ == '__main__':
    unittest.main()

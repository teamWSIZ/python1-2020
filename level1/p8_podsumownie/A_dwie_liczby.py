import unittest
import random

"""
Dane są monety liczby: (a,b), a<b<10**6; startujemy od liczby `a`; 
w jednym kroku można dodać do niej 1, lub pomnożyć ją przez 2. 
Wyznaczyć po ilu krokach minimalnie można osiągnąć liczbę `b`. 

"""


def dwie(a, b):
    MX = 1000010
    cost = [1000] * MX
    cost[a] = 0
    for i in range(a, b):
        if i * 2 < MX:
            cost[i * 2] = min(cost[i * 2], cost[i] + 1)
        cost[i + 1] = min(cost[i + 1], cost[i] + 1)
    return cost[b]


class TestSum(unittest.TestCase):

    def test_1x(self):
        self.assertEqual(dwie(2, 5), 2, '')

    def test_1d(self):
        self.assertEqual(dwie(2, 40), 5, '')

    def test_1(self):
        self.assertEqual(dwie(1, 4), 2, 'Pierwszy')

    def test_2(self):
        self.assertEqual(dwie(6, 28), 3, 'Drugi')

    def test_3(self):
        self.assertEqual(dwie(5, 5), 0, 'Trzeci')

    def test_4(self):
        self.assertEqual(dwie(1, 11), 5, 'Czwarty')

    def test_5(self):
        self.assertEqual(dwie(0, 12), 5, 'Piąty')

    def test_rnd1(self):
        random.seed(111)
        a = []
        b = []
        for i in range(10):
            r = random.randint(1, 1000)
            a.append(r)
            b.append(r + random.randint(1000, 10000))

        res = [dwie(aa, bb) for (aa, bb) in zip(a, b)]
        self.assertEqual(res, [488, 838, 85, 114, 474, 562, 368, 97, 93, 61], '¯\_(ツ)_/¯')


if __name__ == '__main__':
    unittest.main()

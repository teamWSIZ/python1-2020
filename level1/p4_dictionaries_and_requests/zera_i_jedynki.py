import unittest

"""
Dana jest lista liczb skadająca się z 0 i 1, czyli np. 
a = [0,1,0,0,1,0,1,1,1,0,1]
lub
a = [1,1,0,1,1,0,0,0]

Napisać funkcję która policzy ile jest łącznie zer między dwoma skrajnymi 1'kami. W przykładzie
pierwszym najbardziej skrajna 1-ka z lewej jest na pozycji 1 (licząc od 0), a najbardziej skrajna 
z prawej na ostatniej pozycji (czyli -1, wg. konwencji pythona). Wynikiem jest wtedy 4 
(bo 0 na pozycji 0 nie wchodzi do sumy). Podobnie w drugim przykładzie zera na końcu listy 
"nie wchodzą do sumy" i wynikiem jest 1. 

"""
from random import randint, seed

seed(111)


def ile_zer(aa):
    started = False
    sum = 0
    bag0 = 0
    for a in aa:
        if a == 1:
            started = True
            sum += bag0
            bag0 = 0
        if started and a == 0:
            bag0 += 1
    return sum


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(ile_zer([1, 1]), 0, '')

    def test_2(self):
        self.assertEqual(ile_zer([1, 0]), 0, 'Skrajna to ta sama 1ka, L=0, R=0')

    def test_3(self):
        self.assertEqual(ile_zer([1, 0, 1]), 1, '')

    def test_4(self):
        self.assertEqual(ile_zer([1, 0, 0, 0, 1, 0, 0, 1, 0, 0]), 5, '')

    def test_5(self):
        self.assertEqual(ile_zer([0, 0, 0, 1, 0, 0, 0, 0, 0, 1]), 5, '')

    def test_6(self):
        self.assertEqual(ile_zer([1]), 0, '')

    def test_7(self):
        seed(111)
        w = [randint(0, 1) for i in range(10)]
        # print(w)
        self.assertEqual(ile_zer(w), 3, 'test losowy, seed(111) zapewnia powtarzalność `w`')

    def test_8(self):
        seed(117)
        w = [randint(0, 1) for i in range(10000)]
        # print(w)
        self.assertEqual(ile_zer(w), 5024, 'test losowy, seed(111) zapewnia powtarzalność `w`')


if __name__ == '__main__':
    unittest.main()

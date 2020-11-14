import unittest
from typing import List

"""
Dana jest kwadratowa tablica 2-wymiarowa np. [[1, 2, 3], [2, 3, 4], [1, 2, 3]]. 
Sprawdzić czy suma każdego z rzędów i każdej z kolumn jest równa (wszystkie te liczby są równe).

"""


def sudoku(tab: List):
   return True



class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sudoku([[1, 1], [1, 1]]), True, '')

    def test_2(self):
        self.assertEqual(sudoku([[1, 2], [1, 2]]), False, '')

    def test_3(self):
        self.assertEqual(sudoku([[1, 1], [2, 2]]), False, '')

    def test_4(self):
        w = [[1 for i in range(10)] for _ in range(10)]
        self.assertEqual(sudoku(w), True, '')

    def test_5(self):
        w = [[1 for i in range(10)] for _ in range(10)]
        w[0][0] = 2
        self.assertEqual(sudoku(w), False, '')




if __name__ == '__main__':
    unittest.main()

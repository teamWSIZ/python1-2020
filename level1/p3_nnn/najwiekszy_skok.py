import unittest


# [1,2,8,2,6]
# Mając daną listę >=2 elementów wyznaczyć najwięszą wartość w[i+1]/w[i]...

def max_skok(lista):
    # tu napisać kod...
    return 0


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(max_skok([1, 1, 1, 1]), 1, 'Dla listy stałej -- 1')

    def test_2(self):
        self.assertEqual(max_skok([1, 2]), 2, 'Prosty przypadek -- skok dwukrotny')

    def test_3(self):
        self.assertEqual(max_skok([1, 2, 6, 60]), 10, 'Ostatni duży skok')

    def test_4(self):
        self.assertEqual(max_skok([8, 4, 0.1, 0.00000001]), 1 / 2, 'Lista malejąca')

    def test_5(self):
        self.assertEqual(max_skok([16, 8, 4, 2, 1, 2, 4, 8, 16]), 2, 'Lista malejąco rosnąca')


if __name__ == '__main__':
    unittest.main()

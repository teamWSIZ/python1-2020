import unittest
from typing import List

"""
Zadany jest przekrój nory królika wykopanej w ziemi, formalnie w postaci dwóch napisów równej długości (n)
składających się wyłacznie ze znaków '.' (powietrze) i 'sim_annealing' (ziemia). Królik wchodzi
do nory od lewej strony (pozycja 0) i ma przejść do strony prawej (pozycja n-1) przy czym:
- może poruszać się wyłącznie po polach z powietrzem, '.',
- może przechodzić wyłącznie do pól sąsiadujących z tym w którym się znajduje idąć
w prawo, górę lub dół (nie "po skosie")

Ocenić, czy królik przejdzie przez całą norę bez problemów.  

"""

# tu da się przejść
# ------------------------
# → ........sim_annealing......xxx....
# → .....xx....xxx.....xxx
# ------------------------

# ↓↓ tu nie da się przejść
# ------------------------
# → ........sim_annealing.....xxxx....
# → .....xx....xxx.....xxx
# ------------------------




def rabbit_hole(map: List[str]):
    return True


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(rabbit_hole(['...', '...']), True, '')

    def test_2(self):
        self.assertEqual(rabbit_hole(['...', 'xxx']), True, '')

    def test_3(self):
        self.assertEqual(rabbit_hole(['xxx', '..sim_annealing']), False, '')

    def test_4(self):
        self.assertEqual(rabbit_hole(['sim_annealing..', '.sim_annealing.']), False, '')

    def test_5(self):
        self.assertEqual(rabbit_hole(['...xxx...', 'xx.....xx']), True, '')

    def test_6(self):
        self.assertEqual(rabbit_hole(['.sim_annealing', 'sim_annealing.']), False, '')


if __name__ == '__main__':
    unittest.main()

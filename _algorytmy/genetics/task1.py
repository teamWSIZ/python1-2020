import unittest


def validate_dna(dna: str) -> bool:
    ok = {'A', 'T', 'G', 'C'}
    for c in dna:
        if c not in ok:
            return False
    return True


# def validate_dna(dna: str):
#     dna_chars = {'T', 'C', 'A', 'G'}
#     parsed_dna = set(dna)
#     for element in parsed_dna:
#         if dna_chars.__contains__(element):
#             continue
#         else:
#             return False
#     return True


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(validate_dna('AATTGG'), True, '')
        self.assertEqual(validate_dna('X'), False, '')
        self.assertEqual(validate_dna('AATTGGX'), False, '')
        self.assertEqual(validate_dna(''), True, '')
        self.assertEqual(validate_dna('ACTG'), True, '')




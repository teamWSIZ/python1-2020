from random import randint

map = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
       "UCU": "S", "UCC": "s", "UCA": "S", "UCG": "S",
       "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
       "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
       "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
       "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
       "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
       "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
       "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M|START",
       "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
       "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
       "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
       "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
       "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
       "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
       "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }


def random_rna(length: int) -> str:
    l = ["U", "C", "A", "G"]
    w = []
    for _ in range(length):
        w.append(l[randint(0, 3)])
    return ''.join(w)


def translate_to_aminoacids(rna: str) -> str:
    # pociąć rna na kawałki 3-elementowe, wykorzystać map↑↑, i pozbierać w ciąg nazw aminokwasów (string)
    pass
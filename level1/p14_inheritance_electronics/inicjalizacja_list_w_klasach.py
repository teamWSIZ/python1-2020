from typing import List


class A:
    # lista = []
    lista: List

    def __init__(self):
        self.lista = []




# uwaga -- przypisanie typu ggg=lll przypisuje _referencję_ a nie kopie wartości; te listy będą _ciągle równe_
# lll = [1,2,3]
# ggg = lll
# ggg.append(4)
# lll.append(4)
# print(lll)
# print(ggg)

a1 = A()
a2 = A()

a1.lista.append(1)
a2.lista.append(2)

print(a1.lista)
print(a2.lista)

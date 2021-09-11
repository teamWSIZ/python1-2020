import numpy as np
from scipy.sparse import csr_matrix

# https://en.wikipedia.org/wiki/Sparse_matrix


a = [[1, 2, 0], [0, 0, 3], [4, 0, 5]]
A = csr_matrix(a)  # Compressed Sparse Row matrix

"""
CSR format: 
   V         = [ 10 20 30 40 50 60 70 80 ]
   COL_INDEX = [  0  1  1  3  2  3  4  5 ]   
   ROW_INDEX = [  0  2  4  7  8 ]

Jeśli chcemy dane z rzędu "z", to są one (w V == values, i COL_INDEX == kolumny) na pozycjach między
ROW_INDEX[z] i ROW_INDEX[z+1] ← tą ostatnią wykluczając. 

Wynik: 

10 20  0  0  0  0 
 0 30  0 40  0  0
 0  0 50 60 70  0
 0  0  0  0  0 80

"""

print(A)
print('---')
a_dok = A.todok()  # Dictionary of keys matrix
print(a_dok)

print('---')
for k in a_dok.keys():
    print(f'key:{k} v:{a_dok[k]}')
# print(A.todok().keys())
# print(A.todok()[(2, 0)])

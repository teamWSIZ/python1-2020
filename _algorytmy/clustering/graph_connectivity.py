from sklearn.neighbors import kneighbors_graph
import numpy as np

X = [[0, 0], [0.1, 0.1], [0, 0.2], [0.9, 0.9], [1, 1]]

A = kneighbors_graph(X, n_neighbors=2, mode='connectivity', include_self=False)

print(A)

"""
  (0, 0)	1.0
  (0, 2)	1.0
  (1, 1)	1.0 ...
  """
print(type(A))  # <class 'scipy.sparse.csr.csr_matrix'>

a = A.toarray()  # numpy
print(type(a))  # numpy.ndarray
print(a)  # dense array ... dużo zer...

a_dok = A.todok()
print(a_dok.items())  # dict_items([((1, 0), 1.0), ((2, 0), 1.0), ((0, 1), 1.0), ...])

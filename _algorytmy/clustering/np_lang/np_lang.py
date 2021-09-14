import numpy as np

# from numpy import ndarray

data = [[[0.5, 0.], [1.01, 1.], [0.5, 1]], [1, 1, 0]]
X, y = data  # X = [[0.5, 0], [1.01, 1], [0.5, 1]]
X = np.array(X)
# x1 = X[:, 0]
# print(x1)
print(X[:, 0])  # get x-es from np.array

print('---', np.ndarray.flatten(X[0, :]))

d = np.array([0, 1, 1, 0])
print(np.unique(d))  # w/o counts: [0 1], w/ counts (array([0, 1]), array([2, 2]))

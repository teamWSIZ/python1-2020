import numpy as np

x = np.array([[[1], [2], [3]], [[4], [5], [6]]])
print(x.shape)
print(x)

"""
(2, 3, 1)
[[[1]
  [2]
  [3]]

 [[4]
  [5]
  [6]]]
"""

print(x[1:])
"""
[[[4]
  [5]
  [6]]]
"""

print(x[:, :, 0])
"""
[[1 2 3]
 [4 5 6]]
 """

print('------')
y = x.transpose(2, 0, 1)  # channel to the front dimension
print(y.shape)
"""

"""

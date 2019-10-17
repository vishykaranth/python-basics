import numpy as np

# https://github.com/KeithGalli/NumPy/blob/master/NumPy%20Tutorial.ipynb

a = np.array([[1, 2, 3, 4, 5, 6, 7],
              [8, 9, 10, 11, 12, 13, 14]])
print(a)

print a[1, 5]

# Get a specific row
print a[0, :]

# Get a specific column
print a[:, 2]

# Getting a little more fancy [startindex:endindex:stepsize]
print a[0, 1:-1:2]

a[1, 5] = 20
a[:, 2] = [1, 2]
print a

b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print b

print b[0, 1, 1]


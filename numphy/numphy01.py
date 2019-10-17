import numpy as np

a = np.array([1,2,3], dtype='int32')
print(a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

# Get Dimension
print a.ndim

# Get Shape
print b.shape

# Get Type
print a.dtype

# Get Size
print a.itemsize

# Get total size
print a.nbytes

# Get number of elements
print a.size

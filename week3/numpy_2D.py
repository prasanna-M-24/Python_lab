import numpy as np

# Creating lists
lst1 = [[2, 12], [4, 24]]
lst2 = [[30, 1], [1, 17]]

# Converting lists to NumPy arrays
arr1 = np.array(lst1)
arr2 = np.array(lst2)

print("2D Array-1:\n", arr1)
print("2D Array-2:\n", arr2)

# Dimensions
print("Dimensions of the arrays:\n", arr1.ndim, arr2.ndim)

# Addition
print("Addition of arrays:\n", np.add(arr1, arr2))

# Subtraction
print("Subtraction of arrays:\n", np.subtract(arr1, arr2))

# Element-wise Multiplication
print("Multiplication of arrays:\n", np.multiply(arr1, arr2))

# Matrix multiplication
print("Matrix multiplication:\n", np.dot(arr1, arr2))
print("Matrix multiplication using @ operator:\n", arr1 @ arr2)

# Trace
print("Trace of Array1:\n", np.trace(arr1))

# Transpose
print("Transpose of Array1:\n", np.transpose(arr1))

# Determinant
print("Determinant of Array1:\n", np.linalg.det(arr1))
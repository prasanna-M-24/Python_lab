import numpy as np

# Creating a list
lst = [2, 12, 30, 4, 24]

# Converting list to NumPy array
npArr = np.array(lst)
print("Array:", npArr)
print("Dimensions:", npArr.ndim)

# Array with zeros
a = np.zeros(5)
print("Array with zeros:", a)

# Array with ones
b = np.ones(3)
print("Array with ones:", b)

# Array using arange
c = np.arange(5)
print("After arranging:", c)

# Sum
print("Sum of elements:", np.sum(npArr))
print("Sum:", npArr.sum())

# Maximum
print("Maximum element:", np.max(npArr))
print("Max:", npArr.max())

# Minimum
print("Minimum element:", np.min(npArr))
print("Min:", npArr.min())

# Average / Mean
print("Average of elements:", np.mean(npArr))
print("Average:", npArr.mean())

# Indexing
print("Indexing the elements:", npArr[0], npArr[-1])

# Slicing
print("Slicing of Array:", npArr[0:3])
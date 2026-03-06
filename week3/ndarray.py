import numpy as np

arr = np.ndarray((5), dtype=int)
arr[:] = [5, 10, 15, 20, 25]
print("1D Array:\n",arr)

arr2 = np.ndarray((2,2),dtype = int)
arr2[:] = [[2,12],[4,24]]
print("2D Array:\n",arr2)

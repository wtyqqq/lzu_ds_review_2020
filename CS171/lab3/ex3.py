import numpy as np

a = np.array([[1, 2, 3], [2, 4, 5], [1, 1, 1]])
print(a[np.lexsort(a.T)])


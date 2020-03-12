import numpy as np
A = np.array([[1, .67, .33],
			  [.45, 1, .55],
			  [.67, .33, 1]])
b = np.array([2, 2, 2])
print(np.linalg.solve(A, b))
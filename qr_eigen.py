import numpy as np
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

A = np.array([[5, -2],
			  [-2, 8]])
A1 = A
for i in range(1000):
	q, r  = np.linalg.qr(A1)
	A1 = r.dot(q)

# print(A1)
print("Eigenvalues calculated from QR decomposition:", "%.2f" %A1[0][0],"and",  "%.2f" %A1[1][1])

eig_val, eig_vec = np.linalg.eigh(A)
print("Eigenvalues calculated from 'np.linalg.eigh':", eig_val)
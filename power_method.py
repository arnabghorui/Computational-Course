import numpy as np
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

A = np.array([[ 2, -1,  0],
			  [-1,  2, -1],
			  [ 0, -1,  2]])

A1 = np.array([[1, 0, 0],
			   [0, 1, 0],
			   [0, 0, 1]])

x = np.array([1, 1, 1])
y = np.array([1, 1, 1])
count = 0
eig_val_1, eig_vec_1 = np.linalg.eigh(A)
lamda_true = eig_val_1[2]
# print(lamda_true)
while (True):
	A2 = A1
	A1 = A1.dot(A)
	lamda = np.inner(A1.dot(x), y) / np.inner(A2.dot(x), y)
	v = (A1.dot(x))/ (lamda**count)
	count+=1
	if ( abs(lamda - lamda_true)  < 0.01 ):
		break

print("The largest eigenvalue is:","%.3f" %lamda)
print("The largest eigenvector is:", v)
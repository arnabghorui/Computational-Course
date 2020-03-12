import numpy as np
import math
import time

np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

A = np.array([[0, 1, 1],
			  [0, 1, 0],
			  [1, 1, 0],
			  [0, 1, 0],
			  [1, 0, 1]])

start = time.time()

AtA = (np.transpose(A)).dot(A)	#A^T.A
AAt = A.dot(np.transpose(A))	#A.A^T

eig_val_1, eig_vec_1 = np.linalg.eigh(AtA)
eig_val_2, eig_vec_2 = np.linalg.eigh(AAt)

U = np.zeros( (len(AAt), len(AAt)) )	#initializing U, V^T
Vt = np.zeros( (len(AtA), len(AtA)) )
S = np.zeros(len(AtA))

for i in range(len(AAt)):
	for j in range(len(AAt)):
		U[i][j] = eig_vec_2[i][len(AAt)-j-1] 
#eigh orders its eigenvalues in ascending order. But svd does it in the opposite way. Thus I have rearranged the matrix
for i in range(len(AtA)):
	for j in range(len(AtA)):
		Vt[j][i] = eig_vec_1[i][len(AtA)-j-1]
#to calculate transpose we have written Vt[j][i]
for i in range(len(AtA)):
	S[i] = math.sqrt(eig_val_1[len(AtA)-i-1])

end = time.time()
time1 = end-start




start = time.time()

u,s,vt = np.linalg.svd(A)

end = time.time()
time2 = end-start

print("From the code written, decompositions are:\n","U:\n", U,"\nS:\n", S,"\nVt:\n", Vt, "\nand from np.linalg.svd they are:\n","u:\n", u,"\ns:\n", s,"\nvt:\n", vt)
print("Time taken to execute both processes are:", "%.5f" %time1, "s and", "%.5f" %time2, "s respectively")

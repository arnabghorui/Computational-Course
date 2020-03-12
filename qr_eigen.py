import numpy as np
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

A = np.array([[5, -2],
              [-2, 8]])
A1 = A
count = 0
while True:
    q, r  = np.linalg.qr(A1)
    A1 = r.dot(q)
    if(abs(A1[0][1]) < 10**-10 and abs(A1[1][0]) < 10**-10):
        break
print("Eigenvalues calculated from QR decomposition:", "%.2f" %A1[1][1],"and",  "%.2f" %A1[0][0])

eig_val, eig_vec = np.linalg.eigh(A)
print("Eigenvalues calculated from 'np.linalg.eigh':", eig_val)

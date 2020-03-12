import numpy as np
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

A = np.array([[0.2,  .1,  1.0, 1.0,   0.0],
			  [0.1,  4.0, -1.0, 1.0, -1.0],
			  [1.0, -1.0, 60.0, 0.0, -2.0],
			  [1.0,  1.0,    0, 8.0,  4.0],
			  [0,   -1.0, -2.0, 4.0,  700.]])
b = np.array([1., 2., 3., 4., 5.])
x_true = np.array([7.859713071, 0.422926408, -0.073592239, -0.540643016, 0.010626163])
x_old = np.zeros(5)		#intial guess of the solution
x_new = np.zeros(5)



count = 0
while(True):
	for i in range(5):
		for j in range(i):
			if(j != i):
				x_new[i] = x_new[i] - A[i][j]*x_new[j]
			
		for j in range(i+1,5):
			if(j != i):
				x_new[i] = x_new[i] - A[i][j]*x_old[j]

		x_new[i] = (x_new[i] + b[i])/A[i][i]
	x_old = x_new
	x_new = np.zeros(5)
	
	count+=1
	if(all(abs(x_old - x_true) < 0.01)):
	 	break
	
print("Solution is:",x_old, "and number of steps taken:", count)

import numpy as np
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

A = np.array([ [0.2,  0.1,  1.0, 1.0,  0.0],
			   [0.1,  4.0, -1.0, 1.0, -1.0],
			   [1.0, -1.0, 60.0, 0.0, -2.0],
			   [1.0,  1.0,    0, 8.0,  4.0],
			   [0,   -1.0, -2.0, 4.0,  700]])
b = np.array([1., 2., 3., 4., 5.])

x_true = np.array([7.859713071, 0.422926408, -0.073592239, -0.540643016, 0.010626163])	#true solution
x = np.zeros(5)		#intial guess of the solution
r = b - A.dot(x)
v = r
count = 0

while True:		#infinite loop

	t = np.inner(r, r)/ np.inner(v, A.dot(v))
	x = x + t*v
	r_new = r - t*A.dot(v)
	s = np.inner(r_new, r_new) / np.inner(r, r)
	v = r_new + s*v
	r = r_new

	# print(x)
	count+=1
	if(all(abs(x - x_true) < 0.01)):	#if desired tolerance reached then break
	 	break

print("Solution is:",x, "and number of steps taken:", count)
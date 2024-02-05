import numpy as np 
z = np.random.randint(0,5,(10,3))
print(z)
e = np.all(z[:,1:] == z[:,:-1], axis=1)
u = z[~e]
print(u)

import numpy as np 
z = np.array([1,2,3,4,5])
nz = 3
z0 = np.zeros(len(z)+(len(z)-1)*nz)
z0[::nz+1] = z
print(z0)
import numpy as np 
z = np.random.randint(0,2,(6,3))
t = np.ascontiguousarray(z).view(np.dtype((np.void, z.dtype.itemsize * z.shape[1])))
_, idx = np.unique(t, return_index=True)
uz = z[idx]
print(uz)
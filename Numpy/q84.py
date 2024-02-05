import numpy as np 
z = np.random.randint(0,5,(10,10))
n = 3
i = 1 + (z.shape[0]-3)
j = 1 + (z.shape[1]-3)
c = np.lib.stride_tricks.as_strided(z, shape=(i,j,n,n), strides = z.strides+z.strides)
print(c)
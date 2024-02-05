import numpy as np 
z = np.random.uniform(0,1,(10,10))
u,s,v = np.linalg.svd(z)
rank = np.sum(s > 1e-10)
print(rank)
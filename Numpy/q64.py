import numpy as np 
z = np.ones(10)
i = np.random.randint(0,len(z),20)
z += np.bincount(i, minlength=len(z))
print(z)
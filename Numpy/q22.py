import numpy as np 
z = np.random.random((5,5))
print(z)
z = (z - np.mean(z))/(np.std(z))
print(z)
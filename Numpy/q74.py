import numpy as np 
c = np.bincount([1,1,2,3,4,4,6])
a = np.repeat(np.arange(len(c)),c)
print(a)
import numpy as np 
a = np.arange(3).reshape(3,1)
b = np.arange(3).reshape(1,3)
it = np.nditer([a,b,None])
for x,y,z in it:z[...] = x + y
print(it.operands[2])
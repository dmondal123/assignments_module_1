import numpy as np 
p,n = 10,20
m = np.ones((p,n,n))
v = np.ones((p,n,1))
s = np.tensordot(m,v,axes=[[0,2], [0,1]])
print(s)
import numpy as np 
x = np.random.rand(int(5e7))

print(np.power(x,3))
print(x*x*x)
print(np.einsum('i,i,i->i', x,x,x))
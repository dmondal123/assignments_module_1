import numpy as np 
x = np.random.rand(5,10)
y = x - x.mean(axis=1, keepdims=True)
y = x - x.mean(axis=1).reshape(-1,1)
print(y)
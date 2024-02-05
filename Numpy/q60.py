import numpy as np 
z = np.random.randint(0,3,(3,10))
print((~z.any(axis=0)).any())
z = np.array([
  [0,1,np.nan],
  [1,2,np.nan],
  [4,5,np.nan]
 ])
print(np.isnan(z).all(axis=0))
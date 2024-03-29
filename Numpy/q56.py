import numpy as np 
x, y = np.meshgrid(np.linspace(-1,-1,10), np.linspace(-1,-1,10))
d = np.sqrt(x*x + y*y)
sigma, mu = 1.0, 1.0
g = np.exp(-(d-mu)**2 / (2.0 * sigma**2))
print(g)
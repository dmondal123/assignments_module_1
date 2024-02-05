import numpy as np 
z = np.zeros((5,5), [('x', float), ('y', float)])
z['x'], z['y'] = np.meshgrid(np.linspace(0,1,5),
                             np.linspace(0,1,5))
print(z)
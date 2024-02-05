import numpy as np 
phi = np.arange(0, 10*np.pi, 0.1)
a = 1
x = a*phi*np.cos(phi)
y = a*phi*np.sin(phi)

dr = (np.diff(x)**2 + np.diff(y)**2)**.5 
r = np.zeros_like(x)
r[1:] = np.cumsum(dr)                
r_int = np.linspace(0, r.max(), 200) 
x_int = np.interp(r_int, r, x)       
y_int = np.interp(r_int, r, y)
print(x_int, y_int)
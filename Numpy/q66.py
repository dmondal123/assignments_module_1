import numpy as np 
w, h = 256, 256
i = np.random.randint(0,4, (h,w,3)).astype(np.ubyte)
colors = np.unique(i.reshape(-1,3), axis=0)
n = len(colors)
print(n)
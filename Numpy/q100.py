import numpy as np 
x = np.random.randn(100)
n = 1000
idx = np.random.randint(0,x.size, (n,x.size))
means = x[idx].mean(axis=1)
conf = np.percentile(means, [2.5, 97.5])
print(conf)
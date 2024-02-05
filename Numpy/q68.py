import numpy as np 
import pandas as pd 
d = np.random.uniform(0,1,100)
s = np.random.randint(0,10,100)
print(pd.Series(d).groupby(s).mean())
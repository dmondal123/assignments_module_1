import numpy as np 
np.array(0) / np.array(0) #RuntimeWarning: invalid value encountered in divide
np.array(0) // np.array(0) #divide by zero encountered in floor_divide
np.array([np.nan]).astype(int).astype(float) #invalid value encountered in cast

import numpy as np
a = np.array([[15, 2, 3], 
              [4,5,6]])

h = np.hstack([np.ones((a.shape[0], 1)), a])
print(h)
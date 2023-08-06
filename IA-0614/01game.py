import numpy as np

A = np.linspace(-50, 50, 1000)

np.save('A', A)

B = np.load('A.npy')
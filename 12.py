import numpy as np
a = np.arange(0, 27, 3)

b = list(set(a) - set([0, 3, 6, 9]))
print(b)

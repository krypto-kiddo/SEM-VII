# There's literally nothing to see here.

import numpy as np
arr = np.array([1.1, 2.1, 3.1])
print(arr)
print('number of dimensions :', arr.ndim)
print(arr.dtype)
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

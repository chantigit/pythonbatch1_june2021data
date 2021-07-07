import numpy as np
v1=np.array([1,4,7,3],dtype='int')
print(v1.min())
print(v1.max())
print(v1.sum())
v2=np.array([[1,2,3],[4,5,6]],dtype='int')
print(v2.sum())
print(v2.sum(axis=1))

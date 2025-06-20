#Array shape
import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print("Array shape:::")
print(arr.shape)
#array reshape
import numpy as np
arr=np.array([[1,2,3,4,5,6,7,8,9,10,11,12]])
print("Array reshape::")
newarr=arr.reshape(4,3)
print(newarr)
#1D to 3D
import numpy as np
arr=np.array([[1,2,3,4,5,6,7,8,9,10,11,12]])
print("converting 1D to 3D::")
newarr=arr.reshape(2,3,3)
print(newarr)


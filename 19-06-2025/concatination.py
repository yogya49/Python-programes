#concatinate is a method because it is called with (.) operator--->(.concatinate)
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)
#joining 2d arrays
import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
arr_res=np.concatenate((arr1,arr2),axis=0)
print(arr_res)


#copy method
import numpy as np
arr =np.array([1,2,3,4])
x=arr.copy()
arr[0]=42
print("The copy method")
print(arr)
print(x)
#view method
import numpy as np
arr =np.array([1,2,3,4])
x=arr.view()
arr[0]=42
print(arr)
print(x)
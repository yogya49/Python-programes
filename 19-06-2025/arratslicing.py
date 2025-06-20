#array slicing
#Array[start:end]
#array[start:end:stepsize]
#array[:end]
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[1:5])
print(arr[2:4])
#negative slicing
print("Negative slicing")
print(arr[::-1])
print(arr[-2:-7])
#2d slicing
arr=np.array([[1,2,3,4],[5,6,7,8]])
print("2d slicing")
print(arr[1,1:4])
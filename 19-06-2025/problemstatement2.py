'''write a python program to create an array with 15 elements and reshape it to 2d array with 3 rows and 5 columns
ii)5 rows and 3 columns and print dimension
iii)Reshape the aarray into 3d array with 5 rows 3 columns with one element in each column'''
import numpy as np
arr=np.array([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]])
print("2d array with 3 rows and 5 columns::")
newarr=arr.reshape(3,5)
print(newarr)
newarr2=arr.reshape(5,3)
print(newarr2)
print("the dimension is:",newarr2.ndim)
newarr3=arr.reshape("5 rows 3 columns with one element in each column::",5,3,1)
print(newarr3)


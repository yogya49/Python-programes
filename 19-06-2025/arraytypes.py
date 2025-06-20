#creating arrays of different dimensional
import numpy as np
#zero dimentional
Array1=np.array([10])
print(Array1)
print(type(Array1))
print(Array1.ndim)
#one dimentional
Array2=np.array([1,2,3,])
print(Array2)
print(type(Array2))
print(Array2.ndim)
#two dimentional
Array3=np.array([[1,2,3],[4,5,6]])
print(Array3)
print(type(Array3))
print(Array3.ndim)
#Three dimentional 
Array4=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(Array4)
print(type(Array4))
print("It is" ,Array4.ndim ,"dimensional" )

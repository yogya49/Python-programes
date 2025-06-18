'''write a python program to create a squareshape class and declare the properties as
1) Length
2) Bredth
3) Height
i)Calculate the area of square
ii)Check whether the sides of square's are equal or not
iii)calculate the prrimeter of square (4a)
iv)find the diagonal(route 2a) 
v)find the side length of a square using instance methods'''
class Squareshape():
    def __init__(self,length,bredth,height):
        self.Length=length
        self.Bredth=bredth
        self.Height=height
    def display_shape(self):
        Area=self.Length*self.Bredth
        print(f"The area of square is:{Area}")
    def sides(self):
        if (self.Length==self.Bredth):
            print("equal")
        else:
            print("Not equal")
    def perimeter(self):
        Perimeter=4*self.Length        
        print(f"perimeter:{Perimeter}")  
    def diagonal(self):
        Diagonal=1.414*self.Length
        print(f"The diagonal is:{Diagonal}")
values=Squareshape(3,4,5)
values.display_shape()
values.sides()
values.perimeter()
values.diagonal()
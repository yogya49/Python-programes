'''write a python problem to read  marks of 3 subjects each and print the marks list for individual students along with the class where 
 if studests is more then 90 percent--1st class
 more than 75 percent--2nd class
 third class more than 50 percent
 and less than 50 is fail'''
size=int(input("enter the size:"))
list=[]
for i in range(size):
    temp=input("name of the students are:")
    list.append(temp)
print(list)
a=input("enter the name of 1st student to swap:")
b=input("enter the name of second dtudent to swap:")
a,b=b,a
print(list)

#write a pytho nprogeam to sort a list of numbers with out using sort method
#write a python program to reverse a list of numbers without using reverse method
size=int(input("enter the size of list:"))
elements=[]
for i in range(size):
    num=int(input("enter the element:"))
    a=len(elements)
    elements.append(num)
    for i in range(a):
        for j in range(0,a-1,1):
            if elements[j]>elements[j+1]:
                elements[j],elements[j+1]=elements[j+1],elements[j]
print(elements)
#2nd question
size=int(input("enter the size of the list:"))
elements=[]
for i in range(size):
    num=int(input("enter the elements:"))
    elements.append(num)
rev_list=elements[::-1]
print(num)
print(rev_list)   
    

    
size=int(input("Enter the size of list:"))
list=[]
for i in range(size):
    temp=int(input("enter the element:"))
    list.append(temp)
print(list)
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even List :",even)
print("Odd List :",odd)


#write a python program to remove the duplicate values from the list
list1=[]
temp=[]
numbers=int(input("enter the numbers:  "))
for i in range(numbers):
    temp = int(input())
    list1.append(temp)
print(list1)
new_list=[]
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)



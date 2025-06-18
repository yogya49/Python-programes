#write a python program to read a list elements as input from the user and print a nwew list of numbers which are multliples of 5
size=int(input("enter the size:"))
list=[]
for i in range(size):
    temp=int(input())
    list.append(temp)
print(list)
new_list=[]
for i in list:
    if i%5==0:
        new_list.append(i)
print(list)
print(new_list)

'''write a python program to read a size of list as input from the user and take the list elements also as input from the user and find the
length of the list the maximum element or number present in the list and minimum element and the summation of elements of a list and
print the slorted list in ascending order'''
size=int(input("enter the sizr of the list:"))
num=[]
for i in range(size):
    temp=int(input())
    num.append(temp)
print(num)
print(max(num))
print(min(num))
print(sum(num))
print(sorted(num))

    
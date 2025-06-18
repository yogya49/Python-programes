'''take a list of toy names
remove duplicated
sort and display the list of toy names'''
size=int(input("enter the size of the toys::"))
toys=[]
for i in range(size):
    temp=input("enter the names of toys:")
    toys.append(temp)
print(toys)
new_list=[]
for i  in toys:
    if i not in new_list:
        new_list.append(i)
print(new_list)








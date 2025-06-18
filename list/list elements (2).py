#wrie a python program to read the list elements as input from the user and display the list element using for loop
size=int(input("enter te size of the list"))
prog_lang=[]
#reading the list of elements as an input
for i in range(size):
    temp=input()
    prog_lang.append(temp)
print(prog_lang)          

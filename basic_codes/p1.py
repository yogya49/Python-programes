'''num=int(input())
if(num>0):
    print(" positive number")
elif(num<0):
    print(" negative nuber")
else:
    print("zero")'''
num=int(input())
res=" positive number"if(num>0)else" negative number"
print(f"{num} is{res}")

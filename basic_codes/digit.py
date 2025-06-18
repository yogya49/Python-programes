'''num=int(input())
if(num<=9 and num>=-9):
    print(f"{num} is digit")
else:
    print(f"{num} is a number")'''
#digit or number using ternary
num=int(input())
res= "digit" if(num<=9 and num>=-9) else "number"
print(f"{num} is {res}")

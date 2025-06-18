#to check weather the number is 2 digit or not
num=int(input())
result="2 digit" if(num>=10 and num<=99)else "not a 2 digit number"
print(f"{num} is {result}")

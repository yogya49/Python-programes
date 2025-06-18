#summation of digits
num=int(input("enter number:"))
sum=0
temp=numsumdigits=0
rem=0
while(num!=0):
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum)
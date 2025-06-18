#to print how many digits in the format_list_numbered
num=int(input())
temp=num
count=0
while(num>0 ):
    num=num//10
    count+=1
print(f"{temp} has {count} digits")
    

'''write a python program to read two integer values as input from user
a)add 2 numbers with out using addition operation and with out using predefined function
b)subtract using minus operator and with out using predefined functions'''
'''def sum(a,b):
    while(b!=0):
        carry =a^b
        b=(a&b)<<1
        a=carry
    return a
a=int(input("enter first number:"))
b=int(input("enter a number:"))
print(f"the sum of{a} and {b} is:"sum(a,b))'''
def sub(a,b):
    return a+(~b+1)
a=int(input("enter number:"))
b=int(input("enter 2nd number:"))
print(sub(a,b))
        
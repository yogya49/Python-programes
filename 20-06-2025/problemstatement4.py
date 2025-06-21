'''Write a python program to print square numbers from 1 to n
Write a python program to print square numbers from n to 1
Write a python program to print prime numbers from 1 to n
Write a python program to print square numbers from n to 1'''
n=int(input("Enter the value of n:"))
def print_squares(n):
    if n > 0:
        print_squares(n - 1)
        print(n * n)
print_squares(n)
#reverse
n=int(input("Enter the value of n:"))
def print_squares(n):
    if n > 0:
        print(n*n)
        print_squares(n - 1)        
print_squares(n)


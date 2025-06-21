#write a python program to print natural numbers from 1 to n
N=int(input("Enter numbers:"))
i=0
def NaturalNumbers(N,i):
    i=i+1
    if N==0:
        return
    NaturalNumbers(N-1,i)
    print(f"{i} Mathod Call ")
NaturalNumbers(N,i)


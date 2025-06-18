#write a python program to print the reversed multliplication of n to 1
n=int(input())
for i in range(n,0,-1):
    print(f"multliplication table of {i}:")
    for j in range(n,0,-1):
        print(f"{i} * {j}={i*j}")
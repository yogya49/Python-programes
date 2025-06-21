#create a linkedlist of size ninput the data from the user
class Node:
    def __init__(self,data,):
        self.data=data
        self.next=None
n=int(input("Enter numbers:"))  
head=None
Current=None 
for i in range(n):
    Value=int(input("enter a number:"))
    new_node=Node(Value)
    new_node.next=head.next
    while Current:
        print(Current.data,end="-->")
    Current=Current.next
print("None")
 
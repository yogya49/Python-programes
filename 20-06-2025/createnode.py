class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node=Node(10)
print(node.data)
node1=Node(20)
print(node1.data)
node2=Node(30)
print(node2.data)
node3=Node(40)
print(node3.data)
node4=Node(50)
print(node4.data)
current=node
current.next=node2
node2.next=node3
node3.next=node4
while current:
    print(current.data,end="-->")
    current=current.next
print("none")
    
        
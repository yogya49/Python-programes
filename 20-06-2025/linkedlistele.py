'''#creating a node
class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None
#Creating a singly linked list
class singlyLinkedList:
    def __init__(self):
        self.Head=None
Sll=singlyLinkedList()'''
#Traversal in linked list
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.Head=None
    def insert_Front(self,data):
        new=Node(data)
        new.Next=self.Head
        self.Head=new
    def show(self):
        temp=self.Head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
            print("None")
sll=Sll()
sll.insert_Front(99)
sll.show()


                
        
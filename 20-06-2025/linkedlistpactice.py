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
    def Traversal(self):
        if self.Head is None:
            print("Singly linkedlist is empty")
        else:
            a=self.Head
            while a is not None:
                print(a.data,end="-->")
                a=a.next
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
n1=Node(5)
n2=Node(10)
n3=Node(20)
n4=Node(40)
sll.Head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n3.next=n4
sll.Traversal()
sll.insert_Front(99)
sll.show()


                
        
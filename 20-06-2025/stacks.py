#Stacks 
'''Stackes are simple data structures that allow us to store and retrieve data sequentially
--> A stack is a linear structure like arrays and linked list
--> It is an extract data type of adt
--> In a stack the order in which the data arrives is essential it follows LIFO
--> LIFO order data in session abstraction LIFO stands for *last in first out'''
# Operations in stack
''' In stack insertion and deletion are done at one end called top
----> Insertion it is known as push operation
----> Deletion is known as pop operation'''
class Stack:
    def __init__(self):
        self.Stack=[]
    def Push(self,data):
        self.Stack.append(data)
        print(f"{data} Element is appended")
    def isEmpty(self):
        if len(self.Stack)==0:
            return True
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            self.Stack.pop()
            print(f"Element is Removed")
    def Display(self):
        for i in self.Stack:
            print(i)
stack=Stack()
stack.Push(100)
stack.Push(00)
stack.Push(190)
stack.Push(10)
stack.Push(109)
stack.Display()
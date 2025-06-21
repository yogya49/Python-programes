class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.Head=None
    def Add_node(self,data):
        N_Node=Node(data)
        N_Node.next=self.Head
        self.Head=N_Node
    def Display_list(self):
        Current=self.Head
        while Current:
            print(Current.data,end="-->")
            Current=Current.next
        print("None")
    def count_nodes(self):
        count=0
        temp=self.Head
        while temp:
            count+=1
            temp=temp.next
        return count
    #deleting the first node
    def delete_front(self):
        if self.Head:
            self.Head=self.Head.next
L1=Linkedlist()
L1.Add_node(20.2)
L1.Add_node(12)
L1.Add_node(455.2)
L1.Add_node(6787.2) 
L1.Add_node(232.2)  

print("Total number of nodes:",L1.count_nodes())
print("After deleting first element:",L1.delete_front() )
L1.Display_list()

            
        
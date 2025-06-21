class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None
First=Node(10)
Second=Node(20)
Third=Node(30)
Fourth=Node(40)
Fifth=Node(50)
Sixth=Node(60)
Seventh=Node(70)
head=First
First.Next=Second
Second.Next=Third
Third.Next=Fourth
Fourth.Next=Fifth
Fifth.Next=Sixth
Sixth.Node=Seventh
Current=head
while Current:
    print(Current.data,end="-->")
    Current=Current.Next
print("None")

        
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=None
        self.next=None
        # |prev|data|next|
        #|none|10|none|

#operation to perform on this node so we create a class which can do the operation
class Double_11:
    def __init__(self):
        self.head=None
        self.tail=None

    #to add node
    def add_node(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head =new_node
            self.tail=new_node
        else:
            self.tail.next =new_node # type: ignore
            new_node.prev =self.tail # type: ignore
            self.tail=new_node
    def forward_display(self):
        if self.head is None:
            print("Double linked list is empty!!!")
        else:
            current = self.head
            while current is not None:
                print(current.data,end='<->')
                current=current.next
    def reverse_display(self):
        if self.head is None:
            print("Double linked list is empty!!!")
        else:
            current = self.tail
            while current is not None:
                print(current.data,end='<->')
                current=current.prev

#driver code
d11=Double_11()
# d11.forward_display()
print()
d11.add_node(10)
d11.add_node(12)
d11.add_node(40)
d11.add_node(30)
d11.add_node(60)
d11.add_node(40)
d11.forward_display() 
d11.reverse_display()              
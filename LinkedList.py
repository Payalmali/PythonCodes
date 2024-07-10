class Node:
    def __init__(self,data):
        self.data=data
        self.next=next

class Linked:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next = new_node # type: ignore
            self.tail = new_node
    def display(self):
        if self.head is None:
            print("LinkedList is empty !!!")
        else:
            current=self.head
            while current is not None:
                print(current.data,end='-->')
                current=current.next
#driverCode
n1=Linked()
n1.insert(10)
n1.insert(20)
n1.insert('hello')
n1.display()
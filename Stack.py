class Stack:
    def __init__(self):
        self.stack=[]
    def isempty(self):
        return len(self.stack)==0
    def push(self,value):
        self.stack.append(value)
        # 10|20|30|40|50
    def pop(self):
        if not self.isempty():
            self.stack.pop()
        else:
            print('Stack is Empty')
    def topmost(self):
        if not self.isempty():
            return self.stack[-1]
        else:
            print('Stack is Empty')
    def bottom(self):
        if not self.isempty():
            return self.stack[0]
        else:
            print('Stack is Empty')
    def display(self):
        if not self.isempty():
            for a in self.stack:
                print(a,end="-")
        else:
            print('Stack is Empty')

#driver code
s1=Stack()
s1.display()
s1.push(10)
s1.push(20)
s1.push('hello')
s1.display()
s1.pop()
print()
s1.display()
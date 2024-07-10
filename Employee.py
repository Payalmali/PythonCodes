class Employee:
    company='TCS'
    def __init__(self,name,id,desg,salary):
        self.name=name
        self.id=id
        self.desg=desg
        self.salary=salary
    def info(self):
        
        print('''-------------------------------- ''')
        print("Emlopyee name :",self.name)
        print("Emlopyee id :",self.id)
        print("Emlopyee designation :",self.desg)
        print("Emlopyee salary :",self.salary)
        print('''-------------------------------- ''')
    def increment(self,salary):
        self.salary += int((salary*0.1))
        print(salary)
    

#driver code
print(Employee.company,"Welcome's You")
Emp1 = Employee("Samarth",102,"Engineer",10000) 
Emp1.info()
Emp1.increment(10000)
Emp2 = Employee("Samarth",102,"Engineer",10000) 
Emp2.info()
Emp2.increment(10000)

class Bank:
    #constructor
    def __init__(self,acc_no,name,bal=1000):
        self.acc_no=acc_no
        self.name=name
        self.bal=bal
        self.trans =[]
    def details(self):
        print()
        print("---------------------------------")
        print("Account Number :",self.acc_no)
        print("Account Number :",self.name)
        print("Account Number :",self.bal)
        print("----------------------------------")
        print()
    def credits(self,cr_bal):
        self.bal=self.bal+cr_bal
        print('Rs.',cr_bal,"amount credited in",self.acc_no)
        print("Total balance",self.bal)
        print()
        self.trans.append(['cr',cr_bal])
    def debits(self,db_bal):
        if self.bal > db_bal:
            self.bal=self.bal - db_bal
            print('Rs.',db_bal,"amount debited from ",self.acc_no)
            print("current balance Rs:",self.bal)
            print()
            self.trans.append(['db',db_bal])
        else:
            print("you can't withdraw the amount Rs.",db_bal,"!!!",
                  "your current balance is Rs.",self.bal)
            
    def transaction(self):
        print('''
--------------------------------
          Transaction
--------------------------------
  S.No.     cr/db       amount
        ''')
        i=0
        for a,b in self.trans:
            i=i+1
            print(i,'       ',a,'       ',b)
        print('----------------------------------')
        print()
        print('total balance :',self.bal)

#driver code
print("----------------------------------")
print("Welcome to the BOB Bank")
user1=Bank(1001,"Samarth",5000)
user2=Bank(1002,"Payal",6000)
user1.details()
user2.details()
print()
user1.credits(1000)
user2.credits(5000)
print()
user1.debits(4000)
user2.debits(2000)
user1.transaction()
print("----------------------------------")
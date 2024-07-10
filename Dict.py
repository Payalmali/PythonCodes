#function
def rate_card(Itemcode,Qty):
    rate={
        1:['poha',10],
        2:['jalebi',20],
        3:['samosa',15] ,
        4:['kachori',15],
        5:['dosa',60], 
        6:['idli',40] 
    }
    if Itemcode in rate.keys():
        return rate[Itemcode][0],rate[Itemcode][1]*Qty
    else:
        print('Wrong Input')

#driver code
print('''Welcome to the hotel
    ---------------------------
             menu card
        s.no    food    price
        1        poha    10
        2       jalebi   20
        3       samosa   15
        4       kachori  15
        5       dosa     60
        6       idli     40
    ----------------------------  
      ''')
list1=[]
a_list=[]
Itemcode= int(input("Enter the item"))
Qty =int(input("Enter the Qty"))
food,amount = rate_card(Itemcode,Qty) # type: ignore
list1.append(food)
list1.append(Qty)
list1.append(amount)
a_list.append(list1)
for a in a_list:
    print(a)
print("details---------")
print("food :",food)
print("Quantity :",Qty)
print("Amount :",amount)
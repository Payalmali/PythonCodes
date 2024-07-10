# PythonCodes
# name = input('Enter your name :')
# roll = int(input('Enter your roll :'))
# marks = float(input('Enter marks :'))
# print(name)
# print(roll)
# print(marks)


# #multiple assignment
# a,b,c = 1,2,3 
# print(a)
# print(b)
# print(c)
# a,b,c = 1,2+a,3+b
# print(a)
# print(b)
# print(c)
# a = 6
# b = 3
# print(a,' ',b)
# a,b = b,a
# print(a,' ',b)


#list
# list = [] #empty list
# print(list)
# list = [1,3.6,'python']
# print(list)
# print(type(list))
# list1 = eval(input('Enter elements :'))
# print(list1)


# dictionary
# dict1= {
#     'fruit':'apple',
#     'climate': 'cold',
#     'price': '120'
# }
# print(dict1)
# print(dict1['fruit'])


#if-else
# if 5>2 and 6>2:
#     print('if')
# else: 
#     print('else')

# name = 'PAYAL'
# if name.isupper():
#     print('upper case')
# else:
#     print('lower case')

# age = int(input('Enter your age'))

# if age>=18:
#     print('Eligible')
# else:
#     print('not eligible')

# a = int(input('enter 1 num: '))
# b = int(input('enter 2 num: '))
# c = int(input('enter 3 num: '))

# if a>b and a>c:
#     print('1 is greater',a)
# elif b>c and b>a:
#     print('2 is greater',b)
# else:
#     print('3 is greater',c)

# Rock Paper Scissor
''' 
-----------------------------
r --> rock
p --> paper
s --> scissor

rules
r vs p --> p
p vs s --> s
r vs s --> r
'''
# print('Lets play Rock Paper Scissor')

# user1 =input('Player 1 choose(p,r,s) :')
# user2 =input('Player 2 choose(p,r,s) :')
# if user1==user2:
#     print('Draw !!!!')
# elif user1=='p'and user2=='r':
#     print('User1 is win')
# elif user1=='s' and user2=='p':
#     print('User1 is win')
# elif user1=='r' and user2=='s':
#     print('user1 is win')
# elif user1 and user2 != 'p''r''s':
#     print('Invalid Input')
# else:
#     print('User2 is win')

# for loop
# num=int(input('enter a num :'))
# for a in range(1,11):
#     print(num,'x',a,'=',num*a)

# sum of n natural number
# num2= int(input('enter any natural num :'))
# sum = 0
# for a in range(1,num2+1):
#     sum = sum + a
# print(sum)

# factorial of n number
# num1=int(input('enter any num'))
# fact = 1
# for a in range (1,num1+1):
#     fact = fact*a
# print(fact)

# fibonacci series
# num3=int(input('enter any num :'))
# a=0
# b=1
# for i in range(num3):
#     print(a)
#     c= a+b
#     a=b
#     b=c
# a=0
# b=1
# for i in range(8):
#     c=a+b
#     a=b
#     b=c
#     print (a,end='-')
# name =[1,2,3,4,5]
# for i in reversed(name):
#     print(i)
# for a in range(1,4):
#     for b in range(1,a+1):
#         print(4-a,end=' ')
#     print()
# for a in range(1,4):
#     for b in range(1,5-a):
#         print(4-a,end=' ')
#     print()
# for a in range(1,4):
#     for b in range(1,5-a):
#         print(end=' ')
#     for c in range(1,a+1):
#         print('*',end=' ')
#     print()
'''------------------------------------------------'''
#While Loop
# a=4
# while a<10:
#     print('*')
#     a=a+1
# b=5
# while True:
#     print('Iterater')
#     a=a+1

#     if a==10:
#         print('a=',a)
#         break
# fibonacci series
# num = int(input('Enter a number :'))
# sum=0
# while num>0:
#     digit=num%10
#     sum=num+digit
#     num= num//10
# print('sum :',sum) 

# n = int(input('Enter num :'))
# sum=0
# while n > 0:
#     dig=n%10
#     sum=sum+dig
#     n=n//10
#     if n==0 and sum>9:
#         n=sum
#         sum=0
# print("sum",sum)
'''------------------------------------------'''
# list
# l1 = eval(input('enter the elemenets :'))
# print(l1)

# for a in l1:
#     print(a)

# l1=[4,5,6,7,8,9,10]
# for a in range(len(l1)):
#     l2=l1[-5:-7]+l1[3:6]
# print(l2)


# l3=[1,2,3,4]
# l2=[8,7,6,5]
# l4=l2+l3
# print(l4)
# l4=l2*2
# print(l4)
# slicing in list
# print(l1[0:5:3])
# print(l1[:3])
# print(l1[: :-1])
# print(l1[-5:-3])
# l2 =l1[-1:-4:1]+l1[-5:-7:1]
# print(l2)
# for a in range(len(l1)):
# print(l1[0:3:]+l1[-2: -8:])
# l4=[1,2,3,4,5,6,7,8]
# 1 2 3 4 8 7 6 5
# print(l4[0:4]+l4[:-5:-1])
'''---------------------------------'''
# WAP to remove duplicate elements from list
# l2=[1,2,3,4,5,6,3,2,1,4,5,5]
# l3=[]
# for i in l2:
#     if i not in l3:
#         l3.append(i)
# print(l3)
'''---------------------------------------------'''
# Append function and remove and pop
# l2=[1,2,3,4]
# l2.append('hello') # type: ignore
# print(l2)
# l2.pop(1)
# print(l2)
# l2.remove(2)

l1=[1,2,3,4,5,2,1,3,4,4]
l2=[5,5,6,6,7,7,8]
l3=l1+l2
print(set(l3))

#fibonacci series
num3=int(input('enter any num :'))
a=0
b=1
for i in range(num3):
    c= a+b
    a=b
    b=c
# a=0
# b=1
# for i in range(8):
#     c=a+b
#     a=b
#     b=c
    print (a,end='-')
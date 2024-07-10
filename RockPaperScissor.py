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
print('Lets play Rock Paper Scissor')

user1 =input('Player 1 choose(p,r,s) :')
user2 =input('Player 2 choose(p,r,s) :')
if user1==user2:
    print('Draw !!!!')
elif user1=='p'and user2=='r':
    print('User1 is win')
elif user1=='s' and user2=='p':
    print('User1 is win')
elif user1=='r' and user2=='s':
    print('user1 is win')       
elif user1 and user2 != 'p''r''s':
    print('Invalid Input')
else:
    print('User2 is win')

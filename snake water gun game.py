import random
random_num=random.randint(0,2)

#get user input and prints computers 
print("computer's turn snake(s) water(w) or gun(g)")
b=input("your's turn snake(s) water(w) or gun(g)")


#game funciton
def game(comp,you):
    if comp==you:
     return None
    if comp=="s":
       if you=="w":
           return False
       elif you=="g":
           return True
    if comp=="w":
       if you=="g":
           return False
       elif you=="s":
           return True
       if comp=="g":
        if you=="w":
           return True
       elif you=="s":
           return False
  

#values from which computer will chose
points=["s","w","g"]




compp=points[random_num]


hello=game(compp,b)
print(hello)


#if match tie
if hello==False:
    print("You lose")
elif hello==None:
    print("Match tie")
    print("you chose "+ b +" and computer also choose "+compp)
else:
    print("you win")

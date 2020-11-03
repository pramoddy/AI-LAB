import random
guess=0
n=int(input(print("Enter the number from 1 to :")))
num=random.randint(1,n)
while guess!=num:
    guess=int(input(print("Enter the number")))
    if guess<0:
        print("only positive number")
    elif guess<num:
        print("Lesser than random number ")
    else:
        print("grater than random number")
        

print("Congrasulation, you find it")


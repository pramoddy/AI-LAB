#factorial using while loop
num=int(input("Enter the number :"))
fact=1
if num==0:
    print("Factorial is : 1")
elif num<0:
    print("The given value is negative ")
else:
    while num!=0:
        fact=fact*num
        num=num-1
    print(fact)
    

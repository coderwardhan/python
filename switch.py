def sw(a,b,n):
    if(n==1):
        print("Addition = ",a+b)
    elif(n==2):
        print("Substraction = ",a-b)
    elif(n==3):
        print("Multiplication = ",a*b)
    elif(n==4):
        print("Division = ",a//b)
    else:
        print("You have entered the wrong choise")


a=int(input("Enter the value of a="))
b=int(input("Enter the value of b="))
print("'1' for addition")
print("'2' for Substraction")
print("'3' for Multiplication")
print("'4' for Division")
n=int(input("Enter your choise="))
sw(a,b,n)
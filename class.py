class Harsh:
    def __init__(self):
        print()
    def mul(self,a,b):
        self.a=a
        self.b=b
        c = a * b
        print("Multiplication =",c)
    def add(self,a,b):
        self.a=a
        self.b=b
        c = a + b
        print("Addition =",c)
    def sub(self,a,b):
        self.a=a
        self.b=b
        c = a - b
        print("Substraction =",c)
    def div(self,a,b):
        self.a=a
        self.b=b
        c = a // b
        print("Division =",c)
    
a=int(input("Enter the value of A ="))
b=int(input("Entre the value of B ="))    
h1= Harsh()
h1.add(a,b)
h1.sub(a,b)
h1.mul(a,b)
h1.div(a,b)
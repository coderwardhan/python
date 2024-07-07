n=int(input("Enter the term upto which you want fibonacci series="))
a=int(0)
b=int(1)
print(a)
print(b)
for i in range(1,n):
    t=a+b
    print(t)
    a,b=b,t
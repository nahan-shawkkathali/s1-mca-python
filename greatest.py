a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if((a>b) & (a>c)):
    print("a greatest",a)
elif((b>a) &(b>c)):
    print("b greatest",b)
else:
    print("c greatest",c)



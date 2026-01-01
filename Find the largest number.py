a = int(input("Enter the number"))
b = int(input("Enter the number"))
c = int(input("Enter the number"))
if a>b and a>c:
    print("largest is",a)
elif b>c:
    print("largest is",b)
else:
    print("largest is",c)
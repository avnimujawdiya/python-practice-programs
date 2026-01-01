num = int(input("Enter a number: "))
if num>1:
    for i in range(2,num):
    if num%2==0:
        print("not prime")
        break
    else:
        print("prime")
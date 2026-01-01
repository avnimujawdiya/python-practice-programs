a = int(input("Enter first: "))
b = int(input("Enter second: "))

lcm = a*b
while True:
    if lcm%a==0 and lcm%b==0:
        breaklcm = lcm+1
        print("LCM: ",lcm)

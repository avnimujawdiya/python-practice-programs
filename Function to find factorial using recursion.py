def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num = int(input("enter number:"))
print("factorial: ",factorial(num))









# What is Recursion?
# Ek function apne aap ko hi call kare

# Important rule of recursion
# Base case → jahan recursion ruk jaaye
# Recursive call → function khud ko call kare
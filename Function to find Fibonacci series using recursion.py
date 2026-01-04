def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
terms = int(input("Enter number of term"))
for i in range(terms):
    print(fibonacci(i),end=" ")

    # return fibonacci(n-1) + fibonacci(n-2)
    # Function khud ko call kar raha hai
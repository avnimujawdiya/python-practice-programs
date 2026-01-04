try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print(a/b)

except ZeroDivisionError:
    print("cannot divivded by zero")
except ValueError:

    print("Invalid input")
def sum_of_square(lst):
    sum = 0
    for num in lst:
        sum = sum+num**2
    return sum

lst = [99,4,3,9]
print("sum of square",sum_of_square(lst))
def min_in_list(lst):
    min_val = lst[0]
    for num in lst:
        if num<min_val:
            min_val = num
    return min_val
lst = [2,5,8,3,8,0]
print("minimum: ", min_in_list(lst))

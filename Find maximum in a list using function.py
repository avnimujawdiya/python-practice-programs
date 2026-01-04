def max_in_list(lst):
    max_val = lst[0]
    for num in lst:
        if num>max_val:
            max_val = num
    return max_val
lst = [2,5,4,7,2,8]
print("maximum",max_in_list(lst))
def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]
lst = [5,7,3,9,6]
print("second largest:",second_largest(lst))




    # set duplicate values hata deta hai
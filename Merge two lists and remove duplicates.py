def merge_list(lst1,lst2):
    return list(set(lst1+lst2))
lst1 = [2,5,3,6]
lst2 = [6,7,3,9]
print("Merged unique list:",merge_list(lst1,lst2))
    
def common_elements(lst1, lst2):
    return [x for x in lst1 if x in lst2]

lst1 = [1,2,3,4]
lst2 = [3,4,5,6]
print("Common elements:", common_elements(lst1, lst2))

# for x in lst1
# lst1 ke har element ko ek-ek karke uthao
# Har element ko naam diya: x
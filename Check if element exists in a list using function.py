def exists(lst,val):
    return val in lst
lst = [4,6,2,1,3]
val = 8
print("exists" if exists(lst,val) else "does not exist")

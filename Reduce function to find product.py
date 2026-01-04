from functools import reduce

lst = [1,2,3,4,5]
product = reduce(lambda x,y:x*y,lst)
print(product)

# reduce() ka kaam:
# List ke elements ko combine karke ek single value nikalna
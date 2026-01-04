class person:
    def __init__(self,name,age):
      self.name = name
      self.age = age

p1 = person("Avni",17)
print(p1.name,p1.age)


# class ka matlab: ek blueprint / template
# Person → class ka naam

# __init__ ko constructor kehte hain
# Jab bhi object banate ho, ye automatically run hota hai
# name aur age → data jo object ko milega

# self ka matlab: current object
# Ye batata hai:
# “Is object ka name, is object ka age”

# self.name → object ka variable
# name → jo value user ne di

# p1 → object ka naam
# Person() → class ka use
# "Avni" → name
# 17 → age



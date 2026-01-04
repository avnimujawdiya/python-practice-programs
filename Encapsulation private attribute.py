class person:
    def __init__(self,name):
        self.__name=name # private variable
    def get_name(self):
        return self.__name
p = person("Avni")
print(p.get_name(),)

# __name (double underscore) ka matlab:
#  PRIVATE variable

# Encapsulation ka matlab hota hai:
# data ko hide karke rakhna aur direct access se bachana.

# Object p
#  └── __name = "Avni"   ← private (hidden)
#         ↑
#      get_name()  ← safe access

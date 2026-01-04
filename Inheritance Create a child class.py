class person:
    def __init__(self,name):
        self.name = name

class student(person):
     def __init__(self,name,roll):
         super().__init__(name)
         self.roll = roll

s = student("Avni",2005)
print(s.name,s.roll)

# super() ka matlab: parent class (Person)
# name aur roll = object ke ANDAR ki values (attributes)
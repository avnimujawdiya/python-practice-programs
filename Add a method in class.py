class person:
    def _init_(self,name):
        self.name = name

    def greet(self):
        print("Hello,my name is",self.name)

p1 = person("Avni")
p1.greet()

# def greet(self):
# 👉 Ye ek method hai
# 👉 Method = class ke andar function

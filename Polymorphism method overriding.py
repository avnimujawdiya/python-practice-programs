class animal:
    def speak(self):
        print("Animal sound")

class Dog(animal):
     def speak(self):
        print("bark")

d = Dog()
d.speak()  # Dog class me speak() hai?
           #Dog wala speak() chalega

# def speak(self):
#     print("Bark")
#  YAHI POLYMORPHISM HAI 
#  Same method name: speak()
#  Par different output

# Polymorphism (simple meaning)

# Ek hi method ka naam same ho
# par kaam alag-alag kare
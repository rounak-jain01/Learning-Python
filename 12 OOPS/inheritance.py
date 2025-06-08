class Parent:
    designation = "student"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Your Details are {self.name}, {self.age}")


class Child(Parent):
    pass



obj = Child("Rounak",21)
obj.show()

# obj = Parent("Rounak", 21)
# obj.show()
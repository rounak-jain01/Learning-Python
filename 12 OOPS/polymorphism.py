'''Polymorphism in Python
Polymorphism is a core concept in object-oriented programming that allows methods to do different things based on the object it is acting upon, even if they share the same name. In Python, polymorphism can be achieved through method overriding and operator overloading.'''

'''Polymorphism with Method Overriding
In method overriding, a subclass provides a specific implementation of a method that is already defined in its superclass. This allows the subclass to modify or extend the behavior of the method.'''

class Shape:
    pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side    
    
class Circle(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return 3.14 * self.side**2
    

# c = Circle(8)
# print(c.area())
# s = Square(4)
# print(s.area())

'''Overriding Methods with Different Arguments'''
class Demo:
    def display(self,a):
        print(f"Value of a is {self.a}")

    def display(self, a, b):
        print(f"Value of a is {a} and value of b is {b}")

d = Demo()
# d.display(10)  # This will raise an error because the second display method overrides the first one
d.display(10, 20)  # This will work as expected
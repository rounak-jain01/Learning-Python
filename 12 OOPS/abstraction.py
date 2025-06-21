# '''Data Abstraction in Python'''
# '''Data abstraction is a fundamental concept in object-oriented programming that focuses on hiding the complex implementation details of a system and exposing only the necessary parts to the user. In Python, data abstraction can be achieved using abstract classes and interfaces.'''

# from abc import ABC, abstractmethod

# class Shapes(ABC):
#     def __init__(self,color):
#         self.color = color

#     @abstractmethod
#     def area(self):
#         pass

#     def display(self):
#         print(f"Color of the shape is {self.color}")

# class Circle(Shapes):
#     def __init__(self, color, radius):
#         super().__init__(color)
#         self.radius = radius


#     def area(self):
#         print(f" area is{3.14 * self.radius ** 2}") 



# class Square(Shapes):
#     def __init__(self, color,sides):
#         super().__init__(color)
#         self.sides = sides

#     def show(self):
#         print(f"Color of the square is {self.color} and number of sides is {self.sides}")

#     def area(self):
#         print(f"Side is {self.sides ** 2}")





# obj = Circle("Red", 5)  
# # Creating an instance of Circle with color "Red" and radius 5
# obj.display()  
# # This will print the color of the shape
# s1  = Square("Blue", 4)  
# # Creating an instance of Square with color "Blue" and 4 sides
# s1.area()  
# # This will print the color of the square and number of sides


from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def details(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def speed(self):
        print("The car can go fast.")
    
class SUV(Car):

    def details(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show(self):
        print(f"Brand: {self.brand},\nModel: {self.model}, \nYear: {self.year}")


c = SUV()
c.details("TATA", "Harrier", 2022)
c.show()


'''This code defines an abstract class `Car` with an abstract method `details` and a concrete method `speed`. The `SUV` class inherits from `Car`, implements the `details` method, and adds a `show` method to display the car's details. An instance of `SUV` is created, and its methods are called to demonstrate abstraction and inheritance.
This example illustrates how abstraction allows us to define a common interface for different types of cars while hiding the implementation details. The `SUV` class provides specific details about the car, while the `Car` class defines the general behavior that all cars should have.'''
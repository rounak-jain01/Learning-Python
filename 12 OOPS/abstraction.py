'''Data Abstraction in Python'''
'''Data abstraction is a fundamental concept in object-oriented programming that focuses on hiding the complex implementation details of a system and exposing only the necessary parts to the user. In Python, data abstraction can be achieved using abstract classes and interfaces.'''

from abc import ABC
class Shapes(ABC):
    def __init__(self,color):
        self.color = color
    def area(self):
        pass
    def display(self):
        print(f"Color of the shape is {self.color}")

class Circle(Shapes):
    def __init__(self, color, radius):
        self.radius = radius
        
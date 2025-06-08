'''OOPS CONCEPT'''
'''OOPs approach is used to make management system'''
'''in this we are study 
Classes and Object 
with the help of them we can make 
Inheritance...
Encapsulation...
Polymorphism...
Abstraction...
'''

'''What is Class ?'''
'''A class is a Blueprint for an object(Raw map of making something) '''
# class Factory: #Creation of Class
'''A class has two thing 1-> Attributes, 2-> Methods'''
    #Attributes: they are just variables that defining insise the class
    # a = 12

    #Methods: They are the functions created inside the class
    # def hello():
    #     print("HEllo class")
    #     print(f"I am attribute and my value is {Factory.a}")

'''Whenever we want to access the thing that define inside the class so firstly call the class and then call the particular operation'''

# print(Factory.a) #Accessing Attributes define inside the class
# Factory.hello() #Accessing Method define inside the class
# print(Factory.hello())


'''What is Object ?'''
'''They are child of a class '''
'''Object are the instances(Requirement for making the particular thing)of class '''
'''A object is the type of variable that utilizes the class'''


# class Animal:
#     name = "Dog"
#     def hello(self):
#         print("Bark...")

'''To create an object you have to call the class inside a variable and this varibale becomes an object'''
# obj = Animal() #This is an object
# print(obj.name) #A class objects can access attributes and methods 
# obj.hello()


'''Constructor Function'''
'''It is a function that runs automatically you call the class'''
'''constructor function can take the parameters'''
'''self is a special Keyword use to store the location of object and with the help of this we can save several objects'''
# class factory:
#     def __init__(self,name,color,engine): #Constructor Funtions
#         self.name = name #use the location of objects and save it their details
#         self.color = color 
#         self.engine = engine
#         # print(name)
#         # print(color)
#         # print(engine)
#         # print(self)
#         # print("Hello I will run whenever you call the class")

# obj = factory("Baleno","White","BS4") #Finally providing for Blueprint
# obj2 = factory("Creta","Pink","BS1")
# # obj =  factory()

# print(obj.name)
# print(obj2.engine)\\

'''Attribute'''
'''There are Two types of Attribute in python
1> Class Attribute
2>Object Attribute'''

'''Class Attribute : Variable define inside the class are c/s class attribute'''
'''Object Attribute : This is a type of attribute which is somehow connected to the object of that class'''
# class Animal:
#     name = "Tiger" #Class Attribute

#     def __init__(self,age):
#         self.age = age # Object Attribute



'''Methods'''
''' There are 3 three types of method
    1)Class Method - anything inside the decorator are c/s class method, They cannot access the location of object
    2) Static Method - 
    3) Initialized Method - they are targetting the instance of class
     '''

class Human:
    name = "Rohit"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self): #instance Method - because they are targetting the instance of class 
        print(f"Your name is {self.name}, your age is {self.age}")
    @classmethod #decorator to make class method
    def hello(cls): #These method will not target the location of object but they target the location of class
        print(f"Hello {cls.name}")

    @staticmethod
    def static():
        print("Namaste I am static and I'll not target anything.")


obj = Human("Rounak","21")
obj.info()
obj.hello()
obj.static()




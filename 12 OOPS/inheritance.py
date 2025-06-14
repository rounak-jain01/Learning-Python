'''Single Level Inheritance'''

# class Parent:
#     designation = "student"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"Your Details are {self.name}, {self.age}")


# class Child(Parent):
#     pass



# obj = Child("Rounak",21)
# obj.show()

# # obj = Parent("Rounak", 21)
# # obj.show()



# class Person:
#     def __init__(self,name):
#         self.name = name
#     def display(self):
#         print("Hello",self.name)


# class Employee(Person): 
#     pass

# emp = Employee("Rounak")
# emp.display() 
# This will print "Hello Rounak" as Employee inherits from Person and can access its methods.
# The Employee class inherits the __init__ and display methods from the Person class.

# class Person:
#     def __init__(self,name,phone):
#         self.name = name
#         self.phone = phone


# class Employee(Person): 
#     def __init__(self,name,phone, salary):
#         super().__init__(name,phone) # Call the __init__ method of Person to initialize name

#         self.salary = salary 
# Initialize salary attribute specific to Employee class
# The Employee class has its own __init__ method that initializes both name and salary attributes.

# emp = Employee("Rounak",10000,"Redmi")
# print(emp.salary)   # This will print 1000 as Employee class has its own __init__ method that initializes salary.
# print(emp.name)     # This will print "Rounak" as Employee class inherits from Person and can access its name attribute.
# print(emp.phone) 

'''The super() function is used to call the parent class's methods, allowing us to initialize attributes from the parent class.
# This is useful for avoiding code duplication and ensuring that the parent class's initialization logic is executed. '''



'''Multiple Inheritance'''
# class Person: #Parent Class
#     def __init__(self,name):
#         self.name = name

# class Job: #Another Parent Class
#     def __init__(self,salary):
#         self.salary = salary

# class Employee(Person,Job): #Child Class
    # def __init__(self,name,salary):
    #     super().__init__(name)
    #     super().__init__(salary) 
'''Super() call an error as it tries to call the first parent class's __init__ method,
        which in this case is Person. To resolve this, we can call the __init__ methods of both parent classes explicitly.'''
        # Person.__init__(self,name)
        # Job.__init__(self,salary)
'''when we use multiple inheritance, we need to explicitly call the __init__ methods of both parent classes by their name.
This ensures that both the name and salary attributes are initialized correctly.'''


# emp = Employee("Rounak",450000)
# print(emp.salary) 


'''Multilevel Inheritance'''
'''This is a type of inheritance where a class inherits from another class, which in turn inherits from another class.'''
'''for example, if we have a class A, and class B inherits from A, and class C inherits from B, then C is a subclass of B and A.'''
'''In this case, class C can access the attributes and methods of both class A and class B.'''

class Person: #Parent Class
    '''This is the base class for all persons, containing a name attribute.'''
    def __init__(self,name):
        '''Initialize the Person with a name.'''
        self.name = name

class Employee(Person): #Child Class
    '''This class represents an employee, inheriting from Person and adding a salary attribute.'''
    def __init__(self,name,salary):
        super().__init__(name)
        '''Initialize the Employee with a name and salary.'''
        '''The super() function is used to call the __init__ method of the parent class (Person) to initialize the name attribute.'''
        self.salary = salary

class Manager(Employee): #Child Class
    '''This class represents a manager, inheriting from Employee and adding a department attribute.'''
    def __init__(self,name,salary,department):
        '''Initialize the Manager with a name, salary, and department.'''
        super().__init__(name,salary)
        '''The super() function is used to call the __init__ method of the Employee class to initialize the name and salary attributes.'''
        self.department = department



obj = Manager("Rounak",450000,"IT")
# print(obj.name)        # Accessing name from Person class
# print(obj.salary)     # Accessing salary from Employee class
# print(obj.department)  # Accessing department from Manager class
# This will print:
# Rounak    # 450000    # IT
'''In this example, we have a multilevel inheritance structure where:
- The `Person` class is the base class with a `name` attribute.'''


'''Hierarchical Inheritance'''
class Vehicle:
    def start(self):
        print("Vehicle started")
        
    def stop(self): 
        print("Vehicle stopped")

class Bike(Vehicle):
    def feature(self):
        print("This is Bike Class")

class Car(Vehicle):
    def feature_car(self):
        print("This is Car Class")

c = Car()
# c.start()  # Accessing method from Vehicle class
# c.feature_car()  # Accessing method from Car class
# c.stop()  # Accessing method from Vehicle class

'''In this example, we have a hierarchical inheritance structure where:
- The `Vehicle` class is the base class with methods `start` and `stop`.'''
# - The `Bike` class inherits from `Vehicle` and has its own method `feature`.
# - The `Car` class also inherits from `Vehicle` and has its own method `feature_car`.  

'''Hybrid Inheritance'''
'''Hybrid inheritance is a combination of multiple inheritance types, such as single, multiple, multilevel, and hierarchical inheritance.'''


class Person:
    def show(self):
        print("This is Person class")

class Employee(Person):
    def show_employee(self):
        print("This is Employee class")

class Freelancer:
    def freelancing(self):
        print("This is Freelancer class")

class teamlead(Employee,Freelancer):
    def lead(self):
        print("This is Teamlead class")

obj = teamlead()
obj.show()  # Accessing method from Person class
obj.show_employee()  # Accessing method from Employee class
obj.freelancing()  # Accessing method from Freelancer class
obj.lead()  # Accessing method from Teamlead class
# This will print:
# This is Person class  
# This is Employee class
# This is Freelancer class
# This is Teamlead class
'''In this example, we have a hybrid inheritance structure where:
- The `Person` class is the base class with a method `show`.
- The `Employee` class inherits from `Person` and has its own method `show_employee`.
- The `Freelancer` class is independent and has its own method `freelancing`.
- The `teamlead` class inherits from both `Employee` and `Freelancer`, and has its own method `lead`.'''
'''This allows the `teamlead` class to access methods from both `Employee` and `Freelancer`, demonstrating hybrid inheritance.'''
'''In Python, inheritance allows us to create a new class that inherits attributes and methods from an existing class.
This promotes code reuse and establishes a relationship between classes, enabling us to build complex systems more easily.'''

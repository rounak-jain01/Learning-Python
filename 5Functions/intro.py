'''
#function Definiton
Syntax:
def function_name(parameters):
    block Statement(s)

#Function Calling
function_name(arguments)
'''

# ex:
# Function Declartation or Function Definition
# def sum(a,b):
#     print(a+b)

# Function Calling
# sum(4,4)

'''pure and Impure Function

Impure function is a type of Function in which we use things that are define outside the scope of Functoin
for example
'''

# a = int(input("Input 1: "))
# b = int(input("Input 2: "))

# def mysum():
#     print(a+b)
# mysum()

'''In the above example we define a and b outside the scope of mysum function'''


'''
Pure Function is a type of function which use only use things inside there scope
'''
# def mysum():
#     a = int(input("Input 1: "))
#     b = int(input("Input 2: "))
#     print(a+b)
# mysum()


'''Parametrized Function'''
# def mysum(a, b): #-> Parameters
#     print(a+b)

# a = int(input("Input 1: "))
# b = int(input("Input 2: "))
# mysum(a, b) #-> Arguments

'''Arguments are of three types -> Default Argument, keyword arguments, positional arguments'''
'''Positional Arguments -> during calling the order of argumetns is same as the order or paremeters -> def sum(a,b)
sum(13,14) -> here a = 13 and b = 14'''


'''Keyword Arguments -> here we define the arguments using as keyword like during calling we specify the keyword like a = 14, b = 15'''
'''  def add(a,b)
     add(b=14,a=46)'''

'''Default Arguments -> here we define the arguments in the parameteres
    def add(a,b,c=17)
    add(12,14)'''






'''Non Parametrized Function'''
# def mysum():
#     a = int(input("Input 1: "))
#     b = int(input("Input 2: "))
#     print(a+b)
# mysum()


'''Return Function'''
# def sum():
#     a = 5
#     b = 5
#     c = a + b
#     return c

# res = sum()
# print(res)

'''Rules of Return
1) There must be only one return in a function
2) After Return no code is reachable
3) We can return only single value/variable/entity
'''

# def sum(a,b):
#     return a + b

# res = sum(5,7)
# print(res)

'''Lambda Funciton: uses to write a single line function
suntax:
var_name = lambda parameters : return-expression
'''

# sum = lambda a, b : a+b
# res = sum(12,45)
# print(res)


'''Primitive vs Reference'''
'''Primitive - int,float, bool, strings, void -> immutable/non reference -> Capable to create the Copies..'''
'''Reference -  list,tuple,set,dictionary -> mutable/non reference -> Not Capable to create Copies...'''

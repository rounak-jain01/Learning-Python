'''Anything on owr keyboard and inside double qoutes is a string'''
# a = "fobvnefioj4094u3n 65654354@!#$@()_"

name = "Rounak" #it is a string

'''Inside string there is positive or negative indexing 
If i want to print a certain letter in the string then we used indexing'''

# Positive Indexing
print("Normal String:",name) #o/p = Rounak
print("Positive Indexing:",name[1]) #o/p = o

# Negative Indexing
print("Negative Indexing:",name[-1]) #o/p = k
print("Negative Indexing:",name[-3]) #o/p = n


'''-----Slicing-----
syntax:-
string_name[start:end-1:steps]
'''

print("Slicing in string:",name[0:3:1])
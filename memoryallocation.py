'''Deep Copy'''
# a = [10,20,30,40,50]
# b = a
# print(b)
# b[0] = 100
# print(b)
'''Here basically it store the address of that variable not create the another copy of that variable...'''
'''But'''
# print(a)
'''Shallow Copy'''
# a = [10,20,30,40,50]
# b = a.copy()
# print(b)
# b[0] = 100
# print(b)
'''Here basically the copy() function create another space for the variable in the memory '''
'''But'''
# print(a)
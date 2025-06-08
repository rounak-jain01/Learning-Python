'''Creating a program to print natural numbers from 1 to n without using loops '''


# def num(a):
#     if(a == 21):
#         return
#     print(a)
#     num(a + 1)


'''Recurrsion -> When we define a function inside a function'''
'''Backtracking -> is a process to store function '''
'''Using Stack Memory'''

def num(a):
    if(a == 21):
        return
    num(a + 1)
    print(a)


num(1)
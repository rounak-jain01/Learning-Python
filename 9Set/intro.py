#no dublicates in set
# a = [1,2,3,4,5,5,5,1,1,2,2]
# s = set(a)
# print(s)

'''Traversing over set'''
# a = {1,2,3,4,5,6}
# print(a[1]) #TypeError: 'set' object is not subscriptable

'''Concept of Hashing'''
# a = {"hello"}
# print(hash(a))

# a = {2,1,4,5,0}
# print(a)
# a = {2,1,4,5,0,"Hello"}
# print(a)

'''Looping in set'''
'''Only loop work in set'''
# a = {1,6,7,3,7,3,7,9,5,7}

# for i in a:
#     print(i,end=" ")


'''Method to perform Crud Operations'''

'''add an element in the set'''
# s = {10,20,30}
# s.add(23)
# s.add(40)

# print(s)

'''Remove all the element from the set'''
# s = {10,20,30}
# s.clear()
# print(s)


'''difference method = Returns a set containing the difference between two or more sets
'''

# s = {10,20,30,40}
# s2 = {30,40,50,60}

# print(s.difference(s2))
# print(s2.difference(s))

# Another tareeka

# print(s - s2)

'''difference_update() -> Removes the items in this set that are also included in another, specified set'''

# s = {10,20,30,40}
# s2 = {30,40,50,60}

# s -= s2
# print(s)


'''intersection()->Returns a set, that is the intersection of two other sets'''

# s = {10,20,30,40}
# s2 = {30,40,50,60}
# print(s.intersection(s2))
# print(s&s2)


'''issubset() -> Returns whether another set contains this set or not'''
# s1 = {1,2,3,4}
# s1 = {1,2,3,4,10}
# s2 = {1,2,3,4,5}

# print(s1.issubset(s2))
# print(s1 <= s2)

'''symmetric_difference() -> Returns a set with the symmetric differences of two sets'''

# s1 = {10,20,30,40}
# s2 = {30,40,50,60}

# print(s1^s2)


'''union() -> Return a set containing the union of sets'''
# s1 = {10,20,30,40}
# s2 = {30,40,50,60}

# print(s1 | s2)




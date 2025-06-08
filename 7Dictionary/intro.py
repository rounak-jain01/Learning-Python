"""Dictionary"""

# d = {}
# print(type(d))
'''Creating a dictionary'''
# d = {10 : 100, 20 : 200, 30 : 300, 40 : 400}
# print(d)
'''CRUD operation is dictionary'''
'''here key is use as indexes (Reading operatioin)'''
# print(d[40])

'''Adding an element is the dictionary (creation)'''
'''here we use update to add element in the dict'''

# d.update({50:500})
# print(d)


'''here we can also add values either the index is present or not'''
# d[50] = 500
# print(d)

'''update the value of value using key (Updation)'''
# d[10] = 900
# print(d)

'''deleting a value in the dict (Deletion)'''

# del d[40]
# print(d)

'''Traversing a/over dict'''
# for i in d:
    # print(i) #To traverse KEYs
    # print(d[i]) #To Traverse VALUEs

# d1 = {1 : "Hello", 2 : "Bro", 3 : "How"}
# s = ['are', 'you']

'''without using loop'''
# d1[4] = s[0]
# d1[5] = s[1]
# print(d1)

'''Join two dictionary'''

# d1 = {1:100,2:200,3:300}
# d2 = {4:400,5:500,6:600}
# d2 = {3:400,5:500,6:600} #it change the value of 3 from 300 to 400

# for i in d2:
#     d1[i] = d2[i]
#     d1.update(d2)
# print(d1)




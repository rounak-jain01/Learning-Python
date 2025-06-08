a = "Nature"
'''Here We can directly access the string without indexing'''
# for i in a:
#     print(i)

'''Here We can Access Index in a string'''
# for i in range(0,6):
#     print(f"{i} : {a[i]}")


'''What if the range of string is not known then we used Len() function'''
for i in range(0,len(a)):
    print(a[i])
''' Check if the number is Prime or not.'''

num = int(input("Enter a Number: "))       
for i in range(2,(num//2)+1):
    if (num % i == 0):
        print(num, "is Composite")
        break
else:
    print(num, "is Prime")


'''---Alternate Approach---'''
# count = 0

# for i in range(1,num+1):
#     if(num % i == 0):
#         count = count+1

# if(count == 2):
#     print("prime")
# else:
#     print("Non Prime")




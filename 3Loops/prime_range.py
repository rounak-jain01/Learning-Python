'''Prime Number Within a Range'''

# n1 = int(input("Enter Lower limit: "))
# n2 = int(input("Enter Upper limit: "))

# print(f"Prime Number Between {n1} and {n2} are ", end='')
# for i in range(n1,(n2+1)):
#     if i > 1:
#         for j in range(2,(i//2)+1):
#             if i % j == 0:
#                 break
#         else:
#             print(f"{i}", end=" ")

'''Alternate Approach'''
c = int(input("Tell a Number: "))
for i in range(2,(c+1)):
    a = i
    for i in range(2,(a//2)+1):
        if a % i == 0:
            break
    else:
        print(a)
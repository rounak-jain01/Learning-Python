'''Print the sum of all even & odd numbers in a range seperately.'''

num = int(input("Enter a Number: "))

even = 0
odd = 0

# for i in range(1,num+1,2):
#     odd += i
# print("Sum of All odd number from 1 to",num,"is",odd)

# for i in range(2,num+1,2):
#     even += i
# print("Sum of All even number from 1 to",num,"is",even)

for i in range(1,num+1):
    if num % i == 0:
        even += i
    else:
        odd += i

print("Sum of All Even number from 1 to",num,"is",even)
print("Sum of All odd number from 1 to",num,"is",odd)


'''Take a number as input and print its table
       5 * 1 = 5
       5 * 2 = 10 ... up to 10 terms
'''

num = int(input("Enter a number: "))

for i in range(1,11):
#     print(num,"*",i,"=",num*i)
    print(f"{num} * {i} = {num*i}") #Formatted String
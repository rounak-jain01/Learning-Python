'''Print natural number up to n.'''

num = int(input("Enter the Upper Limit to print Natural Numbers: "))

print("Natural Number From 1 -",num)
for i in range(1,num+1):
    print(i,end=" ")
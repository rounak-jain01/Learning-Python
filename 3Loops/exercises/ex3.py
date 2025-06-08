'''Reverse for loop. Print n to 1.'''

n = int(input("Enter the Upper limit to print numbers in reverse: "))

for i in range(n,0,-1):
    print(i, end=' ')
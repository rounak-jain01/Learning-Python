'''Print positive and negative elements of an List'''

l = [1,2,8,9,-6,-8,-6,-7,1,2,30]

print("Positive Elements")
for i in l:
    if (i >= 0):
        print(i,end=" ")

print("\nNegative Elements")
for i in l:
    if (i < 0):
        print(i,end=" ")
    
'''Mean of List elements.'''

l = [1,2,35,235,25,554,5,2342,5235,252]
sum = 0
for i in l:
    sum += i

print("Mean of the given list is ",(sum/len(l)))
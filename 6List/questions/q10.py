'''Check if List is sorted or not.'''

l = [1,2,3,4,5,6,7,8,9]

for i in range(len(l) - 1):
    if (l[i] <= l[i+1]):
        continue
    else:
        print("Your list is not sorted")
        break
else:
    print("Your List is Sorted")

'''Find the smallest element and print its index too.
   {2, 96, 69, 77, 145, 20} = Min element = 2 found at 0 index'''

l = [2, 96, 69, 77, 145, 20]
min = l[0]
ind = 0
for i in range(len(l)):
    if min > l[i]:
        min = l[i]
        ind = i

print(f"Max element = {min} found at {ind} index")
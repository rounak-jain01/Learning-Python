'''Find the greatest element and print its index too.
   {2, 96, 69, 77, 145, 20} = Max element = 145 found at 4 index'''

l = [2, 96, 69, 77, 145, 20]
maxi = l[0]
ind = 0
for i in range(len(l)):
    if maxi < l[i]:
        maxi = l[i]
        ind = i

print(f"Max element = {maxi} found at {ind} index")

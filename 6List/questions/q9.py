'''Find the second greatest element 
  {2, 96, 69, 77, 145, 20} = Second greatest element = 96'''

l = [2, 96, 69, 77, 145, 20]
max1 = l[0]
max2 = l[0]
for i in l:
    if max1 < i:
      max2 = max1
      max1 = i
    elif max2 < i:
      max2 = i

print(f"Second greatest element = {max2}")
        
'''Print list in ascending or descending order'''

l = [4,5,3,9,78,1,0,4]
for i in range(len(l) - 1):
    for j in range(len(l) - 1 - i):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
        
print("In Ascending Order: ")
print(l)

for i in range(len(l) - 1):
    for j in range(len(l) -1 - i):
        if l[j] < l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
        
print("In Descending Order: ")
print(l)

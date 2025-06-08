'''Print  List elements in reverse order'''

a = [2,4,5,6,7,8]
b = []
for i in range(len(a)-1,-1,-1):
    b.append(a[i])

print(b)
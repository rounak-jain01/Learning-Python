'''reverse a list k times'''

l = [10, 20, 30, 40, 50, 60]
k = 2

for i in range(k):
    first = l[0]
    for j in range(len(l)-1):
        l[j] = l[j+1]
    l[-1] = first

print(l)


 
l  = [45,35,4534534,534543,435435,4343,34,3,453,5]

for i in range(len(l)-1):
    for j in range(len(l) - 1 - i):
        if (l[j] > l[j+1]):
            l[j],l[j+1] = l[j+1],l[j]

print(l)
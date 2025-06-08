'''Convert a list to dictionary '''

l = [12,56,23,87,43,2,78]

d = {}

for i in range(len(l)):
    d[i] = l[i]

print(d)
'''count the frequency of each elements'''

l = [1,2,4,2,4,1,5,6,4,2,5,3,2,6,6,2,2]
# count = 0

# for i in l:
#     if i == 6:
#         count += 1

# print(count)

d = {}
for i in l:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print(d)
max = 0
for i in d:
    if max < d[i]:
        max = d[i]

for i in d:
    if d[i] == max:
        print(f"Maximum frewuency of number is {max}")
        break

'''Write a Python program to sum all the values in a dictionary.'''

d = {1:100,2:200,3:300}
sum = 0
for i in d:
    sum += d[i]
print(sum)
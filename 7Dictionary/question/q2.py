'''Write a Python script to merge two Python dictionaries.'''

d1 = {1:100,2:200,3:300,4:400,5:500}
d2 = {6:600,7:700,8:800,9:900,10:1000}

for i in d2:
    d1[i] = d2[i]
    
print(d1)
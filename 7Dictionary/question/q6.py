
d1 = {10:100,20:200,30:300}
d2 = {30:600,40:400,50:500}

for i in d2:
    if i in d1:
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)



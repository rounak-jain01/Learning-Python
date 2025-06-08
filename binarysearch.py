def bsearch(l,key):
    s = 0
    e = len(l) - 1
    while(s <= e):
        m = (s + (e - s) // 2)
        if key == l[m]:
            return (f"{key} is fount at index {m}")
        elif l[m] < key:
            s = m + 1
        else:
            e = m - 1
    return (f"{key} is not found in the list")

l  = [1,2,3,4,5,6,7,8,9,10]
key = 10
ans = bsearch(l,key)
print(ans)





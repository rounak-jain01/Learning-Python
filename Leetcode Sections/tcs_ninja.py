

def maxs(l,k):
    result = []
    for i in range(len(l)-k+1):
        a = l[i:i+k]
        b = max(a)
        result.append(b)
    return result

l = [-1,3,5,1,6,7,3]
k = 3

ans = maxs(l,k)
print(ans)
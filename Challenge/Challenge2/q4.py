#Write a function which gives you total number of perfect pairs from a list. Sample Input: - L = [1,2,2,1,3,4,3,1,4] Sample Output: - Pairs = 4 

def perfect(l):
    pair = 0
    counts = {}
    for i in l:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    for i in counts.values():
        pair = pair + i // 2
    return pair


l = [1,2,2,1,3,4,3,1,4]
ans = perfect(l)
print(ans)

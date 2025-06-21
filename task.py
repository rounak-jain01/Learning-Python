'''give the first non-repeating character in a string'''



def rpt(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char in s:
        if count[char] == 1:
            return char
    
    return "Not Found"  

str = "aaabedefaabd"
ans = rpt(str)
print(ans)

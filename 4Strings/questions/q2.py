'''Arrange string characters such that lowercase letters should come first'''

a = "NETfLix"
ans = ""
c = ""
#output = fixNETL

# for i in a:
#     if i.islower():
#         ans = ans + i

# for i in a:
#     if i.isupper():
#         ans = ans + i

# print(ans)

'''Alternate Approach'''
# for i in a:
#     if i.islower():
#         ans = ans + i
#     else:
#         c = c + i
# print(ans + c)
    
'''Another Method'''
for i in a:
    t = ord(i)
    if(t >= 97 and t <= 122):
        ans += i
    else:
        c += i

print(ans + c)
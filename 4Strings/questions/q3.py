'''Count all letters, digits, and special symbols from a given string'''
a = "P@#yn26at^&i5ve"
count_alpha = 0
count_num = 0
count_sc = 0
print(a)
# for i in a:
#     if(i.isalpha()):
#         count_alpha += 1
#     elif(i.isdigit()):
#         count_num += 1
#     else:
#         count_sc+=1

# print(f"Aplhabets : {count_alpha}, Digits : {count_num} and Special Characters : {count_sc}")

'''Alternate Method'''

for i in a:
    t = ord(i)
    if (t >= 65 and t <= 90) or (t >= 97 and t <= 122):
        count_alpha+=1
    elif (t >= 48 and t <= 57):
        count_num+=1
    else:
        count_sc+=1
print(f"Aplhabets : {count_alpha}, Digits : {count_num} and Special Characters : {count_sc}")
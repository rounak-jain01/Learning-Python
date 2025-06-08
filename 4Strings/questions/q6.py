'''Reverse a string'''

s = input("Enter a string: ")


'''Brute Force Approach'''
# rev = ""
# for i in range(len(s)-1,-1,-1):
#     rev += s[i]

# print(rev)

# if s == rev:
#     print("Given String is Palindrome")
# else:
#     print("Goven String is not a Palindrome")

'''Alternate Appraoch (Two Pointer Approach)'''
# start = 0
end = len(s)-1
for i in range(0,len(s)//2):
    if s[i] != s[end]:
        print("Given string is not a palindrome")
        break;
    end -=1
else:
    print("Given String is Palindrome")

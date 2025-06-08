'''Write a function to check if a password is strong. Criteria:
•	≥ 8 characters
•	1 uppercase, 1 lowercase, 1 digit, 1 special character
Sample Input:    Pass@123
Sample Output: Strong Password
'''

def passstrong(str):
    ucheck = 0
    dcheck = 0
    lcheck = 0
    scheck = 0
    if len(str) >= 8:
        for i in str:
            if i.isupper():
                ucheck = 1
            elif i.islower():
                lcheck = 1
            elif i.isdigit():
                dcheck = 1
            else:
                scheck = 1
        if (ucheck == lcheck == dcheck == scheck == 1):
            return "Strong Password"

    return "Not a Strong Password"


ans = passstrong("Pass@123")
print(ans)

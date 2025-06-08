s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")

if len(s1) == len(s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            print("Strings are Not Equal")
            break
    else:
        print("Strings are Equal")
else:
    print("Strings are Not Equal")
    
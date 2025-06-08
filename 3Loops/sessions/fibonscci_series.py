# n = int(input("Enter a Number: "))
# n1 = 0
# n2 = 1

# def fobo(n,n1,n2):
#     for i in range(n):
#         print(n1)
#         n1, n2 = n1 + n2,n1

# fobo(n,n1,n2)

# sum = 1

# while(n != 0):
#     temp = n % 10
#     sum = sum + (temp**2)
#     n //= 10

# print(sum)

# n = input("Enter a Number: ")
# sum = 0
# for i in range(len(n)):
#     sum+= int(n[i])
# print(sum)

n = input("Enter num: ")

if (n[::] == n[::-1]):
    print("palindrome")
else:
    print("Not")


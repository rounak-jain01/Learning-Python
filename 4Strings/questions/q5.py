'''Count Vowels from given string'''

s = input("Enter a string: ")
count = 0
for i in s:
    if i in "AEIOUaeiou":
        count+=1

print(f"Count of Vowels in the given string {s} is: {count}")
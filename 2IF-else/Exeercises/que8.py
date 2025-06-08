'''Accept an english alphabet from user and check if it is a consonent or a vowel;'''

letter = input("Enter a English Alphabet to check whether it is vowel or consonent: ")

# if((letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u') or (letter == 'A') or (letter == 'E') or (letter == 'I') or (letter == 'O') or (letter == 'U')):
#     print(letter, "is a vowel")
# else:
#     print(letter, "is a consonent")

'''alternate method using " in " operator''' 
if letter in "aeiouAEIOU":
    print(letter, "is a Vowel")
else:
    print(letter, "is a consonent")
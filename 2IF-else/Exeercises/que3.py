'''Accept the gender from the user as char and print the respective greeting message
     Ex - Good Morning Sir (on the basis of gender)'''

gender = input("Please input Your Gender Male or Female: ")

if(gender == "Male" or gender == "male"):
    print("Good Morning Sir")
elif(gender == 'Female' or gender == 'female'):
    print("Good Morning Mam")
else:
    print("Please Select between Male or Female")
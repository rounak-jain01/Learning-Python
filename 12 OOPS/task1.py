'''Create 3 stundents save name,age,email,gender'''
'''also roll number'''
count = 0
class Student:
    def __init__(self,name,age,email,gender):
        global count
        self.name = name
        self.age = age
        self.email = email
        self.gender = gender 
        count += 1
        self.roll = count

    def showdetails(self):
        print(f"Your Details are\nName = {self.name},\nAge = {self.age},\nEmail = {self.email},\nGender = {self.gender},\nRoll Number = {self.roll}")


stdname = []
s1 = Student("Rounak",20,"hello@gmail.com","Male")
s2 = Student("Rohit",23,"hello123@gmail.com","Male")
s3 = Student("Ram",25,"hello321@gmail.com","Male")

s3.showdetails()
from pathlib import Path
import json
import random 
import string


class Bank:
    __database = "data.json"
    data = []

    try:
        if Path(__database).exists():
            with open(__database) as fs:
                data = json.loads(fs.read())

    except Exception as err:
        print(f"Error Occured as {err}")

    @classmethod
    def update_data(cls):
        with open(cls.__database, 'w') as fs:
            json.dump(cls.data,fs)

    @classmethod
    def generateAcc(cls):
        alpha = random.choices(string.ascii_letters,k=4)
        digits = random.choices(string.digits,k=8)
        id = alpha+digits
        random.shuffle(id)
        return "".join(id)


    def createuser(self):
        info = {
            "name": input("Enter your name: "),
            "email": input("Enter your email: "),
            "age": int(input("Enter your age: ")),
            "phonenumber": input("Enter your phone number: "),
            "AccountNo.": bank.generateAcc(),
            "pin": input("Enter your pin: "),
            "balance": 0
        }

        if info["age"] < 18:
            print("Your account cannot be created. You are not balik...")

        if len(info["phonenumber"]) != 10 or len(info["pin"]) != 4:
            print("Invalid input. Please try again later...")


        print(f"Please keep your account number safe: {info['AccountNo.']}")
        Bank.data.append(info)
        Bank.update_data()


    def depositMoney(self):
        acc = input("Please Enter Your Account Number ")
        pin = input("Please Enter Your Pin ")

        userdata = [i for i in Bank.data if i["AccountNo."] == acc and i["pin"]== pin]
        if not userdata:
            print("No data Found for this User ")
            
        else:
            amt = int(input("Enter Your Amount "))
            if (amt <= 0):
                print("Please Input a Valid Amount ")
            elif amt > 10000:
                print("Amount is Greater than 10000")
            else:
                userdata[0]["balance"] += amt
                Bank.update_data()
                print("Money Deposited Successfully")


    def withdrawlMoney(self):
        acc = input("Please Enter Your Account Number ")
        pin = input("Please Enter Your Pin ")
        userdata = [i for i in Bank.data if i["AccountNo."] == acc and i["pin"]== pin]
        if not userdata:
            print("No data Found for this User ")
        else:
            amt = int(input("Enter Amount to withdrawl "))
            if amt > 10000:
                print("You can withdrawl between 0-10000 only")
            elif amt == 0:
                print("Please Enter a Valid Amount")
            else:
                if userdata[0]["balance"] < amt:
                    print("Insufficient Funds")
                else:
                    userdata[0]["balance"] -= amt
                    Bank.update_data()
                    print(f"{amt} Withdrawl Successfully")

    def details(self):
        acc = input("Please Enter Your Account Number ")
        pin = input("Please Enter Your Pin ")
        userdata = [i for i in Bank.data if i["AccountNo."] == acc and i["pin"]== pin]
        if userdata == False:
            print("No user data Found")
        else:
            print("User Details are: ")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def Update_details(self):
        # Update user details except account number and balance
        Ac = input("Enter your account number: ")
        pin = input("Enter your 4 digit pin: ")
        user_data = [i for i in Bank.data if i["AccountNo."] == Ac and i["pin"] == pin]
        if not user_data:
            print("Sorry, no data found for this account number or pin.")
            return
        else:
            print("You cannot change your account number")
            print(
                "Now update your details and skip the field you don't want to change."
            )
            # Collect new info, allow skipping fields
            New_info = {
                "name": input("Enter your name : "),
                "email": input("Enter your email : "),
                "age": input("Enter your age : "),
                "phonenumber": input("Enter your phone number : "),
                "pin": input("Enter your pin : "),
            }

            # If a field is left blank, keep the old value
            for key in New_info:
                if New_info[key] == "":
                    New_info[key] = user_data[0][key]

            # Preserve account number and balance
            New_info["AccountNo."] = user_data[0]["AccountNo."]
            New_info["balance"] = user_data[0]["balance"]
            # Update the user data with new information
            for key in New_info:
                if key == "age":
                    new_age = input("Enter your age : ")
                    if new_age == "":
                        New_info["age"] = user_data[0]["age"]
                    else:
                        New_info["age"] = new_age  # keep as string
                elif key in ["phonenumber", "pin"]:
                    user_data[0][key] = str(New_info[key])
                else:
                    user_data[0][key] = New_info[key]
            Bank.update_data()
            print("Your details have been updated successfully.")

    def delete_account(self):
        # Delete a user's account
        Ac = input("Enter your account number: ")
        pin = input("Enter your 4 digit pin: ")
        user_data = [i for i in Bank.data if i["AccountNo."] == Ac and i["pin"] == pin]
        if not user_data:
            print("Sorry, no data found for this account number or pin.")
            return
        else:
            Bank.data.remove(user_data[0])
            Bank.update_data()
            print("Your account has been deleted successfully.")


bank = Bank()


a = True
while(a):
    check = int(input("""
    Press 1 to create a bank account: 
    Press 2 For deposit Money
    Press 3 for Withdrawl Money
    Press 4 to View Details
    Press 5 to update your details:
    Press 6 to delete your account:
    Press 0 for Exit
    """))

    if check == 1:
        bank.createuser()

    if check == 2:
        bank.depositMoney()

    if check == 3:
        bank.withdrawlMoney()

    if check == 4:
        bank.details()

    if check == 5:
        bank.Update_details()

    if check == 6:
        bank.delete_account()

    if check == 0:
        a = False
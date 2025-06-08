'''Access Modifiers'''
'''
1) Public : to private any attribute/Method just put __(double underscore) before the name of attribute and method
2) Protected :  to private any attribute/Method just put _ (single underscore) before the name of attribute and method
3) Private : 
'''


class Hide:

    __pincode = "34532123445"
    @classmethod
    def bankDetails(cls):
        # print(cls.__pincode)
        print(f"Name is SBI, ACCOUNT NUMBER : 465326778534")



'''Anyone can access your methods and attribute that is public'''
'''Only your inherited class can access your methods and attributes this is protected'''
'''No one can access your atttrbutes and methods this is Private'''

obj = Hide()
obj.bankDetails()

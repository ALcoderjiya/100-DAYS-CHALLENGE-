#Validate Phone number Entered by User
def isPhoneValid(phone):
    if len(phone) != 10:
        return False
    elif not phone.isdigit():
        return False
    elif phone[0] not in ("6789"):
        return False
    else:
        return True

txt = input("Enter phone number : ")
if isPhoneValid(txt):
    print("Phone Number is valid")
else:
    print("Phone Number is Invalid")

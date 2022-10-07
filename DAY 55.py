#DAY 55 CHECK IF AN EMAIL ID IS VALID OR NOT
'''
email = input("Enter Email-id : ")

if email.endswith(".com"):
    if email[0] != '@' and email.count("@") == 1:
        for ch in email:
            if ch.isalpha() or ch.isdigit() or ch == "." or ch == "_" or ch == "@":
                continue
            else:
                print("Valid Email id ")
                break
        else:
            print("Valid Email id ")
    else:
        print("Not a Valid Email id")
    print("Valid Emmail id")
else:
    print("Not a Valid Email id ")

'''
#or

def isValidEmail(email):
    if email.endswith(".com"):
        if email[0] != '@' and email.count("@") == 1:
            for ch in email:
                if ch.isalpha() or ch.isdigit() or ch == "." or ch == "_" or ch == "@":
                    continue
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False
    
email = input("Enter Email-id :")
if isValidEmail(email):
    print("Valid email id")
else:
    print("Not a Valid Email id")
    

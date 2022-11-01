#DAY 60 LOGIN SCREEN
'''
for k in range(3):
    userid = input("Enter the user id : ")
    passw = input("Enter the Password : ")

    if userid.lower() == "jiya" and passw.lower() == "python":
        print("Password Matched !!!")
        break
    else:
        print("Invalid User Id or Password")
else:
    print("Access  Denied")

'''

#using dictionary
password = {"xyz":"mnn","abc":"qwe","lmn":"yui"}
userid = input("Enter the user id : ")
passw = input("Enter the Password : ")
for i in password:
    if passw in password[i]:
        print("Password matched !!!")
        break
    else:
        print("Invalid User Id or Password")


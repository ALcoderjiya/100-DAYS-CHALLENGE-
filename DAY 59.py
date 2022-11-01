#Check strength of a password
password = input("Enter the required password : ")
n = len(password)
if n >= 8 and n <= 16:
    c = 0
    s = 0
    d = 0
    b = 0
    a = 0
    for ch in password:
        if ch.isupper():
            c+=1
        elif ch.islower():
            s+=1
        elif ch.isdigit():
            d+=1
        elif ch in ".,:!@#$%^&*()~?<>":
            b+=1
        else:
            a += 1
            break
    if a !=0:
        print("Invalid Password")
    else:
        if c > 0 and s >0 and d > 0 and b > 0:
            print("Password Strength is Strong")
        else:
            print("Weak password")
else:
    print("Password must have minimum of 8 characters and maximum of 16")
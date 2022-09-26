#STRING PALINDROME
txt = input("Enter a String : ")
rev = txt[::-1]
print("String is ",txt)
print("Reverse is ",rev)
if txt == rev:
    print("It is a Palindrome ")
else:
    print("It is not a Palindrome")

'''
#OR 
txt = input("Enter a String : ")
rev = ""
for i in range(len(txt)-1,-1,-1):
    rev += txt[i]
    
print("String is ",txt)
print("Reverse is ",rev)
if txt == rev:
    print("It is a Palindrome ")
else:
    print("It is not a Palindrome")

'''
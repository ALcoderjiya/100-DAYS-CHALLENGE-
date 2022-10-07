#DAY 54 TOGGLE CASE A STRING
txt = input("Enter a String : ")

result = ""
for ch in txt:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch

print("Original String ",txt)
print("Resultant String ",result)


'''
#or 
txt = input("Enter a String : ")

result = ""
for ch in txt:
    
    if ord(ch) >= 97 and ord(ch) <=122:
        result += chr(ord(ch)-32)
    elif ord(ch) >= 65 and ord(ch) <= 90:
        result += chr(ord(ch)+32)
    else:
        result += ch

print("Original String ",txt)
print("Resultant String ",result)
'''
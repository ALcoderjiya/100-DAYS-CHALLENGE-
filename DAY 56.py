#DAY 56 Generating Four Digits OTP
'''
import random as rd
otp = []
for i in range(4):
    digit = rd.randint(0,9)
    otp.append(digit)

print("Your OTP is : ",end =' ')
for d in otp:
    print(d,end=' ')
'''
'''
#If we want digits shouldn't be repeated 
import random as rd
otp = []
i = 0
while i < 4:
    digit = rd.randint(0,9)
    if digit not in otp:
        otp.append(digit)
        i += 1

print("Your OTP is : ",end =' ')
for d in otp:
    print(d,end=' ')
    
'''
#or using function

import random as rd
def generateotp():
    otp = []
    i = 0
    while i < 4:
        digit = rd.randint(0,9)
        if digit not in otp:
            otp.append(digit)
            i += 1
    return otp

otp = generateotp()
print("Your OTP is :",end = ' ')
for d in otp:
    print(d,end = ' ')


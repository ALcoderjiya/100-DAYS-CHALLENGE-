#DAY 61 COUNT NUMBER OF VOWELS IN A TEXT FILE
'''
#to write in text file to count vowels
f = open("story.txt","w")
f.write("Thus is a sample file which we are creating using a Python Program.\n")
f.write("This file will be used through another program to process its Data.\n")
f.write("Thank you ")
f.close()
'''
'''
#to count the vowels
f = open("story.txt","r")
data = f.read()
print(data)
vowels = 0
for ch in data:
    if ch in "aeiouAEIOU":
        vowels += 1
print("No. of Vowels is",vowels)
f.close()
'''
f = open("story.txt","r")
data = f.read()
u = 0 #counter of uppercase
l = 0 #counter of lowercase
d = 0 #counter of digit
x = 0 #counter of extra character
for ch in data:
    if ch.isupper():
        u += 1
    elif ch.islower():
        l += 1
    elif ch.isdigit():
        d += 1
    else:
        x += 1
print("Number of Capital letter in the file ",u)
print("Number of Small letter in the file ",l)
print("Number of Digit in the file ",d)
print("Number of Extra Characters ",x)


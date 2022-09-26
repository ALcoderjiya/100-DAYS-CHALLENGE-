#DAY 46 REVERSE A STRING WORD BY WORD
txt = input("Enter the string to be reversed : ")

words = txt.split()
words = words[::-1]
print(words)
res = ""
for w in words:
    res += w + " "

res = " ".join(words)
print(res)
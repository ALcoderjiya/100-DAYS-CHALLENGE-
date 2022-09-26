#DAY 45 NUMBER OF VOWELS IN A STRING
txt = input("Enter a String : ")

c = 0

for ch in txt:
    if ch in 'aeiouAEIUO':
        c += 1

print("Number Of vowels ",c)

#DAY 53 COUNT THE FREQUENCY OF EACH LETTER IN A STRING
txt = input("Enter a String : ").upper()
d = {}
for ch in txt:
    if ch not in d :
        d[ch] = 1
    else:
        d[ch] += 1
for k in d:
    print(k," occurs for ",d[k]," times")
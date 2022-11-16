#DAY 67 CHECH IF WORD IS EASY TO PRONOUNCE OR NOT
word = input("Enter a word : ")

c = 0
for ch in word:
    if ch.isalpha():
        if ch not in 'aeiuoAEIOU':
            c += 1
            if ch == 4:
                print("It is Difficult to pronounce")
                break
        else:
            c = 0
    else:
        print("Invalid Input")
        break
else:
    print("It is easy to Pronounce")

#DAY 33 Guessing game
import random as rd
num = rd.randint(10,60)
low = 10
high = 60
chance = int(input("Enter the number of times you have to try yourself :"))

for i in range(chance):
    guess = int(input("Enter a number between "+ str(low) +  " to " + str(high) + " : "))
    if guess == num:
        print("<>"*30)
        print("                     YOU WIN !!!             ")
        print("<>"*30)
        break
    elif num > guess:
        print("Sorry, but the number is greater than your guess")
        low = guess + 1
    elif num < guess:
        print("Sorry, but the number is lesser than your guess ")
        high = guess - 1

else:
    print("<>" * 30)
    print("                     YOU LOSE !!!             ")
    print("<>" * 30)

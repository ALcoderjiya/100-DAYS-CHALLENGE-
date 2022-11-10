#DAY 65 TIC TAC TOE
grid = {1 : " ",2 : " ",3 : " ",4 : " ",5 : " ", 6 : " ",7 : " ",8 : " ",9 : " "}
def show():
    print()
    print("-"*13)
    print("| " + grid[1]+ " | " + grid[2]+ " | " + grid[3] + " |")
    print("-"*13)
    print("| " + grid[4] + " | " + grid[5] + " | " + grid[6] + " |")
    print("-" * 13)
    print("| " + grid[7] + " | " + grid[8] + " | " + grid[9] + " |")
    print("-" * 13)
    print()

p1 = input("Enter Player 1's Name : ")
p2 = input("Enter Player 2's Name : ")

turn = 1

while True:
    show()
    if turn %2 == 1:
        pos = int(input(p1 + " Enter the Position to place X :  "))
        if pos in grid and grid[pos] == " ":
            grid[pos] = "X"
            turn += 1

    else:
        pos = int(input(p2 + " Enter the Position to place O :  "))
        if pos in grid and grid[pos] == " ":
            grid[pos] = "O"
            turn += 1

    if grid[1] == grid[2] == grid[3] and grid[1] != " ":
        if grid[1] == "X":
            print(p1," Wins !!!")
        else:
            print(p2 , "Wins !!!")
        show()
        break
    elif grid[4] == grid[5] == grid[6] and grid[4] != " ":
        if grid[4] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif grid[7] == grid[8] == grid[9] and grid[7] != " ":
        if grid[7] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif grid[1] == grid[4] == grid[7] and grid[7] != " ":
        if grid[1] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif grid[2] == grid[5] == grid[8] and grid[2] != " ":
        if grid[2] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif grid[3] == grid[6] == grid[9] and grid[9] != " ":
        if grid[3] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif grid[1] == grid[5] == grid[9] and grid[1] != " ":
        if grid[1] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif grid[3] == grid[5] == grid[7] and grid[7] != " ":
        if grid[3] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif turn > 9:
        print("Its a Draw")
        break
'''
#single player and computer
import random as rd
ch = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
grid = {1 : " " ,2 : " " ,3 : " " ,4 : " " ,5 : " ", 6 : " " ,7 : " " ,8 : " " ,9 : " "}

def show():
    print()
    print("- " *13)
    print("| " + grid[1 ]+ " | " + grid[2 ]+ " | " + grid[3] + " |")
    print("- " *13)
    print("| " + grid[4] + " | " + grid[5] + " | " + grid[6] + " |")
    print("-" * 13)
    print("| " + grid[7] + " | " + grid[8] + " | " + grid[9] + " |")
    print("-" * 13)
    print()

p1 = input("Enter Player 1's Name : ")
p2 = print("Player 2's Name : computer")

turn = 1

while True:
    r = rd.choice(ch)
    show()
    if turn %2 == 1:
        pos = int(input(p1 + " Enter the Position to place X :  "))
        if pos in grid and grid[pos] == " ":
            grid[pos] = "X"
            turn += 1


    else:
        pos = print("Computer entered ", r)
        if r in grid:
            grid[r] = "O"
            turn += 1
            ch.remove(r)

    if grid[1] == grid[2] == grid[3] and grid[1] != " ":
        if grid[1] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, "Wins !!!")
        show()
        break
    elif grid[4] == grid[5] == grid[6] and grid[4] != " ":
        if grid[4] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif grid[7] == grid[8] == grid[9] and grid[7] != " ":
        if grid[7] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif grid[1] == grid[4] == grid[7] and grid[7] != " ":
        if grid[1] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif grid[2] == grid[5] == grid[8] and grid[2] != " ":
        if grid[2] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif grid[3] == grid[6] == grid[9] and grid[9] != " ":
        if grid[3] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif grid[1] == grid[5] == grid[9] and grid[1] != " ":
        if grid[1] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif grid[3] == grid[5] == grid[7] and grid[7] != " ":
        if grid[3] == "X":
            print(p1, " Wins !!!")
        else:
            print(p2, " Wins !!!")
        show()
        break
    elif turn > 9:
        print("Its a Draw")
        break
'''
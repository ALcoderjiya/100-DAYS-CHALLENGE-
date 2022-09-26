#DAY 27 Pattern Making
n = int(input("How many rows are there : "))
for a in range(n, 0, -1):
    for b in range(a, 0, -1): #or (1, a+1)
        print(b,end = ' ')
    print()

'''
n = int(input("How many rows are there : "))
for a in range(n, 0, -1):
    for b in range(1, a+1):
        print(chr(64+b),end = ' ')
    print()
    
n = int(input("How many rows are there : "))
for a in range(n, 0, -1):
    for b in range(1, a+1):
        print("*",end = ' ')
    print()
'''

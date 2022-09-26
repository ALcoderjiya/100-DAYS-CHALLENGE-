#DAY 34 LINEAR SEARCH
A = eval(input("Enter a List of Numbers : "))
num = int(input("Enter Number To be Searched :"))

cnt = 0
for i in range(len(A)):
    if A[i] == num:
        print("Found at Position ", i+1)
        cnt += 1

if cnt == 0:
    print("Number Not Found")
#DAY 38 SWAPPING OF HALF LIST
A = eval(input("Enter a list of Numbers :"))

print("Before Swap ",A)
n = len(A)
if n % 2 == 0:
    gap = n // 2
else:
    gap = n // 2 + 1

for  i in range(n//2):
    temp = A[i]
    A[i] = A[i+gap]
    A[i+gap] = temp

print("After swap ",A)
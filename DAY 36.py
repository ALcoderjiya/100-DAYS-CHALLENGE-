# DAY 36 REVERSING A LIST
A = eval(input("Enter a list of values: "))

n = len(A)

for  i in range( n // 2):
    A[i],A[n-1-i] = A[n-1-i],A[i]

print(A)

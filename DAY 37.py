#SWAP ADJACENT ELEMENTS
A = eval(input("Enter the list of Values : "))

print("Before Swap ",A)

for i in range(0, len(A), 2):
    if i+1 < len(A):
        temp = A[i] #or A[i],A[i+1] = A[i+1],A[1]
        A[i] = A[i+1]
        A[i+1] = temp

print("After Swap ",A)
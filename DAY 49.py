#DAY 49 ROTATE A LIST BY N POSITION
A = eval(input("Enter the list elements : "))
n = int(input("Enter the number of the positions to shift : "))
print(A)
'''
#or
A = A[n:] + A[:n]
#print(A)
'''
'''
#or
for i in range(n):
    temp = A.pop(0)
    A.append(temp)

print(A)

'''
#or
for i in range(n):
    temp = A[0]
    for j in range(len(A)-1):
        A[j] = A[j+1]
    A[-1] = temp
print(A)

#DAY 39 REMOVE DUPLICATES FROM A LIST
A = eval(input("Enter a list of Values :"))

print("Before Removal List is  ",A)
for val in A:
    if A.count(val) > 1:
        A.remove(val)

print("After Removal List is ",A)

#or

'''
D = []
print("Before Removal List is  ",A)
for val in A:
    if val not in D:
        A.append(val)

print("After Removal List is ",D)


#or
i = 0
print("Before Removal List is  ",A)

while i < len(A):
    if A.count(A[i]) > 1:
        A.remove(A[i])
    else:
        i+=1
        break
print("After Removal List is ",A)
'''
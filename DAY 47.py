#DAY 47 UNION & INTERSECTION OF TWO LISTS
A = eval(input("Enter List 1 : "))
B = eval(input("Enter List 2 : "))

U = A.copy()
I = []
for val in B:
    if val in A:
        I.append(val)
    else:
        U.append(val)
print("A = " ,A)
print("B = ",B)
print("Union of A and B is ",U)
print("Intersection of A and B is ",I)

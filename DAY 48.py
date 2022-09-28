#DAY 48 Cartesian Product of two lists
A = eval(input("Enter the element of first list : "))
B = eval(input("Enter the element of Second list : "))

R = []
for n1 in A:
    for n2 in B:
        R.append((n1,n2))

print("First List is ",A)
print("Second List is ",B)
print("Final Cartesian Product is ",R)

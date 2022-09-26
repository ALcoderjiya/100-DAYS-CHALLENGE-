#SELECTION SORTING
a = eval(input("Enter a list of Numbers : "))
n = len(a)

print("Before Swap ",a)

for i in range(n-1):
    for j in range(i+1,n):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print("After Swap ",a)
#DAY 44 INSERTION SORT
a = eval(input("Enter the list of Numbers : "))
n = len(a)

print("Before Swap ",a)

for i in range(1, len(a)):

    num = a[i]
    j = i-1
    while j >= 0 and num < a[j]:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = num

print("After Swap ",a)
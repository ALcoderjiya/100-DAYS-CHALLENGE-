#BUBBLE SORT
#in Ascending Order
a = eval(input("Enter a list of numbers : "))
print("Before Sort ",a)
n = len(a)
for i in range(n-1):
    for j in range(0,n-1-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print("After Sort ",a)

'''
#in Descending Order
a = eval(input("Enter a list of numbers : "))
print("Before Sort ",a)
n = len(a)
for i in range(n-1):
    for j in range(0,n-1-i):
        if a[j] < a[j+1]
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
'''
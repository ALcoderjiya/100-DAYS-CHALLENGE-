#SECOND HIGHEST NUMBER
A = eval(input("Enter the list of values : "))

m = 0
for num in A:
    if num > m:
        m = num

res = 0
for num in A:
    if num != m and num > res:
        res = num

print("Second Highest number is ",res)

'''
#or
m = max(A)
while m in A:
    A.remove(m)

res = max(A)
print("Second Highest number is ",res)
'''
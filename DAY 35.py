#DAY 35 BINARY SEARCH
A = eval(input("Enter a list of numbers : "))
#for example
#A = [10,23,28,32,36,45,59,65,77,88]
num = int(input("Enter the number to be searched : "))

beg = 0
end = len(A) - 1
while beg <= end:
    mid = (beg + end) // 2
    if A[mid] == num:
        print("\nFound at Position ", mid+1)
        break
    elif num > A[mid]:
        beg = mid + 1
    elif num < A[mid]:
        end = mid - 1
else:
    print("\nNot Fount")
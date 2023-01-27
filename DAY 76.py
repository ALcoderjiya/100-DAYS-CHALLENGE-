def partition(A ,left, right):
    i = left-1
    pivot = right
    for j in range(left,right):
        if A[j] < A[pivot]:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[pivot] = A[pivot],A[i+1]
    return i+1
def quicksort(A, left, right):
    if right - left > 1:
        p = partition(A,left,right)
        quicksort(A,left,p-1)
        quicksort(A,p+1,right)
    else:
        return
n = eval(input("Enter a list of numbers : "))
print("\t\tBEFORE SORTING ")
print(n)
quicksort(n,0,len(n)-1)
print("\t\tAFTER SORTING")
print(n)

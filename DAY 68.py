#DAY 68 FACTORIAL OF A NUMBER USING RECURSION
def factorial(num):
    if num == 1:
        return 1
    res = num * factorial(num - 1)
    return res

n = int(input("Enter n : "))
r = factorial(n)
print("Factorial of ",n," is ",r)
#Check if the Number is Strong Number or not
import math
num = int(input("Enter a Number : "))
s = 0
a  = num

while num > 0 :
    d = num % 10
    s += math.factorial(d)
    num = num // 10

print("Sum is  ", s)
if s ==a :
    print(a, " is a Strong Number ")
else:
    print(a," is not a Strong Number")

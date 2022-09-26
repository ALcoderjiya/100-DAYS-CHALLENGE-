#DAY 23 Sum of Series
#x+x^2/2!+x^3/3!+x^4/4!...x^n/n!
x = int(input("Enter value of x :"))
n = int(input("Enter value of n : "))
s = 0
p = 1
for a in range(1,n+1):
   p *= a
   s += x ** a / p

print("Sum of Series ",s)

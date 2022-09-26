#DAY 19 Sumof digits of a Number
num = int(input("Enter a Number : "))
s = 0
a = num
while num > 0:
   d = num % 10
   s += d
   num = num // 10
print("Sum of Digits of  ",a, " is ",s)

#DAY20 Palindrome number
num = int(input("Enter a number to be checked : "))
a = num
res = 0
while a > 0:
   d = a % 10
   res = res * 10 + d
   a = a // 10

print("Reverse of number is " ,res)

if num == res:
   print(num," is a Palindrome")
else:
   print(num," is not a Palindrome ")
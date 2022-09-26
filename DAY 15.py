#DAY 15 Prime number
num = int(input("Enter a number : "))
f = 0
for a in range(1,num+1):
   if num % a == 0:
      f += 1
if f == 2:
   print(num," is a  Prime Number")
else:
   print(num," is not a Prime Number")

'''
if num == 1:
   print(" 1 is not Prime")
else:
   for a in range(2,num):
       if num % a == 0:
         print(num," is not a Prime Number")
         break
   else:
      print(num," is a  Prime Number")
'''
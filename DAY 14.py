#DAY14 Prefect Number
num = int(input("Enter a number : "))
s = 0
for a in range(1,num):
   if num % a == 0:
      s += a

if s == num:
   print(num," is a Perfect Number ")
else:
   print(num," is not  a Perfect Number ")

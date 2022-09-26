#DAY 13 Factor of a number
num = int(input("Enter a number: "))

print("Factors of ",num," are : ")
a = 1
while a <= num:
   if num % a == 0:
      print(a)
   a += 1
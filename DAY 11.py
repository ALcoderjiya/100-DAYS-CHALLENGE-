#DAY 11 multiplication table of a number
num = int(input("Enter a number : "))
print("Multiplication Table of ",num, " is ")
for n in range(1,11):
   res = n * num
   print(num, "X", n, "=",res)

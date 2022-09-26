#DAY 12
num = int(input("Enter a number : "))
p = 1
for a in range(1,num+1): #or (num,0,-1)
   p = p * a #p *= a

print("Factorial of ",num," is ",p)

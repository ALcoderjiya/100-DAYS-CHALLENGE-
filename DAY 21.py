#DAY 21 Sum of Series
#1+1/2+1/3+1/4....
n = int(input("Enter n : "))
s = 0
for a in range(1,n+1):
   if a < n:
      print("1/"+str(a),end = ' + ')
   else:
      print("1/"+str(a))
   s += 1/a
print("Sum is ",round(s,2))
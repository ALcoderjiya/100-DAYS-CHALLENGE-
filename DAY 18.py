#DAY 18 Fibonacci Series
n = int(input("How many elements of Fibonacci Series are to be printed : "))
a = 0
b = 1
if n >= 2:
   print(a,b,end = ' ')
   for i in range(n):
      c = a +b
      print(c,end = ' ')
      a = b
      b = c
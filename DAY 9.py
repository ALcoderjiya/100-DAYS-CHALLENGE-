#DAY 9 Grade of a student as per percentage marks
per  = float(input("Enter the percentage marks secured : "))
if per >= 90:
   print("Grade is A+")
elif per >= 80 and per < 90:
   print("Grade is A")
elif per >= 60 and per < 80:
   print("Grade is B")
elif per >= 50 and per < 60:
   print("Grade is C")
elif per < 50:
   print("Grade  is D")
else:
   print("Grade is E")
# DAY 3 REPORT CARD
name = input("Enter name : ")
eng = float(input("Enter marks in English : "))
math = float(input("Enter marks in Maths: "))
sst = float(input("Enter marks in Social Science : "))
sci = float(input("Enter marks in Science : "))
hin = float(input("Enter marks in Hindi : "))
total = eng + math + sst + sci + hin
per = total / 5
print("~"*30)
print("Report Card for ",name)
print("~"*30)
print("Total Marks Scored ",total)
print("Percentage Marks ",per,"%")
if per >= 40:
   print("          Congratualtions !!! ")
else:
   print("           Sorry, Try Again")
print("~"*30)

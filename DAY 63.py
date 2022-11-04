#DAY 63 LOGIN SCREEN USING CSV FILE
import csv

uname = input("Enter Username : ")
passw = input("Enter Password : ")

f = open("user.csv","r")
cr = csv.reader(f)
for row in cr:
    if row[0] == uname and row[1] == passw:
        print("Welcome ",uname," Access Granted ")
        break
else:
    print("Invalid Username or Password")

f.close()
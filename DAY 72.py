#INSERTING A RECORD IN A TABLE
import mysql.connector

con = mysql.connector.connect(host="localhost",user = "root",database = "school")
if con.is_connected():
    rno = int(input("Enter Roll Number : "))
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    q = "insert into student values(%s,%s,%s)"
    values = (rno,name,age)
    cur1 = con.cursor()
    cur1.execute(q,values)
    con.commit()
    print("Student Inserted Successfully")
#Deleteing a record
import mysql.connector

con = mysql.connector.connect(host="localhost",user = "root",database = "school")
if con.is_connected():
    rno = input("Enter Roll Number to be deleted : ")
    q = "deleted from student where sid = "+ rno
    cur1 = con.cursor()
    cur1.execute(q)
    con.commit()
    print("Student Deleted Successfully")
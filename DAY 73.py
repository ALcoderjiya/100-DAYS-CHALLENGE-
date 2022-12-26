#Updating a record
import mysql.connector

con = mysql.connector.connect(host="localhost",user = "root",database = "school")
if con.is_connected():
    rno = int(input("Enter Roll Number of student to be updated : "))
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    q = "update student set name = %s, age = %s where sid = %s"
    values = (name,age,rno)
    cur1 = con.cursor()
    cur1.execute(q,values)
    con.commit()
    print("Student Updated Successfully")
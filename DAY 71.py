#DAY 71 PYTHON-SQL CONNECTIVITY
import mysql.conector

con = mysql.connector.connect(host="localhost",user = "root",database = "school")
if con.is_connected():
    q = "Select * from student"
    cur = con.cursor()
    cur.execute(q)
    res = cur.fetchall()
    for row in res:
        print("Id is ",row[0]," Name is ",row[1]," Age is ",row[2])
    if cur.rowcount == 0:
        print("Table is Empty")
    else:
        print(cur.rowcount," Students Processed ")
else:
    print("Error in Connection")


import mysql.connector as mycon
con = mycon.connect(host="localhost",use="root",passowrd="",databse="school")
if con.is_connected():
    an = int(input("Enter the admission no. of the student : "))
    q = "select * from student "
    cr = con.cursor()
    cr.execute(q)
    res = cr.fetchall()
    for row in res:
        if row[0] == an:
            print("Found")
            print(row)
            break
    else:
        print("Not Student Found with given ID ")
'''
#or 
import mysql.connector as mycon
con = mycon.connect(host="localhost",use="root",passowrd="",databse="school")
if con.is_connected():
    an = input("Enter the admission no. of the student : ")
    q = "select * from student where admno = "+ an
    cr = con.cursor()
    cr.execute(q)
    res = cr.fetchone()
    if len(res) != 0:
        print(res)
    else:
        print("Not Student Found with given ID ")
'''
